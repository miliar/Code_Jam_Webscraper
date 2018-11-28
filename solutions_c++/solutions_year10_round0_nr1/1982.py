#include<iostream>
using namespace std;
int main()
{
	freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\A-large.out","w",stdout);

	int T,cas;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		long long N,K;
		scanf("%d%d",&N,&K);
		printf("Case #%d: ",cas);
		N=(1LL<<N)-1;
		K&=N;
		puts((K==N)?"ON":"OFF");
	}
}