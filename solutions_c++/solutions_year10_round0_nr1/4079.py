#include<cstdio>

using namespace std;

int i,n,p,a,b,j,r;



int main()
{
	freopen("date.in","r",stdin);
	//freopen("date.out","w",stdout);
	scanf("%d",&n);
	for (i=1;i<=n;++i)
	{
		scanf("%d%d",&a,&b);
		p=1;
		for (j=1;j<=a;++j)
			p*=2;
		r=p;
		while (r<=b)
			r+=p;
		//if (!b) g<<"Case #"<<i<<": "<<"OFF\n";
		 if (r-1==b) 
				printf("Case #%d: ON\n",i);

		else printf("Case #%d: OFF\n",i);
	}
	return 0;
} 
