// SRM.cpp : Defines the entry point for the console application.
//
#pragma once
#include "stdafx.h"
//#include "vec.h"
//#include "BinaryTree.h"
//#include "lib.h"
//#include "exercise.h"

#include <vector>
#include <string>
#include <algorithm>
#include <vector>
#include <numeric>
#include <iostream>
#include <fstream>
#include <limits>
#include <functional>
#include <cmath>
#include <stdio.h>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <cctype>
#include <string>

using namespace std;
 
void gcj1();
void gcj2(); 
void gcj3();


int _tmain(int argc, _TCHAR* argv[])
{ 	 
	//gcj2();
	gcj3();
    return 0;
} 

 

//Google code jam 
vector<string> tokenize(const string& str, const string& delimiters = " ")
{     
	vector<string> tokens;
	string::size_type lastPos = str.find_first_not_of(delimiters, 0);     
	string::size_type pos  = str.find_first_of(delimiters, lastPos);

	while (string::npos != pos || string::npos != lastPos)
	{         
		tokens.push_back(str.substr(lastPos, pos - lastPos));         
		lastPos = str.find_first_not_of(delimiters, pos);        
		pos = str.find_first_of(delimiters, lastPos);
	}

	return tokens;
}

void gcj1()
{
	ifstream infile("E:\\input1.txt");
	ofstream outfile("E:\\output1.txt");
	int T;
	string str;
	getline(infile, str);
	T = atoi(str.c_str()); 	 

	vector<int> beg, end;
	//for (int i 
	 
	for (int t = 0; t < T; ++t)
	{	
		string res;

		getline(infile, str);
		vector<string> input = tokenize(str);		 
		int A1, A2, B1, B2;
		A1 = atoi(input[0].c_str());
		A2 = atoi(input[1].c_str());
		B1 = atoi(input[2].c_str());
		B2 = atoi(input[3].c_str());

		
						 		 	
		outfile << "Case #" << t + 1 << ": " << res << endl;		
	}

	infile.close();
	outfile.close();
}

int mincost(int a, int b, int D, int I, int M)
{
	int res;
	if (abs(a - b) > M)
	{
		res = D;
		if ((M != 0))
		{
			res = min(res, I * (abs(a - b - 1)  / M));
		}
		res = min(res, abs(a - b) - M);
		}
	else
	{
		res = 0;
	}
	return res;
}
 
void gcj2()
{
	ifstream infile("E:\\input2.txt");
	ofstream outfile("E:\\output2.txt");
	int T;
	string str;
	getline(infile, str);
	T = atoi(str.c_str()); 	 
	 
	for (int t = 0; t < T; ++t)
	{	
		int res;
		cout << t << endl;
		if (t == 10)
			int kk =0;
		

		getline(infile, str);
		vector<string> input = tokenize(str);		 
		int D, I, M, N;
		D = atoi(input[0].c_str());
		I = atoi(input[1].c_str());
	    M = atoi(input[2].c_str());
		N = atoi(input[3].c_str());

		getline(infile, str);
		input = tokenize(str);	
		vector<int> a;
		for (int i = 0; i < input.size(); ++i)
		{
			a.push_back(atoi(input[i].c_str()));
		}	


		if (N == 1)
		{
			res = 0;
		}
		else if (N == 2)
		{
			if (abs(a[0] - a[1]) <= M)
			{
				res = 0;
			}
			else
			{
				res = mincost(a[0], a[1], D, I, M);
			}
		}
		else
		{
			int tmp = a[0];
			if (a[2] < a[0])
			{
				a[0] = a[2];
				a[2] = tmp;
			}
			if ((abs(a[0] - a[1]) <= M) && (abs(a[1] - a[2]) <= M))
			{
				res = 0;
			}
			else if (abs(a[0] - a[1]) <= M)
			{
				res = mincost(a[1], a[2], D, I, M);
			}
			else if (abs(a[1] - a[2]) <= M)
			{
				res = mincost(a[0], a[1], D, I, M);
			}
			else
			{
				res = D + mincost(a[0], a[2], D, I, M);
				res = min(res, D + mincost(a[0], a[1], D, I, M));
				res = min(res, D + mincost(a[1], a[2], D, I, M));
				if (M != 0)
				{
					res = min(res, I * ((abs(a[0] - a[1]) - 1) / M) + mincost(a[1], a[2], D, I, M));
					res = min(res, I * ((abs(a[1] - a[2]) - 1) / M) + mincost(a[0], a[1], D, I, M));
				}
				
				if (abs(a[0]  - a[2]) <= 2 * M)
				{
					for (int i = a[0]; i <= a[2]; ++i)
					{
						if (((i - a[0]) <= M) && ((a[2] - i) <= M))
						{
							res = min(res, abs(i - a[1]));
						}
					}
				}
				for (int j = - M; j <= M; ++j)
				{
					for (int k = - M; k <= M; ++k)
					{
						int b = a[0] + j;
						int c = b + k;
						res = min(res, abs(b - a[1]) + abs(c - a[2]));

						b = a[1] + j;
						c = a[1] + k;
						res = min(res, abs(b - a[0]) + abs(c - a[2]));

						b = a[2] + j;
						c = b + k;
						res = min(res, abs(b - a[1]) + abs(c - a[0]));
					}
				}

				 

			}
		}
								 		 	
		outfile << "Case #" << t + 1 << ": " << res << endl;		
	}

	infile.close();
	outfile.close();
}

bool isrow(vector<string> board, char c, int N, int K)
{	
	for (int i = 0; i < board.size(); ++i)
	{
		for (int j = 0; j < board.size(); ++j)
		{
			if (board[i][j] == c)
			{
				if (j <= (N - K))
				{
					bool isstop = false;
					for (int k = j + 1; k < j + K; ++k)
					{
						if (board[i][k] != c)
						{
							isstop = true;
							//j = k;
							break;
						}
					}
					if (!isstop)
					{
						return true;
					}
				}

				if (i <= (N - K))
				{
					bool isstop = false;
					for (int k = i + 1; k < i + K; ++k)
					{
						if (board[k][j] != c)
						{
							isstop = true;
							//j = k;
							break;
						}
					}
					if (!isstop)
					{
						return true;
					}
				}
				
				
				if (j <= (N - K) && i <= (N - K))
				{
					bool isstop = false;
					for (int k = 1; k < K; ++k)
					{
						if (board[i + k][j + k] != c)
						{
							isstop = true;							
							break;
						}
					}
					if (!isstop)
					{
						return true;
					}
				}

				if ((j >= K - 1) && i <= (N - K))
				{
					bool isstop = false;
					for (int k = 1; k < K; ++k)
					{
						if (board[i + k][j - k] != c)
						{
							isstop = true;							
							break;
						}
					}
					if (!isstop)
					{
						return true;
					}
				}

			}
		}
	}		
	return false;
}

void gcj3()
{
	ifstream infile("E:\\input1.txt");
	ofstream outfile("E:\\output1.txt");
	int T;
	string str;
	getline(infile, str);
	T = atoi(str.c_str()); 	 
	 
	for (int t = 0; t < T; ++t)
	{	
		string res;

		getline(infile, str);
		vector<string> input = tokenize(str);		 

		int N = atoi(input[0].c_str());
		int K = atoi(input[1].c_str());

		vector<string> board;
		for (int i = 0; i < N; ++i)
		{
			getline(infile, str);			
			string tmp;
			for (int i = 0; i < N; ++i)
			{
				if (str[i] != '.')
					tmp.push_back(str[i]);
			}
			string str1(N - tmp.size(), '.');
			str1 = str1 + tmp;
			board.push_back(str1);
		}

		bool isred = isrow(board, 'R', N, K);
		bool isb = isrow(board, 'B', N, K);

		if (isred && isb)
		{
			res = "Both";
		}
		else if (isred)
		{
			res = "Red";
		}
		else if (isb)
		{
			res = "Blue";
		}
		else
		{
			res = "Neither";
		}
						 		 	
		outfile << "Case #" << t + 1 << ": " << res << endl;		
	}

	infile.close();
	outfile.close();
}