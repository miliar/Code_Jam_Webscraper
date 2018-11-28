#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;
ifstream inf;
ofstream outf;
#define FOR(i,a,b) for(int _b=(b),i=(a);i<=_b;i++)
#define FORD(i,a,b) for(int _b=(b),i=(a);i>=_b;i--)


vector <vector<int > >m;
int n;
int good(int l,int  from)
{
	//int fl = 0;
	for (int i = from + 1;i < n; i++)
		if (m[l][i] == 1) return 0;
	return 1;
}
int main(void){
	//freopen("input.txt","rt",stdin);
	//freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	int tests;
	inf >> tests;
	long long p[100];
	p[0] = 1;
	for(int i = 1; i < 40; i++)
		p[i] = p[i-1] * 2;
 	for(int test = 0; test < tests; test++)
	{		
		long long n, k;
		inf >> n >>  k;
		long long z = k % (p[n]);

		outf << "Case #"  << test+1 << ": " ;
		if (z != p[n] - 1 )
			outf <<  "OFF" << endl;
		else 
			outf <<  "ON" << endl;
		
	}
	
	outf.close();
	return 0;
}
