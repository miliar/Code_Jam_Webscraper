#include<cstdlib>
#include<stdio.h>
#include<vector>

using namespace std;


int main()
{
	int t,n;
	int min,sxor,suma,tmp;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
	{
		scanf("%d",&n);
		scanf("%d",&tmp); sxor=suma=min=tmp;
		for(int j=1;j<n;++j)
		{
			scanf("%d",&tmp);
			suma+=tmp;
			sxor^=tmp;
			if(tmp<min) min=tmp;
		}
		if(sxor==0)
			printf("Case #%d: %d\n",i+1,suma-min);
		else
			printf("Case #%d: NO\n",i+1);
	}
}
