#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;


int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	int c[11]={0,1},b[11]={0,1},t,m,i,j,n,k,mm,a;
	for(i=2;i<11;++i)
	{
		c[i]=i*3-2;
		b[i]=i*3-4;
	}

	scanf("%d",&t);
	for(i=1;i<=t;++i)
	{
		scanf("%d%d%d",&n,&m,&mm);
//		sort(a,a+n);
		k=0;
		for(j=0;j<n;++j)
		{
			scanf("%d",&a);
			if(a>=c[mm]) ++k;
			else if(a>=b[mm])
				if(m) {++k;--m;}
		}
		printf("Case #%d: %d\n",i,k);
	}
	
}
		