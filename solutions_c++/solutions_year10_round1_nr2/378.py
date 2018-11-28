#include<iostream>
#include<cstdio>

using namespace std;

int f[101][256],d,I,m,n,a[101],z,g[101][256],ans;

inline int abs(int a)
{
	return a>0?a:-a;
}

inline int insert(int a,int b)
{
	if(m==0)
		return a==b?0:1<<29;
	int re=abs(a-b)/m;
	if(abs(a-b)%m==0)
		--re;
	return max(0,re*I);
}

int main()
{
	freopen("gcjr2b.in","r",stdin);
	freopen("gcjr2b.out","w",stdout);
	scanf("%d",&z);
	for(int zz=1;zz<=z;++zz)
	{
	//	cout<<zz<<endl;
		ans=1<<29;
		scanf("%d %d %d %d",&d,&I,&m,&n);
		//cout<<insert(1,50)<<endl;;
		for(int i=1;i<=n;++i)
			scanf("%d",&a[i]);
		for(int i=1;i<=n;++i)
		{
			for(int j=0;j<=255;++j)
			{
				f[i][j]=1<<29;
				for(int k=0;k<i;++k)
					for(int l=0;l<=255;++l)
						f[i][j]=min(f[i][j],d*(i-k-1)+f[k][l]+abs(a[i]-j)+insert(j,l));
				if(n==i)
					ans=min(ans,f[i][j]);
				//cout<<i<<' '<<j<<' '<<f[i][j]<<endl;
			}
		}
		printf("Case #%d: %d\n",zz,ans);
	}
	return 0;
}
