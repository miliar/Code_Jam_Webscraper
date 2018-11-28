#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

const int MAXN=10010;

int F[MAXN],D[MAXN],I[MAXN];
int N,End;

bool Solve()
{
	memset(F,0,sizeof(F));
	scanf("%d",&N);
	for (int i=1;i<=N;++i)
		scanf("%d%d",&D[i],&I[i]);
	scanf("%d",&End);
	F[1]=D[1];
	for (int i=1;i<=N;++i)
	{
		for (int j=i+1;j<=N&&D[j]-D[i]<=F[i];++j)
			F[j]=max(F[j],min(D[j]-D[i],I[j]));
		//printf("%d:%d\n",i,F[i]);
		if (F[i]+D[i]>=End)	return true;
	}
	return false;
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;++i)
		printf("Case #%d: %s\n",i,Solve()?"YES":"NO");
	return 0;
}