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
	for(int test = 0; test < tests; test++)
	{		
		long long r, k, n;
		long long g[2000], price[2000], nextt[2000];
		inf >> r >> k >> n;
		for(int i = 0; i < n; i++) 
			inf >> g[i];
		for(int i = 0; i < n; i++)
		{
			// posadka begins from i
			long long onRoad = 0;
			int j = i;
			nextt[i] = i;
			
			while(j != i + n)
			{
				int nxt = j % n;
				if (onRoad + g[nxt] <= k)
					onRoad += g[nxt];
				else
				{	
					nextt[i] = nxt;
					break;
				}
				j++;
			}
			price[i] = onRoad;
			
		}
		//price nextt done
		long long anw = 0;
		int crt = 0;
		for(int i = 0; i < r; i++)
		{
			anw += price[crt];
			crt = nextt[crt];

		}
		outf << "Case #"  << test+1 << ": " << anw << endl ;
	}
	
	outf.close();
	return 0;
}
