#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>

int n,m,T;

void Solve(int x)
{
	scanf("%d%d",&n,&m);
	int Ans=1;
	for (int i=1;i<=n;++i){
		int p=m & 1;
		m>>=1;
		Ans&=p;
		if (!Ans) break;
	}
	if (Ans) printf("Case #%d: ON\n",x);
	else printf("Case #%d: OFF\n",x);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for (int i=1;i<=T;++i)
		Solve(i);
	return 0;
}
