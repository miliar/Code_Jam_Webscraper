#include <iostream>
#include <cstdio>
using namespace std;
int tim,n,k;
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&tim);
	for(int i=1;i<=tim;i++)
	{
		scanf("%d %d\n",&n,&k);
		bool bo=1;
		for(int j=1;j<=n;j++)
		if(!(k&1))
		{
			bo=0;
			break;
		}else
			k>>=1;
		if(bo)
			printf("Case #%d: ON\n",i);
			else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}
