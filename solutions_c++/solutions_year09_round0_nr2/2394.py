// codejam2009_2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <tchar.h>

// TODO: reference additional headers your program requires here
#include <vector>
#include <iostream>
#include <math.h>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <cstring>
#include <bitset> 
#include <ctype.h>
#include <fstream>
#include <climits>
#include <stdio.h>
#include <stdlib.h>
#include <cstdio> 
#include <cstdlib> 
#include <time.h>
#include <ctime>
#include <wchar.h>
#include <wctype.h>
#include <cwchar> 
#include <cwctype> 
#include <complex>
#include <deque>
#include <exception>
#include <list>
#include <map>
#include <iomanip> 
#include <set>
#include <sstream>
#include <stack>
using namespace std; 

bool isBasin(vector<int> v, int row,int i)
{
	int column = v.size()/row;
	int r = i/column;
	int c = i%column;

	vector<int> neighbor(4,-1);
	
	if (r > 0)
	{
		neighbor[0] = v[(r-1)*column + c];		
	}
	if (c > 0)
	{
		neighbor[1] = v[r*column + c-1];		
	}
	if (c < column-1)
	{
		neighbor[2] = v[r*column + c+1];		
	}
	if (r < row-1)
	{
		neighbor[3] = v[(r+1)*column + c];		
	}
	
	int minimum = 20000;
	for (int j = 0; j < 4; j++)
	{
		if (neighbor[j] < minimum && neighbor[j] != -1)
		{
			minimum = neighbor[j];
		}
	}

	if (minimum >= v[i])
	{
		return true;	
	}

	return false;	
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inFile;
	inFile.open("B-large.in");
	if (!inFile)
	{
		cout << "Unable to open file." << endl;
		exit(1);
	}

	ofstream outFile;
	outFile.open("out.txt");
	if (!outFile)
	{
		cout << "Unable to open file." << endl;
		exit(1);
	}

	char str[1000];
	int map_num;
	
	inFile.getline(str,1000);
	
	string st(str);
	map_num = atoi(st.c_str());
	
	for (int i = 0; i < map_num; i++)
	{
		inFile.getline(str,1000);
		int H,W;
		string st2(str);
		
		int found = st2.find(' ');
		string str1,str2;

		str1 = st2.substr(0,found);
		str2 = st2.substr(found+1,st2.length()-found);
		H = atoi(str1.c_str());
		W = atoi(str2.c_str());
		vector<int> v;
	
		for (int j = 0; j < H; j++)
		{
			inFile.getline(str,1000);
			string str3(str);
			
			int found2 = str3.find_first_of(' ');
			if (found2 == string::npos)
			{
				v.push_back(atoi(str3.c_str()));
				continue;				
			}
			else
			{
				int pos = 0;
				string tmp;
				while (found2 != string::npos)
				{
					tmp = str3.substr(pos,found2-pos+1);
					v.push_back(atoi(tmp.c_str()));
					pos = found2 + 1;
					found2 = str3.find_first_of(' ',found2+1);
				}
				tmp = str3.substr(pos,found2-pos+1);
				v.push_back(atoi(tmp.c_str()));
			}						
		}			

		char ch = 'a';
		vector<char> state(H*W,' ');

		vector<int>	st;		

		for (int k = 0; k < H*W; k++)
		{
			if (state[k] == ' ')
			{
				while(!isBasin(v,H,k))
				{
					st.push_back(k);

					int column = v.size()/H;
					int r = k/column;
					int c = k%column;

					vector<int> nb(4,-1);
					int minimum = 20000;
					if (r > 0)
					{
						nb[0] = v[(r-1)*column+c];
					}
					if (c > 0)
					{
						nb[1] = v[r*column+c-1];
					}
					if (c < column-1)
					{
						nb[2] = v[r*column+c+1];
					}
					if (r < H-1)
					{
						nb[3] = v[(r+1)*column+c];
					}
					for (int z = 0; z < 4; z++)
					{
						if (minimum > nb[z] && nb[z] != -1)
						{
							minimum = nb[z];
						}
					}
					if (nb[0] == minimum)
					{
						k = (r-1)*column+c;
					}
					else if (nb[1] == minimum)
					{
						k = r*column + c - 1;
					}
					else if (nb[2] == minimum)
					{
						k = r*column + c + 1;
					}
					else if (nb[3] == minimum)
					{
						k = (r+1)*column+c;
					}					
				}
				if (state[k] == ' ')
				{
					state[k] = ch;
					ch++;					
				}
				for (int t = 0; t < st.size(); t++)
				{
					state[st[t]] = state[k];						
				}

				if (!st.empty())
				{
					k = st[0];
					st.clear();
				}
			}
		}

		outFile << "Case #" << i+1 << ": " << endl;
	
		for (int row = 0; row < H; row++)
		{
			for (int col = 0; col < W; col++)
			{
				outFile << state[row*W+col] << ' ';
			}
			outFile << endl;
		}
		v.clear();				
	}

	inFile.close();
	outFile.close();	
	
	return 0;
}

