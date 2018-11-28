#include<iostream>
using namespace std;
int main()
{
	freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\A-large.out","w",stdout);

	int T,cas,m,n;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		scanf("%d%d",&n,&m);
		printf("Case #%d: ",cas);
		printf((m%(1<<n)+1==(1<<n))?"ON\n":"OFF\n");
	}
}