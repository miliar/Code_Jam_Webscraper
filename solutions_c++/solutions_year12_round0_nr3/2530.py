#include<cstdio>
#include<stdlib.h>
#include<string.h>

using namespace std;

int tt;
int a,b;
char s[10];

int go(int x)
{
	int vys=0;
	sprintf(s,"%d",x);
	int len=strlen(s),k=len-1;
	int bolo[10],sz=0;
	while(k--)
	{
		for(int i=len-1;i>=0;--i)
			s[i+1]=s[i];
		s[0]=s[len];
		s[len]=0;
		if (s[0]!='0')
		{
			int y=atoi(s);
			int ok=1;
			for(int j=0;j<sz;++j)
				if (bolo[j]==y)
				{
					ok=0;
					break;
				}
			if (ok&&y<x&&y>=a)
			{
				bolo[sz++]=y;
				++vys;
			}
		}
	}
	return vys;
}

int main()
{
	scanf("%d",&tt);
	for(int t=1;t<=tt;++t)
	{
		scanf("%d%d",&a,&b);
		int vys=0;
		while(b>=a)
			vys+=go(b--);
		printf("Case #%d: %d\n",t,vys);
	}
	return 0;
}
