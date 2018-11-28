#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
#define   max(a,b)    ((a)>(b)?(a):(b))
#define   min(a,b)    ((a)<(b)?(a):(b))
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(i=(a);i<(b);i++)
#define   REP(i,n)     rep(i,0,n)
#define   inf         1000000000
FILE *fin;
FILE *fout;
int N;
int S;
int Q;
string engine[110];
string query[1010];
//int engno[110];
int queryno[1010];
int dp[1010][110];
int main()
{
   	fin=fopen("A-large.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
    fscanf(fin,"%d\n",&N);
    int round=1;
	for (round=1;round<=N;round++)
	{
        fscanf(fin,"%d\n",&S);
		for (i=1;i<=S;i++)
		{
		    char c;
			char  t[1000];
			int tcnt=0;
			while (fscanf(fin,"%c",&c)&&c!='\n')
			{
                t[tcnt++]=c;
			}
			t[tcnt++]='\0';
			engine[i]=string(t);
		}
		fscanf(fin,"%d\n",&Q);
		for (i=1;i<=Q;i++)
		{
            char c;
			char  t[1000];
			int tcnt=0;
			while (fscanf(fin,"%c",&c)&&c!='\n')
			{
                t[tcnt++]=c;
			}
			t[tcnt++]='\0';
			query[i]=string(t);
			for (j=1;j<=S;j++)
			{
				if (engine[j]==query[i])
				{
					queryno[i]=j;
				}
			}
		}
        for (i=0;i<1010;i++)
        {
			for (j=0;j<110;j++)
			{
				dp[i][j]=inf;
			}
        }
        for (i=1;i<=S;i++)
        {
			dp[0][i]=0;
        }
        for (i=1;i<=Q;i++)
        {
			for (j=1;j<=S;j++)
			{
				if (query[i]==engine[j])
				{
					dp[i][j]=inf;
					continue;
				}
                if (query[i]!=engine[j])
                {
					dp[i][j]=min(dp[i-1][j],dp[i-1][queryno[i]]+1);
					for (k=1;k<=S;k++)
					{
						if(k!=j)
							dp[i][j]=min(dp[i][j],dp[i-1][k]+1);
					}
				//	dp[i][j]=min(dp[i-1][j],dp[i-1][queryno[i]]+1);
				
                }
			}
        }
		int ret=inf;
        for (i=1;i<=S;i++)
        {
			ret=min(ret,dp[Q][i]);
        }
		printf("Case #%d: %d\n",round,ret);
		fprintf(fout,"Case #%d: %d\n",round,ret);
	}
}