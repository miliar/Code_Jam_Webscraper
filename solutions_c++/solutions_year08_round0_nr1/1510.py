#include "stdafx.h"
#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <stack>
#include <cmath>
#include <queue>
#include <istream>
#include <sstream>
#include <set>
using namespace std;
 
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl; 

vs strsp(string c, string delim=" ")
{
	vs ret;
	string a = "";
	int p = 0;
	while(p < c.size())
	{
		while(p < c.size() && delim.find(c[p]) == string::npos ) { a += c[p++]; }
		if(a.size()) { ret.push_back(a); a = ""; }
	}
	return ret;
}	

int queers[1050];
int S, Q;
int dp[105][1050];

int rec(int engine, int bq)
{
	if(bq == Q) return 0;
	int & ret = dp[engine][bq];
	if(ret != -1) return ret;
	
	if(queers[bq] != engine) return ret = rec(engine,bq+1);
	ret = 100000;
	for(int i = 0; i < S; i++)
	{
		if(i== engine) continue;
		ret = min(ret, 1+rec(i,bq+1));
	}
	return ret;
}


int main()
{
	int T, ctest = 0;
	
	
	ofstream fout("aout.txt");
	ifstream fin("ain.txt");
	fin >> T;
	while(ctest++ < T)
	{
		S = 0;
		fin >> S;	
		deb(S);
		memset(queers,0,sizeof(queers));
		vs names;
		char clear = ' ';
		fin >> noskipws >> clear;

		for(int i = 0; i < S; i++)
		{	
			string buff = "";
			while(true)
			{
				char next = ' ';
				fin >> noskipws >> next;
				if(next == '\n') break;
				else buff += next;
			}
			//cout << buff << endl;
			names.push_back((string)buff);
		}
		fin >> Q;
		fin >> noskipws >> clear;
		
		if(Q == 0)  
		{ 
			fout << "Case #" << ctest << ": 0" << "\n"; 
			continue; 
		}

		for(int i = 0; i < Q; i++)
		{
			string buff = "";
			while(true)
			{
				char next = ' ';
				fin >> noskipws >> next;
				if(next == '\n'  || next == '\0') break;
				else buff += next;
			}

			for(int j = 0; j < S; j++)
			{
				if(buff == names[j]) { queers[i] = j; break; }
			}
		}

		memset(dp,-1,sizeof(dp));
		int best = 1000000;
		for(int i = 0; i < S; i++) 
		{ 
			if(i==queers[0]) continue; 
			best = min(best,rec(i,1)); 
		}

		fout << "Case #" << ctest << ": " << best << "\n";
	}
	fout.close();
	return 0;
}
		