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
	

int main(void){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	//for (int pd = 0; pd <= 100; pd++)
		//for(int pn = 0; pn <= 100; pn++)
	int dp[1000];
	for (int  i = 0; i <= 100; i++)
		dp[i] = 10000000;
	int k = 0;
	for (long n = 1; n < 10000; n++)	
			for (long pd = 0; pd <= 100; pd++)
			{
				if ((n*pd) % 100 != 0)
					continue;
				if (dp[pd] > n)
				{
					dp[pd] = n;
					k++;
					//cout << pd << "  " << dp[pd] << endl;
				}								
			}

	//cout << dp[50];


		

		
	int tests;
	inf >> tests;
	for (int test = 0; test < tests; test++)
	{		
		outf << "Case #" << test+1 << ": ";
		long long  n,pd,pn;
		inf >> n >> pd >> pn;
		if ((pd == 0 && pn == 0 ) || (pd == 100 && pn == 100)   ||  (dp[pd] <= n && pn!=0 && pn!=100) ) 
		{
			outf << "Possible" << endl;
			continue;
		}
		else
		{
			outf << "Broken" << endl;
			continue;
		}


		

		
		
	}

	outf.close();
	return 0;
}
