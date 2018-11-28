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

typedef __int64 LL;
#define I64d "%I64d"

double X[20],y[20],x[20],Y[20];

struct SS
{
	int id, r;
};

SS S[20];

bool cmpr(SS A, SS B)
{
	return A.r < B.r;
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);	freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);	freopen("B-small-attempt2.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);	freopen("B-small-attempt1.out","w",stdout);
//	freopen("B-large.in","r",stdin);			freopen("B-large.out","w",stdout);

	int T, ks;
	int N, W, L, i;
	int lasty, lastr, f;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{

		scanf("%d%d%d",&N,&L,&W);

		f = 0;
		if(W>L) 
		{
			f = 1;
			swap(L,W);
		}

		for(i=0;i<N;i++)
		{
			S[i].id = i;
			scanf("%d",&S[i].r);
		}

		sort(S,S+N,cmpr);

		x[N-1] = 0;
		y[N-1] = 0;
		lasty = 0;
		lastr = S[N-1].r;
		for(i=N-2;i>=0;i--)
		{
			x[i] = x[i+1] + S[i+1].r + S[i].r;
			y[i] = y[i+1];

			if(x[i]>L)
			{
				x[i] = 0;
				y[i] = lasty + lastr + S[i].r;
				lasty = y[i];
				lastr = S[i].r;
			}
		}

		for(i=0;i<N;i++)
		{
			X[S[i].id] = x[i];
			Y[S[i].id] = y[i];
		}

		printf("Case #%d:",ks);
		for(i=0;i<N;i++)
		{
			if(f) swap(X[i],Y[i]);
			printf(" %.1lf %.1lf",X[i],Y[i]);
		}
		printf("\n");
	}

	return 0;
}