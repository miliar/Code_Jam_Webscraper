#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <string.h>
#include <algorithm>

using namespace std;

typedef long long i64;
typedef pair<int,int> pii;

pii aa[1000500];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t,n,s,p;
	cin >> t;
	int mn[150];
	int mx[150];
	int cur;
	for (int ct=1;ct<=t;ct++)
	{
		int res=0;
		scanf("%d%d%d",&n,&s,&p);
		for (int i=0;i<n;i++)
		{		
			scanf("%d",&cur);
			mn[i]=cur/3;
			if (cur%3) mx[i]=mn[i]+1;
			else mx[i]=mn[i];
			if (mx[i]>=p) res++;
			else
				if (mx[i]==p-1 && mx[i]>0 && (cur%3==2 || cur%3==0) && s)
				{
					res++;
					s--;
				}
		}
		printf("Case #%d: %d\n",ct,res);
	}
	return 0;
}