#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

#include "Defines.h"

using namespace std;

template<class T>
T StringTo(const string input)
{
	istringstream buffer(input);
	T out;
	buffer >> out;
	return out;
}

bool ParseToNM(const string input, N_TYPE& n, M_TYPE& m)
{
	try
	{
		size_t sepPos = input.find(separator);
		string nStr = input.substr(0,sepPos), mStr = input.substr(sepPos + 1);
		n = StringTo<N_TYPE>(nStr);
		m = StringTo<M_TYPE>(mStr);
	}
	catch(...)
	{
		return false;
	}
	return true;
}

PATH_TYPE ParsePath(const string& input)
{
	string remainder = input.substr(1);//omit root slash
	size_t until = remainder.find(dirSeparator);
	PATH_TYPE res = PATH_TYPE();
	while((until = remainder.find(dirSeparator)) != string::npos)
	{
		res.push_back(remainder.substr(0,until));
		remainder = remainder.substr(until + 1);
	}
	res.push_back(remainder.substr(0,until));
	return res;
}

string PathsToString(const PATHS& input)
{
	string res = "";
	for(size_t i = 0;i < input.size();i++)
	{
		for(size_t j = 0;j < input.at(i).size() - 1;j++)
		{
			res.append(input.at(i).at(j) + dirSeparator);
		}
		res.append(input.at(i).at(input.at(i).size() - 1));
		if(i < input.size() - 1)
		{
			res.append("\n");
		}
	}
	return res;
}

RESULT_TYPE CalculateResult(PATHS& existing,PATHS& resulting)
{
	PATH_TYPE working = PATH_TYPE();
	PATH_TYPE* goal;
	bool found;
	RESULT_TYPE result = 0;
	for(size_t i = 0;i < resulting.size();i++)
	{
		goal = &resulting.at(i);
		for(size_t dir = 1;dir <= goal->size();dir++)
		{
			found = false;
			working.assign(goal->begin(),goal->begin() + dir);
			for(size_t search = 0;search < existing.size();search++)
			{
				if(existing.at(search) == working)
				{
					found = true;
					break;
				}
			}
			if(!found)
			{
				result++;
				existing.push_back(working);
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

	string tStr, line;
	T_TYPE T;
	N_TYPE N;
	M_TYPE M;
	PATHS present, desired;
	RESULT_TYPE result;
	
	getline(file,tStr);
	T = StringTo<T_TYPE>(tStr);
	for(T_TYPE i = 0;i < T;i++)
	{
		present.clear();
		desired.clear();
		getline(file,line);
		if(!ParseToNM(line, N, M))
		{
			return EXIT_FAILURE;
		}
		for(N_TYPE j = 0;j < N;j++)
		{
			getline(file,line);
			present.push_back(ParsePath(line));
		}
		for(M_TYPE k = 0;k < M;k++)
		{
			getline(file,line);
			desired.push_back(ParsePath(line));
		}
		result = CalculateResult(present,desired);
		output << "Case #" << (i + 1) << ": " << result;
		if(i < T - 1)
		{
			//isn't the last one
			output << "\n";
		}
	}

	file.close();
	output.close();

	//string trash;
	//getline(cin, trash);

	return EXIT_SUCCESS;
}