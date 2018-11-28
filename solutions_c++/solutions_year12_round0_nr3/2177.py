#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

int n,m,*a=new int[2000000],c;

int aa()
{
	int i,j,k,l=0;
	for(i=n;i<=m;++i)
	{
		j=0;
		if(!a[i])
		{
			a[i]=1;
			k=i;
			for(k=(k%10)*c+k/10;k!=i;k=(k%10)*c+k/10)
				if(k>=n&&k<=m)
				{
					a[k]=1;
					++j;
				}
		}
		l+=(j*j+j)>>1;
	}
	return l;
}


int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	int t,i,k,j;
	scanf("%d",&t);
	for(i=1;i<=t;++i)
	{
		scanf("%d%d",&n,&m);
		memset(a+n,0,(m-n+1)*sizeof(int));
		if(n<10) k=0;
		else 
		{
			for(c=1,j=n/10;j;j/=10)
				c*=10;
			k=aa();
		}
		printf("Case #%d: %d\n",i,k);
	}
}
