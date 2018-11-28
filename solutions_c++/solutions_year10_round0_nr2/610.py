// SRM.cpp : Defines the entry point for the console application.
//
#pragma once
#include "stdafx.h" 

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
void gcj22();
void gcj3();

string strdiff(string a, string b);

bool lessthan(string str1, string str2);
 
int _tmain(int argc, _TCHAR* argv[])
{ 	
	gcj2();

	 
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

int gcd(int a, int b)
{
	a = a > 0 ? a : - a;
	b = b > 0 ? b : - b;

	if (a > b)
		return gcd(b, a);

	if (a == 0)
		return b;

	return gcd(b % a, a);
} 

string strdiff(string a, string b)
{
	if (lessthan(a, b))
		return '-' + strdiff(b, a);	

    deque<char> tmp;
	int isb = false;
	b.insert(0, a.size() - b.size(), '0');

	for (int i = b.size() - 1; i >= 0; --i)
	{
		int u = a[i] - '0';
		int v = b[i] - '0';
		if (isb)
		{
			v = v + 1;
		}
		if (u < v)
		{
			isb = true;
			tmp.push_front(10 + u - v + '0');
		}
		else
		{
			isb = false;
			tmp.push_front(u - v + '0');
		}
	}	

	while (!tmp.empty() && (tmp.front() == '0'))
		tmp.pop_front();

	string res(tmp.begin(), tmp.end());	

	return res;		
}

string strdiv(string a, string b)
{
	return "";
}

string strmul(string a, string b)
{
	return "";
}

string strmod(string a, string b)
{
	return strdiff(a, strmul(strdiv(a, b), b));
}


string gcd(string a, string b)
{	 
	if (lessthan(b, a))
		return gcd(b, a);

	if (a == "")
		return b;

	return gcd(strmod(b, a), a);
} 
	
int gcd(vector<int> seq)
{
	int res = 0;

	for (size_t i = 0; i < seq.size(); i++)
	{
		res = gcd(res, seq[i]);
	}

	return res;
}


string gcd(vector<string> seq)
{
	string res = seq[0];

	for (size_t i = 0; i < seq.size(); i++)
	{
		res = gcd(res, seq[i]);
	}

	return res;
}

void gcj1()
{
	ifstream infile("E:\\input1.txt");
	ofstream outfile("E:\\output1.txt");
	int T;
	string str;
	getline(infile, str);
	T = atoi(str.c_str()); 

	int f[31];

	f[0] = 0;

	for (int i = 1; i < 31; ++i)
	{
		f[i] = 2 * f[i - 1] + 1;
	}
	 
	for (int t = 0; t < T; ++t)
	{	
		string res;

		getline(infile, str);
		vector<string> input = tokenize(str);

		int N = atoi(input[0].c_str());
		int K = atoi(input[1].c_str());

		int pos = f[N];
		K = K % (pos + 1);

		if (K == pos)
			res = "ON";
		else
			res = "OFF";		

						 		 	
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
		long long res;

		getline(infile, str);
		vector<string> input = tokenize(str);	

		int N = atoi(input[0].c_str());
		vector<int> times;
		for (int i = 0; i < N; ++i)
		{
			times.push_back(atoi(input[i + 1].c_str()));
		}

		sort(times.begin(), times.end());

		int m = times[0]; 

		vector<int> diff;
		for (int i = 0; i < N; ++i)
		{
			if (times[i] != m)
				diff.push_back(times[i] - m);
		}

		int g = gcd(diff);
		
		if (m % g == 0)
		{
			res = 0;
		}
		else
		{
			res = (m / g + 1) * g - m;			
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
		getline(infile, str);
		vector<string> input = tokenize(str);		

		int R = atoi(input[0].c_str());
		int k = atoi(input[1].c_str());
		int N = atoi(input[2].c_str());

		vector<long long> gsize;
        getline(infile, str);
		input = tokenize(str);	

		for (int n = 0; n < N; ++n)
		{
			long long tmp = atol(input[n].c_str());			
			if (tmp <= k)			
				gsize.push_back(tmp);

		}

		long long res = 0;

		if (R <= (N + 1))
		{
			int cpos = 0;
			int tmp = 0;
			long long csize = 0;
			for (int i = 0; i < R; ++i)
			{			
				tmp = cpos;
				do
				{
					csize = csize + gsize[tmp];
					tmp = (tmp + 1) % N;					
				}
				while (((csize + gsize[tmp]) <= k) && (tmp != cpos));
				res = res + csize;
				csize = 0;
				cpos = tmp;
			}
		}
		else
		{
			int cpos = 0;
			int tmp = 0;
			long long csize = 0;
			for (int i = 0; i < (N + 1); ++i)
			{			
				tmp = cpos;
				do
				{
					csize = csize + gsize[tmp];
					tmp = (tmp + 1) % N;					
				}
				while (((csize + gsize[tmp]) <= k) && (tmp != cpos));
				res = res + csize;
				csize = 0;
				cpos = tmp;
			}
			R = R - N - 1;

			int spos = cpos;
			tmp = cpos;
			int period = 0;
			long long pres = 0;
			csize = 0;
			for (int i = 0; i < (N + 1); ++i)
			{
				tmp = cpos;
				do
				{
					csize = csize + gsize[tmp];
					tmp = (tmp + 1) % N;					
				}				
				while (((csize + gsize[tmp]) <= k) && (tmp != cpos));
				pres = pres + csize;
				if (spos == tmp)
				{
					period = i + 1;
					break;
				}			
				cpos = tmp;
				csize = 0;
			}

			int times = R / period;
			res = res + pres * times;
			R = R % period;

			cpos = spos;
			tmp = cpos;
			csize = 0;
			for (int i = 0; i < R; ++i)
			{			
				tmp = cpos;
				do
				{
					csize = csize + gsize[tmp];
					tmp = (tmp + 1) % N;					
				}
				while (((csize + gsize[tmp]) <= k) && (tmp != cpos));
				res = res + csize;
				csize = 0;
				cpos = tmp;
			}

		}		
						 		 	
		outfile << "Case #" << t + 1 << ": " << res << endl;		
	}

	infile.close();
	outfile.close();
}

bool lessthan(string str1, string str2)
{
	if (str1.size() > str2.size())
		return false;

	if (str1.size() < str2.size())
		return true;
	
	return str1 < str2;
	
}

void gcj22()
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
		vector<string> times;
		for (int i = 0; i < N; ++i)
		{
			times.push_back((input[i + 1].c_str()));
		}

		sort(times.begin(), times.end(), lessthan);

		string m = times[0]; 

		vector<string> diff;
		for (int i = 0; i < N; ++i)
		{
			if (times[i] != m)
				diff.push_back(strdiff(times[i], m));
		}

		string g = gcd(diff);
		string r = strmod(m, g);
		res = strmod(strdiff(g, r), g);			
		 

		outfile << "Case #" << t + 1 << ": " << res << endl;		
	}

	infile.close();
	outfile.close();
}
 