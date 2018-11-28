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
void gcj4();

int _tmain(int argc, _TCHAR* argv[])
{ 	 
	 
    gcj3();
    return 0;
} 


vector<string> tokenize(const string& str, const string& delimiters = " ");


//Google code jam 



void gcj4()
{
	ifstream infile("E:\\input4.txt");
	ofstream outfile("E:\\output4.txt");
	int T;
	string str;
	getline(infile, str);
	T = atoi(str.c_str()); 	  
	 
	for (int t = 0; t < T; ++t)
	{	
		int res = 0;
		getline(infile, str);
		vector<string> input = tokenize(str);		 
		int N = atoi(input[0].c_str());
		int M = atoi(input[1].c_str());

		vector<double> px, py, qx, qy;

		for (int i = 0; i < N; ++i)
		{
			getline(infile, str);
			vector<string> input = tokenize(str);
			px.push_back(atoi(input[0].c_str()));
			py.push_back(atoi(input[1].c_str()));
		}	

		for (int i = 0; i < M; ++i)
		{
			getline(infile, str);
			vector<string> input = tokenize(str);
			double qx = atoi(input[0].c_str());
			double qy = atoi(input[1].c_str());



		}

	
						 		 	
		outfile << "Case #" << t + 1 << ": " << res << endl;		
	}

	infile.close();
	outfile.close();
} 

int mincost(vector<int> M, vector<vector<int> > tickets, int P, int& minid)
{
	int res = 0;

	if (M.size() == 2)
	{
		if (M[0] > 0 || M[1] > 0)
			return tickets[0][0];
		else
			return 0;
	}

	int tmp = 0;
	for (int i = 0; i < M.size(); ++i)
	{
		tmp = max(tmp, M[i]);
	}

	if (tmp <= 0)
		return 0;
	
    minid = - 1;
	int mincost = 1e7;
	for (int i = 0; i < M.size(); ++i)
	{		
		if (M[i] == tmp)
		{
			int tmpcost = 0;
			int id = i;
			for (int j = 0; j < tmp; ++j)
			{
				id /= 2;
				tmpcost += tickets[j][id];				
			}

			if (tmpcost < mincost)
			{
				mincost = tmpcost;
				minid = i;				
			}
		}
	}

	return mincost;

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
		int res = 0;
		getline(infile, str);
		vector<string> input = tokenize(str);		 
		int P = atoi(input[0].c_str());
		vector<int> M;
		
		int nc = 1;
		for (int i = 0; i < P; ++i)
		{
			nc *= 2;			
		}

		getline(infile, str);
		input = tokenize(str);
		for (int i = 0; i < nc; ++i)
		{
			M.push_back(P - atoi(input[i].c_str()));
		}

		vector<vector<int> > tickets;
		for (int i = 0; i < P; ++i)
		{
			vector<int> current;
			getline(infile, str);
			input = tokenize(str);
			nc /= 2;
			for (int j = 0; j < nc; ++j)
			{
				current.push_back(atoi(input[j].c_str()));
			}
			tickets.push_back(current);
		}
		
		for (int i = 0; i < P; ++i)
		{
			int minid;
			int cost = mincost(M, tickets, P, minid);
			res += cost;
			nc = M.size();
			if (minid >= nc / 2)
			{
				for (int j = 0; j < nc; ++j)
				{
					if (j < nc / 2)
						M[j]--;
					else
						M[j] = 0;
				}
			}
			else
			{
				for (int j = 0; j < nc; ++j)
				{
					if (j < nc / 2)
						M[j] = 0;
					else
						M[j]--;
				}
			}
		}		
						 		 	
		outfile << "Case #" << t + 1 << ": " << res << endl;		
	}

	infile.close();
	outfile.close();
} 


void gcj3()
{
	ifstream infile("E:\\input3.txt");
	ofstream outfile("E:\\output3.txt");
	int T;
	string str;
	getline(infile, str);
	T = atoi(str.c_str()); 	  
	 
	for (int t = 0; t < T; ++t)
	{	
		int res = 0;
		getline(infile, str);
		vector<string> input = tokenize(str);		 
		int R = atoi(input[0].c_str());

		vector<int> nwx, nwy, sex,sey;

		int ind[102][102];
		int ind2[102][102];
		
		for (int i = 0; i < 102; ++i)
		{
			for (int j = 0; j < 102; ++j)
			{
				ind[i][j] = 0;
				ind2[i][j] = 0;
			}
		}
		 
		for (int i = 0; i < R; ++i)
		{
			getline(infile, str);
		    input = tokenize(str);	
			int X1 = atoi(input[0].c_str());
			int Y1 = atoi(input[1].c_str());
			int X2 = atoi(input[2].c_str());
			int Y2 = atoi(input[3].c_str());
			nwx.push_back(X1);
			nwy.push_back(Y1);
			sex.push_back(X2);
			sey.push_back(Y2);

			for (int j = X1; j <= X2; ++j)
			{
				for (int k = Y1; k <= Y2; ++k)
				{
					ind[k][j] = 1;
				}
			}
			 

		}

		

		
		bool isstop = false;

		while(!isstop)
		{			
			for (int i = 1; i < 101; ++i)
			{
				for (int j = 1; j < 101; ++j)
				{
					ind2[i][j] = ind[i][j];
					if (ind[i][j] == 1)
					{
						if (ind[i - 1][j] == 0 && ind[i][j - 1] == 0)
							ind2[i][j] = 0;						 
					}
					else
					{
						if (ind[i - 1][j] == 1 && ind[i][j - 1] == 1)
							ind2[i][j] = 1;
					}
				}
			}

			isstop = true;
			for (int i = 1; i < 101; ++i)
			{
				for (int j = 1; j < 101; ++j)
				{
					if (ind2[i][j] == 1)
					{
						isstop = false;						
					}
					ind[i][j] = ind2[i][j];
				}
			}
			res++;
		}
						 		 	
		outfile << "Case #" << t + 1 << ": " << res << endl;		
	}

	infile.close();
	outfile.close();
} 

vector<string> tokenize(const string& str, const string& delimiters)
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