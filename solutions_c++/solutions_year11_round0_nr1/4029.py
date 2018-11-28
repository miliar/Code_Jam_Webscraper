#include <cstdio>
#include <cstring>
int max(int x,int y) {return (x<y)?y:x;}
int abs(int x) {return (x<0)?-x:x;}
int main()
{
	int n,i,j,t,x;
	char c;
	freopen("in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for (i=1;i<=t;++i)
	{
		scanf("%d  ",&n);
		char c;int o=1,b=1,x,sol=0,to=0,tb=0;
		for (j=1;j<=n;++j)
		{
				scanf("%c %d ",&c,&x);
				if (c=='O') 
					sol+=1+max(0,abs(x-o)-sol+to),o=x,to=sol; else
						sol+=1+max(0,abs(x-b)-sol+tb),b=x,tb=sol;
			}
		printf("Case #%d: %d\n",i,sol);
	}
return 0;
}
					
		