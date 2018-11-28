#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int N,K,test;

int main()
{
	//freopen("i.txt","r",stdin);
	int cnt=1;
	for (scanf("%d",&test);test--;cnt++)
	{
		scanf("%d%d",&N,&K);
		bool ok=true;
		for (int i=1;i<=N;++i,K>>=1)
			if (!(K&1)) ok=false;
		printf("Case #%d: ",cnt);
		puts(ok?"ON":"OFF");
	}
	return 0;
}
