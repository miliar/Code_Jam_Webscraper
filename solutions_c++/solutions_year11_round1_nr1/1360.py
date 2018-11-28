#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("lowesy.out","w",stdout);
	int _,cases=1;
	scanf("%d\n",&_);
	while(_--)
	{
		int N,D,G;
		scanf("%d%d%d",&N,&D,&G);
		printf("Case #%d: ",cases++);
		if(G==100&&D!=100)
		{
			puts("Broken");
			continue;
		}
		bool f=false;
		for(int i=1;i<=N&&!f;i++)
		{
			int v=i*D;
			if(v%100!=0) continue;
			bool ok=false;
			for(int j=i;j<=1000000&&!ok;j++)
			{
				int t=j*G;
				if(t%100!=0) continue;
				if(v/100<=t/100) ok=true;
			}
			if(ok) f=true;
		}
		if(f) puts("Possible");
		else puts("Broken");
	}
	return 0;
}