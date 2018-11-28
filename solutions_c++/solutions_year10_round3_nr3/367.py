#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

#include "Defines.h"

using namespace std;

template<class T>
T StringTo(const string& input)
{
	istringstream buffer(input);
	T out;
	buffer >> out;
	return out;
}

template<class T>
string ToString(const T& input)
{
	stringstream buffer;
	buffer << input;
	return buffer.str();
}

uint HexTo(const string& input)
{//only cares about the first element
	string first = input.substr(0,1);
	if(first == F)
	{
		return 15;
	}
	else if(first == E)
	{
		return 14;
	}
	else if(first == D)
	{
		return 13;
	}
	else if(first == C)
	{
		return 12;
	}
	else if(first == B)
	{
		return 11;
	}
	else if(first == A)
	{
		return 10;
	}
	else
	{
		return StringTo<uint>(first);
	}
}

bool ValidBoard(const BOARD& board, const N_TYPE& size, const N_TYPE& x, const N_TYPE& y)
{
	COLOUR first = board.at(y).at(x).colour;
	N_TYPE distance;//Manhattan distance
	ROW row;
	bool failed = false;
	if(board.at(y).at(x).used)
	{
		return false;
	}
	
	for(N_TYPE yIter = y;yIter < y + size;yIter++)
	{
		row = board.at(yIter);
		for(N_TYPE xIter = x;xIter < x + size;xIter++)
		{
			distance = (yIter - y) + (xIter - x);//abs unnecessary because all positive
			if(row.at(xIter).used)
			{
				failed = true;
			}
			else if(distance % 2 == 0)
			{//so it's an even number of steps away
				if(row.at(xIter).colour != first)
				{
					failed = true;
				}
			}
			else
			{
				if(row.at(xIter).colour == first)
				{
					failed = true;
				}
			}
			if(failed)
			{
				return false;
			}
		}
	}
	return true;
}

RESULT_TYPE CalculateResult(BOARD& board, const N_TYPE& m, const N_TYPE& n)
{
	RESULT_TYPE result = RESULT_TYPE();
	N_TYPE maximum = min(m,n);

	for(N_TYPE size = maximum;size > 0;size--)
	{
		for(N_TYPE y = 0;y <= m - size;y++)
		{
			for(N_TYPE x = 0;x <= n - size;x++)
			{
				if(ValidBoard(board,size,x,y))
				{//board with top-left at x,y is valid
					//set all the tiles to used
					for(N_TYPE yIter = y;yIter < y + size;yIter++)
					{
						for(N_TYPE xIter = x;xIter < x + size;xIter++)
						{
							board.at(yIter).at(xIter).used = true;
						}
					}
					if(result.count(size) > 0)
					{//we found a match of this size already
						result[size]++;
					}
					else
					{
						result.insert(COUNT_TYPE(size,1));
					}
				}
			}
		}
	}

	return result;
}

int main(int argc, char* argv[])
{
	ifstream file;
	ofstream output;
	bool inOpened = false, outOpened = false;
	//argv[0] is the executable path, argv[1] is the target input
	if(argc >= 2)
	{
		file.open(argv[1]);
		if(file)
		{
			inOpened = true;
		}
		if(argc >= 3)
		{
			output.open(argv[2]);
			if(output)
			{
				outOpened = true;
			}
		}
	}
	if(!inOpened)
	{
		file.open(defaultInput);
		if(file)
		{
			inOpened = true;
		}
		else
		{
			return EXIT_FAILURE;
		}
	}
	if(!outOpened)
	{
		output.open(defaultOutput);
		if(output)
		{
			inOpened = true;
		}
		else
		{
			return EXIT_FAILURE;
		}
	}

	string tStr, nStr, mStr, line, hex, test;
	size_t sepPos;
	T_TYPE T;
	N_TYPE M, N;
	ROW row;
	uint hexInt;
	BOARD board;
	RESULT_TYPE result;
	RESULT_TYPE::reverse_iterator iter;
	
	getline(file,tStr);
	T = StringTo<T_TYPE>(tStr);
	for(T_TYPE i = 0;i < T;i++)
	{
		getline(file,line);
		sepPos = line.find(separator);
		mStr = line.substr(0,sepPos);
		nStr = line.substr(sepPos + 1);
		M = StringTo<N_TYPE>(mStr);
		N = StringTo<N_TYPE>(nStr);

		board.clear();
		row.reserve(N);
		for(N_TYPE j = 0;j < M;j++)
		{
			row.clear();
			getline(file,line);
			for(N_TYPE k = 0;k < N/4;k++)
			{
				hex = line.at(k);
				hexInt = HexTo(hex);
				test = "";
				for(int l = 3;l >= 0;l--)
				{
					row.push_back((hexInt/int(pow(double(2),double(l)))) % 2);
				}
			}
			board.push_back(row);
		}

		result = CalculateResult(board,M,N);
		output << "Case #" << (i + 1) << ": " << result.size();
		
		for(iter = result.rbegin();iter != result.rend();iter++)
		{
			output << "\n" << (*iter).first << separator << (*iter).second;
		}
		if(i < T - 1)
		{
			//isn't the last one
			output << "\n";
		}
	}

	file.close();
	output.close();

	return EXIT_SUCCESS;
}