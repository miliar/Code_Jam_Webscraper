#include<stdio.h>
#include<memory>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,o,i,j,k,x,y,a,b,c,d,m,n;
	int z[3][3];
	__int64 ans;
	scanf("%d",&t);
	for(o=1;o<=t;o++)
	{
		memset(z,0,sizeof(z));
		scanf("%d%d%d%d%d%d%d%d",&n,&a,&b,&c,&d,&x,&y,&m);
		for(i=0;i<n;i++)
		{
			z[x%3][y%3]++;
			x=(a*(__int64)x+b)%m;
			y=(c*(__int64)y+d)%m;
		}
		ans=0;
		for(i=0;i<3;i++)
			for(j=0;j<3;j++)
				if(z[i][j]>=3)
					ans+=z[i][j]*(__int64)(z[i][j]-1)*(z[i][j]-2)/6;
		for(i=0;i<9;i++)
			for(j=i+1;j<9;j++)
				for(k=j+1;k<9;k++)
					if(!((i/3+j/3+k/3)%3)&&!((i%3+j%3+k%3)%3))
						ans+=z[i/3][i%3]*(__int64)z[j/3][j%3]*z[k/3][k%3];
		printf("Case #%d: %I64d\n",o,ans);
	}
	return 0;
}


