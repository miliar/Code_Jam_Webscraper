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
long long gcd(long long a, long long b)
{
	if (a == 0)
		return b;
	return gcd(b % a, a);

}
int main(void){
	//freopen("input.txt","rt",stdin);
	//freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	int tests;
	inf >> tests;
	for(int test = 0; test < tests; test++)
	{		
		long long r, k, n, anw;
		long long g[2000], price[2000], nextt[2000];
		inf >> n;
		for(int i = 0; i < n; i++) 
			inf >> g[i];
		long long nd = abs(g[1] - g[0]);
		for (int i = 2; i < n; i++) 
			nd = gcd(nd, abs(g[i] - g[0]));

		if (nd !=1 )
		{
			long long r = g[0] % nd;
			long long rev = nd - r;
			while(rev >= nd) rev -= nd;
			nd = rev;
		}
		else
			nd = 0;
		outf << "Case #"  << test+1 << ": " << nd << endl ;
	}
	//outf << gcd(3, 2);
	
	outf.close();
	return 0;
}
