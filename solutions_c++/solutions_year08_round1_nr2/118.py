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

int main()
{
	int T, ctest = 0;
	
	ofstream fout("cout.txt");
	ifstream fin("cin.txt");
	fin >> T;
	while(ctest++ < T)
	{
		int N = 10, M = 10;
		fin >> N >> M;
		vector< vector<int> > prefs(M,vector<int>());
		vector<int> with(M,-1);

		for(int i = 0; i < M; i++)
		{
			int C;
			fin >> C;
			int shake, yes;
			with[i] = -1;
			for(int j = 0; j < C; j++)
			{
				fin >> shake >> yes;
				shake--;
				if(yes == 0) prefs[i].push_back(shake);
				else with[i] = shake;
			}
		}
		vector<int> malted(N,0);
		int IMP = 0;

		while(true)
		{
			int change = 0;
			for(int i = 0; i < M; i++)
			{
				
				if(with[i] != -1 && malted[with[i]]) continue;
				
				int has = 0;
				for(int j = 0; j < prefs[i].size(); j++)
				{
					if(malted[prefs[i][j]]) continue;
					else { has++; break; }
				}
				if(has == 0)
				{
					if(with[i] == -1) { IMP = 1; break; }
					else 
					{
						malted[with[i]]++;
						change++;
						break;
					}
				}
			}
			if(IMP == 1) break;
			if(change == 0) break;
			
		}
		if(IMP == 1)
		{
			fout << "Case #" << ctest << ": IMPOSSIBLE" << endl;
		}
		else
		{
			fout << "Case #" << ctest << ":";
			for(int i = 0; i < N; i++) fout << " " << malted[i];
			fout << endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}
		