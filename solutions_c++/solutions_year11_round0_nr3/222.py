#include<cstdio>
int main()
{
	int _;scanf("%d",&_);
	for(int __=1;__<=_;__++)
	{
		int n,s=0,m=1000000007,x=0;
		scanf("%d",&n);
		while(n--)
		{
			int a;scanf("%d",&a);
			s+=a;if(m>a)m=a;x^=a;
		}
		if(x==0)printf("Case #%d: %d\n",__,s-m);
		else printf("Case #%d: NO\n",__);
	}
	return 0;
}
