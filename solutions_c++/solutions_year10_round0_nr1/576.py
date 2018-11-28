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

int main()
{
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.out","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int ks, T, n, k;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d%d",&n,&k);

		printf("Case #%d: ",ks);

		if( (k & ((1<<n)-1)) == ((1<<n)-1) )
			printf("ON\n");
		else
			printf("OFF\n");
	}

	return 0;
}