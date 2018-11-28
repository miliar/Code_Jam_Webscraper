#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#define oo 1005

using namespace std;

long long v[oo],x[oo];
long long n,m,end,t,p,q,Ans,Test;

void Solve()
{
	p=0,q=0,Ans=0;
	scanf("%I64d%I64d%I64d%I64d",&n,&m,&end,&t);
	for (int i=1;i<=n;++i)
		scanf("%I64d",&x[i]);
	for (int i=1;i<=n;++i)
		scanf("%I64d",&v[i]);
		
	for (int i=n;i>=1;--i){
		if (q==m) break;
		if (v[i]*t>=end-x[i])
			Ans+=p,++q;	
		else ++p;
	}
	if (q==m) printf("%I64d\n",Ans);
	else printf("IMPOSSIBLE\n");
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%d",&Test);
	
	for (int i=1;i<=Test;++i){
		printf("Case #%d: ",i);
		Solve();
	}
	
	return 0;
}
