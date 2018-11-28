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



long long dp [2200][15][15];
long long m[2200];
long long pr[15][2200];
int main(void){
	
	//freopen("input.txt","rt",stdin);
	//freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	int tests;
	inf >> tests;
	int p2[15];
	int imp = 200000000;
	for(int i = 0; i < 14; i++)
		p2[i] = 1 << i;
 	for(int test = 0; test < tests; test++)
	{
		long long  anw = 0;
		int p;
		inf >> p;
		for(int i = 0; i < p2[p];i++)
			inf >> m[i];
		for (int l = 1; l <= p; l++)
			for(int i = 0; i < p2[p - l] ;i++)
				inf >> pr[l][i];
		// l = 0
		for(int i = 0; i < p2[p];i++)
		{
			for(int l = 0; l < 13; l++)
				dp[i][0][l] = imp;
			for(int l = 0; l <= m[i]; l++)
				dp[i][0][l] = 0;
		}
		for(int le = 1; le <= p; le++)
		{
			for(int i = 0; i < p2[p - le];i++)
			{
					for(int l = 0; l < 12; l++)
					{
						//if(le == 1 && i ==1)
						//	outf << 1;
						// pokupayu
						dp[i][le][l] = pr[le][i] + dp[i * 2][le - 1][l]+ dp[i * 2 + 1][le - 1][l];

						long long ne = imp;
						if(l < 11) 
							ne = dp[i * 2][le - 1][l + 1]+ dp[i * 2 + 1][le - 1][l + 1];
						dp[i][le][l] = min(dp[i][le][l], ne);
					}

			}

		}

		anw = dp[0][p][0];
		//for(int i = 0; i < 11; i++)
		//	anw = min(anw,  dp[0][p][i]);
		



		outf << "Case #"  << test+1 << ": " ;
		outf <<  anw << endl;
		
	}
	
	outf.close();
	return 0;
}
