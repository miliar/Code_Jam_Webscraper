#include <iostream>
#include <stdio.h>
#include <memory.h>
using namespace std;

int num[11000];

int main()
{
	int t,n,i,j,l,h,test=0;
	FILE *f;
	f=fopen("C.out","w");

	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&n,&l,&h);
		for(i=1;i<=n;i++) scanf("%d",&num[i]);
		for(i=l;i<=h;i++)
		{
			for(j=1;j<=n;j++)
			{
				if(num[j]%i!=0&&i%num[j]!=0) break;
			}
			if(j>n) break;
		}
		fprintf(f,"Case #%d: ",++test);
		if(i>h) fprintf(f,"NO\n");
		else fprintf(f,"%d\n",i);
	}
	return 0;
}
