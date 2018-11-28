const double pi=3.1415926535897932, e=2.7182818284590452;
#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/stack:16000000")
#include <cstdio>
#include <cmath>
#include <complex>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

int N,M,V;
int val[1000000],ch[1000000],res[1000000][20];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d",&N);
	for (int ii=1; ii<=N; ++ii)
	{
		scanf("%d%d",&M,&V);
		for (int i=0; i<M; ++i)
			if (i<(M-1)/2)
				scanf("%d%d",&val[i],&ch[i]);
			else
				scanf("%d",&val[i]),
				res[i][val[i]]=0,
				res[i][1-val[i]]=1000000,
				ch[i]=0;
		for (int i=(M-1)/2-1; i>=0; --i)
		{
			int ror[20],rand[20];
			res[i][0]=res[i][1]=ror[0]=ror[1]=rand[0]=rand[1]=1000000;
			for (int i1=0; i1<2; ++i1)
				for (int i2=0; i2<2; ++i2)
					ror[i1|i2] = min(ror[i1|i2], res[i*2+2][i1]+res[i*2+1][i2]),
					rand[i1&i2] = min(rand[i1&i2], res[i*2+2][i1]+res[i*2+1][i2]);
			if (ch[i]==1)
			{
				if (val[i]!=1)
				res[i][0]=min(res[i][0], rand[0]+1),
				res[i][1]=min(res[i][1], rand[1]+1);
			else
				res[i][0]=min(res[i][0], ror[0]+1),
				res[i][1]=min(res[i][1], ror[1]+1);
			}
			if (val[i]==1)
				res[i][0]=min(res[i][0], rand[0]),
				res[i][1]=min(res[i][1], rand[1]);
			else
				res[i][0]=min(res[i][0], ror[0]),
				res[i][1]=min(res[i][1], ror[1]);
		}
		if (res[0][V]==1000000)
			printf("Case #%d: IMPOSSIBLE\n", ii);
		else
			printf("Case #%d: %d\n", ii, res[0][V]);
	}
	return 0;
}
