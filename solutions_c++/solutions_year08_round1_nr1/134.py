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
	
	ofstream fout("aout.txt");
	ifstream fin("ain.txt");
	fin >> T;
	while(ctest++ < T)
	{
		int N;
		fin >> N;
		vi x(N,0), y(N,0);
		for(int i = 0; i < N; i++) fin >> x[i];
		for(int j = 0; j < N; j++) fin >> y[j];

		sort(x.begin(),x.end());
		sort(y.begin(),y.end());
		reverse(y.begin(), y.end());

		long long total = 0;
		for(int i = 0; i < N; i++) total += x[i]*y[i];

		fout << "Case #" << ctest << ": " << total << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
		