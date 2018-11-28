#include<iostream>
using namespace std;
struct 
{
	__int64 x,y;
	int a,b,c,d,m;
	void next()
	{
		x=(a*x+b)%m;
		y=(c*y+d)%m;
	}
}random;
__int64 mhash[3][3];
int main()
{
	int n;
	int a,b,c,d,m,k,tn;
	int x0,y0;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&n);
	for(tn=1;tn<=n;++tn)
	{
		memset(mhash,0,sizeof(mhash));
		scanf("%d%d%d%d%d%d%d%d",&k,&a,&b,&c,&d,&x0,&y0,&m);
		random.x=x0;random.y=y0;
		random.a=a;random.b=b;random.c=c;random.d=d;random.m=m;
		//k=20;
		mhash[x0%3][y0%3]=1;
		__int64 ans=0;
		int a,b,c,x,y,z;
		int i,j,hk;
		for(hk=1;hk<=k-1;++hk)
		{
			random.next();
			i=random.x%3;
			j=random.y%3;
			for(a=0;a<3;++a)
			{
				for(x=0;x<3;++x)
				{
					if((i+a+a)%3==0&&(j+x+x)%3==0)
						ans+=mhash[a][x]*(mhash[a][x]-1)/2;
				}
			}
			__int64 tmp=0;
			for(a=0;a<3;++a)
			{
				for(b=0;b<3;++b)
				{
					for(x=0;x<3;++x)
					{
						for(y=0;y<3;++y)
						{
							if(a==b&&x==y)continue;
							if((a+b+i)%3==0&&(x+y+j)%3==0)
								tmp+=mhash[a][x]*mhash[b][y];
						}
					}
				}
			}
			ans+=tmp/2;
			++mhash[i][j];
		}
		printf("Case #%d: %I64d\n",tn,ans);
	}
	return 0;
}