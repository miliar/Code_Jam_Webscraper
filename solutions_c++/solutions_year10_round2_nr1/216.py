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
 
vector<string> tokenize(const string& str, const string& delimiters = " ");
void gcj1();
void gcj2(); 
void gcj3();


int _tmain(int argc, _TCHAR* argv[])
{ 	 
	gcj1();	
    return 0;
} 

 

//Google code jam 
void gcj1()
{
	ifstream infile("E:\\input1.txt");
	ofstream outfile("E:\\output1.txt");
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

		vector<vector<string> > current;
		vector<vector<string> > tocreate;

		for (int i = 0; i < N; ++i)
		{
			getline(infile, str);
			input = tokenize(str, "/");	
			current.push_back(input);					
		}

		for (int i = 0; i < M; ++i)
		{
			getline(infile, str);
			input = tokenize(str, "/");	
			tocreate.push_back(input);					
		}

		for (int i = 0; i < M; ++i)
		{
			vector<string> str = tocreate[i];
			//string tmp;
			int pos = 0;
			for (int j = 0; j < current.size(); ++j)
			{
				vector<string> str2 = current[j];
				int tmp = 0;
				for (int k = 0; k < min(str.size(), str2.size()); ++k)
				{
					if (str[k] != str2[k])
					{
						tmp = k;
						break;
					}
					else
					{
						tmp = k + 1;
					}
				}			
				
				pos = max(tmp, pos);				 
				if (pos == str.size())
				{
					break;					
				}
			}

			if (pos != str.size())
			{
				res += str.size() - pos;				 
				current.push_back(str);
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
		int res;

		getline(infile, str);		
		int n = atoi(str.c_str());

		
				
						 		 	
		outfile << "Case #" << t + 1 << ": " << res << endl;		
	}

	infile.close();
	outfile.close();
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
		string res;

		getline(infile, str);
		vector<string> input = tokenize(str);		 

		int N = atoi(input[0].c_str());
		int K = atoi(input[1].c_str());	 
		int B = atoi(input[2].c_str());	
		int time = atoi(input[3].c_str());	
		
		vector<int> location, speed;
		vector<bool> isintime;

		getline(infile, str);
		input = tokenize(str);	

		for (int i = 0; i < N; ++i)
			location.push_back(atoi(input[i].c_str()));

		getline(infile, str);
		input = tokenize(str);	

		for (int i = 0; i < N; ++i)
			speed.push_back(atoi(input[i].c_str()));

		int cnt = 0;
		for (int i = 0; i < N; ++i)
		{
			if ((B - location[i]) > time * speed[i])
			{
				isintime.push_back(false);
			}
			else
			{
				isintime.push_back(true);
				cnt++;
			}
		}

		if (cnt < K)
		{
			res = "IMPOSSIBLE";
		}
		else
		{
			int tmp = 0;
			int cnt = 0;
			for (int i = N - 1; i >= 0; --i)
			{
				if (isintime[i])
				{
					cnt++;
					if (cnt == K)
						break;
				}
				else
				{
					tmp += (K - cnt);
					//tmp++;
				}
			}
			ostringstream os;
			os << tmp;			
			res = os.str();
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