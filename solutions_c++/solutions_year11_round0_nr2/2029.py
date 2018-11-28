#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

string process(string input, char** mat, char** oppose, map<char, int> baseElem)
{
	string res = "";
	for(int i=0; i<(int)input.length(); i++)
	{
		if(res.empty())
			res += input[i];
		else
		{
			char lastChar = res[res.length() - 1];
			int col = -1;
			if(baseElem.find(lastChar) != baseElem.end())
			{
				col = baseElem[lastChar];
			}
			int row = baseElem[input[i]];
			if(col >= 0 && mat[col][row] > 0)
			{
				res[res.length()-1] = mat[col][row];
			}
			else
			{
				bool broken = false;
				for(int j=0; j<(int)res.length(); j++)
				{
					if(baseElem.find(res[j]) != baseElem.end())
					{
						col = baseElem[res[j]];
						if(oppose[col][row] == 1)
						{
							res.clear();
							broken = true;
							break;
						}
					}
				}
				if(!broken)
					res += input[i];
			}
		}
	}
	return res;
}

void main()
{
	map<char, int> baseElem;
	baseElem['Q'] = 0;
	baseElem['W'] = 1;
	baseElem['E'] = 2;
	baseElem['R'] = 3;
	baseElem['A'] = 4;
	baseElem['S'] = 5;
	baseElem['D'] = 6;
	baseElem['F'] = 7;

	ifstream f("Input.txt");
	ofstream outFile("Output.txt");
	int T;
	f >> T;
	for(int i=0; i<T; i++)
	{
		int C, D, N;
		char** mat = new char*[8];
		char** oppose = new char*[8];
		for(int j=0; j<8; j++)
		{
			mat[j] = new char[8];
			oppose[j] = new char[8];
			memset(mat[j], 0, 8);
			memset(oppose[j], 0, 8);
		}

		int col, row;
		string input;
		string tmp;
		f >> C;
		for(int j=0; j<C; j++)
		{
			f >> tmp;
			col = baseElem[tmp[0]];
			row = baseElem[tmp[1]];
			mat[col][row] = tmp[2];
			mat[row][col] = tmp[2];
		}
		f >> D;
		for(int j=0; j<D; j++)
		{
			f >> tmp;
			col = baseElem[tmp[0]];
			row = baseElem[tmp[1]];
			oppose[col][row] = 1;
			oppose[row][col] = 1;
		}
		f >> N;
		f >> input;
		string res = process(input, mat, oppose, baseElem);
		outFile << "Case #" << i+1 << ": " << "[";
		for(int j=0; j<(int)res.length(); j++)
		{
			outFile << res[j];
			if(j < (int)res.length() - 1)
				outFile << ", ";
		}
		outFile << "]" << endl;
	}
	outFile.close();
	f.close();
}