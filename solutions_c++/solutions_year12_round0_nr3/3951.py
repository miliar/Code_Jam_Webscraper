/*===============================================================
*   Copyright (C) 2012 All rights reserved.
*   
*   file: c.cpp
*   author: ivapple
*   date: 2012-04-15
*   description: 
*
*   update log: 
*
================================================================*/
#include <cstdlib>
#include <cstdio>
#include <cmath>

#include <iostream>
#include <fstream>
#include <map>

#define out(x) (cout<<#x<<": "<<x<<endl)

#define FOR(i,s,t) for(i=s; i<t; i++)

using namespace std;

template<class T>void show(T a, int n){int i; for(i=0;i<n;i++)cout<<a[i]<<" ";cout<<endl;}

template<class T>void show(T a, int r, int l){int i; for(i=0;i<r;i++)show(a[i],l);cout<<endl;}

int T;
int A, B;
int factor[10]={0,1,10,100,1000,10000,100000,1000000,10000000};

	ifstream fin("cbig.txt");
	//ifstream fin("test.txt");
	ofstream fout("c.txt");
int solve(int num)
{
	int digit;
	int digit2;
	digit = log10(num)+1;
	if (digit == 1)
		return 0;
	int mov = 0;
	int high, low;
	int cycle,dif;
	int re = 0;
	cycle = num;
	map<int, bool> state;
	while (mov<digit-1)
	{
		high = cycle/factor[digit];
		low = cycle%factor[digit];
		cycle = low*10 + high;
		mov = mov+1;
		digit2 = log10(cycle)+1;
		dif = digit - digit2;
		cycle = cycle*factor[dif+1];
		mov = mov+dif;
		if (cycle < num && cycle >=A)
		{
			if (state.find(cycle) == state.end())
			{
	//	    fout << num << " " << cycle << endl;
			re = re+1;
			state[cycle]=true;
			}
//		out(re);
		}
	}
	//out(re);
	return re;
}

int main()
{
	fin >> T;
	int i, j;
	int result;
	FOR(i,0,T)
	{
		result = 0;
		fin >> A >> B;
		FOR(j,A+1,B+1)
		{
		//	out(solve(j));
		result += solve(j);
			//out(result);
		}
		fout << "Case #" << i+1 <<": " << result << endl;
	}
	return 0;
}
