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




			int d, ins, m, n;
			int dd[1000];
			int gdd(int x)
			{
				if (dd[x] != -1)
					return dd[x];
				if (x <= m)
					return 0;
				int res = gdd(x - 1) + 1;
				int b = 1000000;
				if ( m > 0)
					b = gdd(x - m) + ins;
				if (res > b)
					res = b;
				dd[x] = res;
				return res;
			}
int distance(int a,int  b) // a,b nelzya menyat!!!
{
	return
		(gdd(abs(a - b)));
	if (a == b)
		return 0;
	int ne = abs(a - b);
	int res = 1000000; // nelzya
	if( m > 0 )
				{
					int cnt = 0;// skolko figovin dobavili sprava
					while (ne > m)
					{
						ne -= m;
						cnt++;
					}
					//cnt += 1;
					ne = cnt * ins;
					if (ne < res)
						res = ne;
				}
	return res;
}
int main(void){
	//freopen("input.txt","rt",stdin);
	//freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	int tests;
	inf >> tests;
	int dp[102][259];
	int a[222];
	int imp = 100000000;
 	for(int test = 0; test < tests; test++)
	{
			for (int i = 0; i < 500; i++)
				dd[i] = -1;
			inf >> d >> ins >> m >> n;
			//vector <int> a = vector<int>(n);
			for (int i = 0; i < n; i++)
				inf >> a[i];
			for (int i = 0; i < 256; i++) 
				dp[1][i] = min (abs(i - a[0]), d);
			for (int i = 0; i < 256; i++)
			{	
				int ne = distance(i, a[0]);
				dp[1][i] = min(dp[1][i], ne);

			}
			for(int k = 2; k <= n; k++)
			{
				for(int r = 0; r < 256; r++)
				{
					dp[k][r] = 1000000;
					dp[k][r] = min (dp[k][r], dp[k - 1][r] + d);
					for (int z = 0; z < 256; z++) // tut bred
						dp[k][r] = min (dp[k][r], dp[k - 1][z] +  abs(z - a[k - 1]) +  distance(z, r) );
				}
					
						// udalili

				
						//end
						/*if (dp[k][r] == 0)
							k = 200;*/

					
				// dp[k-1] - ready lets do next

			}
			int anw = (n - 1) * d;
			for(int i = 0; i < 256; i++)
				anw = min(anw, dp[n][i]);

			

				
			outf << "Case #"  << test+1 << ": " ;
			outf <<  anw << endl;
		
	}
	
	outf.close();
	return 0;
}
