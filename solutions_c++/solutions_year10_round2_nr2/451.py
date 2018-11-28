#include <cstdlib>
#include <cstdio>
#include <iostream>

using namespace std;

int N,K,B,T;
int X[100],V[100];
bool Can[100];


void Solve(int KKK)
{
	scanf("%d%d%d%d",&N,&K,&B,&T);
	for (int i=1;i<=N;++i)
		scanf("%d",&X[i]);
	for (int i=1;i<=N;++i)
		scanf("%d",&V[i]);
	for (int i=1;i<=N;++i)
		Can[i]=(X[i]+V[i]*T>=B);
	int k=K,p;
	for (p=N;p&&k;--p)
		k-=Can[p];
	if (k!=0)
	{
		printf("Case #%d: IMPOSSIBLE\n",KKK);
		return ;
	}
	int Ans=0;
	for (int i=p+1;i<=N;++i)
		if (Can[i])
		for (int j=i+1;j<=N;++j)
			Ans+=!Can[j];
	printf("Case #%d: %d\n",KKK,Ans);
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int Test;
	scanf("%d",&Test);
	for (int i=1;i<=Test;++i)
		Solve(i);
	
	return 0;
}