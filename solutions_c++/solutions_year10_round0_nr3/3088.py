/* This is my Google Code Jam 2010.
 *
 * All code in this file was written by me, unless otherwise noted. I hereby
 * grant permission to copy, modify and reuse my code for any purpose.
 *  
 * Walaa Usama [BlackCode23]  <walaa_23@msn.com>   May 2010
 */

#include "stdafx.h"
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <string>
#include <cmath>
#define rep(i,m) for(int i=0;i<m;i++)
#define rep2(i,x,m) for(int i=x;i<m;i++)
const double PI = 2*acos(0.0);
using namespace std;

//Public Declarations
int cases;
long r, k, n, g;
vector<long> G;
long cash;

void Solve(int caseNum)
{
	cash = 0;
	rep(i, r)
	{
		int max = 0, count = -1;
		rep(j, n)
		{
			if((max + G[j]) > k)
			{
				break;
			}
			else
			{
				count = j;
				max +=G[j];
			}
		}
		cash += max;
		for(int k=0; k<=count; k++)
		{
			G.push_back(G[k]);
		}
		G.erase(G.begin(), G.begin()+count+1);
	}
	printf("Case #%d: %d\n", caseNum, cash);
}
void ReadInputs()
{
	freopen( "A-small.out" , "w" , stdout );
    freopen( "A-small.in" , "r" , stdin );
	scanf( "%d" ,&cases);
	rep(i, cases)
	{
		scanf( "\n%d%d%d\n" , &r, &k, &n);
		G.clear();
		rep(j, n)
		{
			scanf( "%d" , &g);
			G.push_back(g);
		}
		Solve(i);
	}
}
int main()
{
	ReadInputs();
    return 0;
}


