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
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "C-small-attempt0(3)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}


bool can[20][20];
int mas[50][50];

int s[1<<16];
int dp[1<<16];
int n,k;


int check(int i,int j)
{
	for (int t=0;t<k;t++)
	{
		if (mas[i][t]==mas[j][t]) return 0;
		if (t)
		{
			if (mas[i][t-1]>mas[j][t-1] && mas[i][t]<mas[j][t])
				return 0;
			if (mas[i][t-1]<mas[j][t-1] && mas[i][t]>mas[j][t])
				return 0;
		}
	}
	return 1;
}


 int ocnt(int a)
 {
	int res=0;
	 while (a)
	{
		a=a & (a-1);
		res++;
	}
	return res; 
 }

int main()
{
	init();


	int tst;
	scanf("%d\n",&tst);
	for (int cas=1;cas<=tst;cas++)
	{
		memset(mas,0,sizeof(mas));
		scanf("%d%d\n",&n,&k);
		for (int i=0;i<n;i++)
		for (int j=0;j<k;j++)
			scanf("%d",&mas[i][j]);
		
		for (int i=0;i<n;i++)
		for (int j=i+1;j<n;j++)
			can[i][j]=can[j][i]=check(i,j);

		for (int i=0;i<1<<n;i++)
		{
			s[i]=1;
			for (int x=0;x<n;x++) if ((1<<x)&i)
			for (int y=x+1;y<n;y++) if ((1<<y)&i)
			{
				if (!can[x][y]) s[i]=0;
			}
		}

		dp[0]=0;
		for (int i=1;i<1<<n;i++)
		{
			if (s[i]) 
			{
				dp[i]=1;
				continue;
			}
			dp[i]=ocnt(i);
			int t=i;
			while (t)
			{
				t=(t-1)&i;
				int t2=i^t;
				int r = dp[t]+dp[t2];
				if (r<dp[i]) dp[i]=r;			
			}
		}

		printf("Case #%d: %d\n",cas,dp[(1<<n)-1]);
	}
  

   return 0; 
}
