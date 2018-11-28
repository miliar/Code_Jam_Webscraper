#include<cstdio>
#define MN 16
int test,ntest,n,i,j,xa,xb,sa,sb,t[MN],w;
int main()
{
	scanf("%d",&ntest);
	for(test=1; test<=ntest; ++test)
	{
		scanf("%d",&n);
		for(i=0; i<n; ++i)
			scanf("%d",t+i);
		w=-1;
		for(i=(1<<n)-2; i>0; --i) 
		{
			xa=xb=sa=sb=0;
			for(j=0; j<n; ++j)
				if(i & (1<<j)) { xa^=t[j]; sa+=t[j]; }
				else           { xb^=t[j]; sb+=t[j]; }
			if(xa==xb && sa>w) w=sa;
		}
		if(w<0) printf("Case #%d: NO\n",test);
		else printf("Case #%d: %d\n",test,w);
	}
}
