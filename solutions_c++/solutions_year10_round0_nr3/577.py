#pragma warning(disable:4786)
#include<math.h>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<utility>
#include<algorithm>
#include<string.h>
#include<stdio.h>
#include<set>
#include<stdlib.h>
#include<sstream>
#include<functional>
#include<queue>
#include<stack>
using namespace std;

#define MAX(A,B) ((A)>(B)?(A):(B))
#define MIN(A,B) ((A)<(B)?(A):(B))
#define ABS(A) ((A)>0?(A):(-(A)))
#define S(X) ((X)*(X))

typedef pair<int,int> PII;

//int dr[]={-1,0,1,0};
//int dc[]={0,1,0,-1};
//int dr[]={-2,-2,-1,1,2,2,1,-1};
//int dc[]={-1,1,2,2,1,-1,-2,-2};

typedef __int64 LL;
#define I64d "%I64d"

LL income[1002],g[1002];
int flag[1002];

int main()
{
//	freopen("c-small-attempt0.in","r",stdin);
//	freopen("c-small-attempt0.out","w",stdout);

	freopen("c-large.in","r",stdin);
	freopen("c-large.out","w",stdout);

	int T, ks, N, round, i, now;
	LL R, K, sum, here, ans, c, L, X;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		printf("Case #%d: ",ks);
		scanf("%I64d%I64d%d",&R,&K,&N);
		for(i=0;i<N;i++) {scanf("%I64d",&g[i]); flag[i]=0;}

		now = 0;
		for(round = 1; round <= R; round++)
		{
			flag[now] = round;

			sum=0;
			for(i=0;i<N;i++)
			{
				here = g[(i+now)%N];

				if(sum + here > K) break;

				sum+=here;
			}

			income[round] = sum;
			income[round] += income[round-1];

			now = (now + i)%N;

			if(flag[now])
				break;
		}

		if(round>=R) 
			ans = income[R];
		else
		{
			c = flag[now];
			L = round+1 - c;
			X = R-round;

			ans = income[round] + X/L*(income[round] - income[ c-1 ]);
			if(X%L) ans+= income[c-1+X%L] - income[c-1];
		}

		printf("%I64d\n",ans);
	}

	return 0;
}