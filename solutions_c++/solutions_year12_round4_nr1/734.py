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

LL r[10004], d[10004], l[10004];
int main()
{
//	freopen("A-small-attempt0.in","r",stdin);	freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);	freopen("A-small-attempt1.out","w",stdout);
	freopen("A-large.in","r",stdin);			freopen("A-large.out","w",stdout);

	int T, ks;
	int N;
	int f,i,j;
	LL target;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		printf("Case #%d: ",ks);

		scanf("%d",&N);
		for(i=0;i<N;i++)
		{
			scanf("%I64d%I64d",&d[i],&l[i]);
			r[i] = 0;
		}
		scanf("%I64d",&target);

		r[0] = d[0];
		f = 0;
		for(i=0;i<N;i++)
		{
			if(d[i]+r[i]>=target) f = 1;
			for(j=i+1;j<N;j++)
			{
				if(d[j]-d[i]>r[i]) break;

				r[j] = MAX(r[j], MIN(d[j]-d[i],l[j]));
			}
		}

		if(f) printf("YES\n");
		else printf("NO\n");
		
	}

	return 0;
}