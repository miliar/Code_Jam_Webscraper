#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "A-large";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
 	freopen((problem_name+".out").c_str(),"wt",stdout);
}


int i,j,k;

int dp[1005][105];
string s[110],q[1100];



int main()
{
	init();

	int n;
	scanf("%d\n",&n);

	for (int tt=1;tt<=n;tt++)
	{
		memset(dp,1,sizeof(dp));
		int ns,nq;		
		char ss[500];
		scanf("%d\n",&ns);
		for (i=0;i<ns;i++)
		{
			gets(ss);
			s[i]=ss;
		}
		scanf("%d\n",&nq);
		for (i=0;i<nq;i++)
		{
			gets(ss);
			q[i]=ss;
		}	
		for (i=0;i<=ns;i++) dp[0][i]=0;
		for (i=0;i<nq;i++)
		{
			for (j=0;j<ns;j++)
			{
				if (q[i]==s[j])
				{
					for (k=0;k<ns;k++) if (k!=j) dp[i+1][k]=min(dp[i+1][k],dp[i][j]+1);
				} else
				{
					dp[i+1][j]=min(dp[i+1][j],dp[i][j]);
					for (k=0;k<ns;k++) if (k!=j) dp[i+1][k]=min(dp[i+1][k],dp[i][j]+1);				
				}
			}		
		}
		int res=10000000;
		for (i=0;i<ns;i++) res=min(res,dp[nq][i]);		
		printf("Case #%d: %d\n",tt,res);
	
	}



		

	return 0;
}
