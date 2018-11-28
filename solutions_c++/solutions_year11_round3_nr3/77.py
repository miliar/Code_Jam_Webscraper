#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
#include <algorithm>
#include <map>
#include <stack>
#include <vector>
#include <stdlib.h>
#include <cmath>
#include <fstream>
using namespace std;
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define INF 0x7f7f7f7f
#define INFL (1LL<<60)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
int num[20000];
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	scanf("%d",&T);
	int cas = 0;
	while(T--)
	{
		int N,L,H;
		scanf("%d%d%d",&N,&L,&H);
		for(int i=0;i<N;i++)
			scanf("%d",&num[i]);
		printf("Case #%d: ",++cas);
		bool flag = true;
		for(int i=L;i<=H;i++)
		{
			flag = true;
			for(int j=0;j<N;j++)
			{
				int a = max(i,num[j]);
				int b = min(i,num[j]);
				if(a%b!=0)
				{
					flag = false;
					break;
				}
			}
			if(flag)
			{
				printf("%d\n",i);
				break;
			}
		}
		if(!flag)printf("NO\n");
	}
    return 0;
}
