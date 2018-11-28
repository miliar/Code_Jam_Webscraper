#include <iostream>
#include <vector>
#include <algorithm>

#define ll long long

using namespace std;

char F[502][502]={0};
int Px[502][502]={0};
int Py[502][502]={0};
ll Cx[502][502]={0};
ll Cy[502][502]={0};
int n,m,d;

ll getX(int j,int l,int r)
{
	return Px[r][j]-(l>0 ? Px[l-1][j] : 0)+1LL*d*(r-l+1);
}

ll getY(int i,int l,int r)
{
	return Py[i][r]-(l>0 ? Py[i][l-1] : 0)+1LL*d*(r-l+1);
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		scanf("%d%d%d\n",&n,&m,&d);
		for(int i=0;i<n;i++)
			gets(F[i]);
		for(int i=0;i<m;i++)
			Px[0][i]=F[0][i]-'0';
		for(int j=0;j<m;j++)
			for(int i=1;i<n;i++)
				Px[i][j]=Px[i-1][j]+F[i][j]-'0';
		for(int i=0;i<n;i++)
			Py[i][0]=F[i][0]-'0';
		for(int i=0;i<n;i++)
			for(int j=1;j<m;j++)
				Py[i][j]=Py[i][j-1]+F[i][j]-'0';
		bool finded=false;
		for(int K=min(n,m);K>=3;K--)
		{
			for(int i=0;i<=n-K;i++)
			{
				ll mn=-(K-1),sum=0,cx=0;
				for(int j=0;j<K;j++)
				{
					cx+=getX(j,i,i+K-1)*(mn+2*j);
					sum+=2*getX(j,i,i+K-1);
				}
				Cx[i][0]=cx;
				Cx[i][0]-=(F[i][0]-'0'+d)*(mn);
				Cx[i][0]-=(F[i+K-1][0]-'0'+d)*(mn);
				Cx[i][0]+=(F[i][K-1]-'0'+d)*(mn);
				Cx[i][0]+=(F[i+K-1][K-1]-'0'+d)*(mn);
				for(int j=1;j<=m-K;j++)
				{
					sum-=2*getX(j-1,i,i+K-1);
					cx-=sum;
					cx-=getX(j-1,i,i+K-1)*(mn);
					cx+=getX(j+K-1,i,i+K-1)*(-mn);
					sum+=2*getX(j+K-1,i,i+K-1);
					Cx[i][j]=cx;
					Cx[i][j]-=(F[i][j]-'0'+d)*(mn);
					Cx[i][j]-=(F[i+K-1][j]-'0'+d)*(mn);
					Cx[i][j]+=(F[i][j+K-1]-'0'+d)*(mn);
					Cx[i][j]+=(F[i+K-1][j+K-1]-'0'+d)*(mn);
				}
			}
			for(int j=0;j<=m-K;j++)
			{
				ll mn=-(K-1),sum=0,cx=0;
				for(int i=0;i<K;i++)
				{
					cx+=getY(i,j,j+K-1)*(mn+2*i);
					sum+=2*getY(i,j,j+K-1);
				}
				Cy[0][j]=cx;
				Cy[0][j]-=(F[0][j]-'0'+d)*(mn);
				Cy[0][j]-=(F[0][j+K-1]-'0'+d)*(mn);
				Cy[0][j]+=(F[K-1][j]-'0'+d)*(mn);
				Cy[0][j]+=(F[K-1][j+K-1]-'0'+d)*(mn);
				for(int i=1;i<=n-K;i++)
				{
					sum-=2*getY(i-1,j,j+K-1);
					cx-=sum;
					cx-=getY(i-1,j,j+K-1)*(mn);
					cx+=getY(i+K-1,j,j+K-1)*(-mn);
					sum+=2*getY(i+K-1,j,j+K-1);
					Cy[i][j]=cx;
					Cy[i][j]-=(F[i][j]-'0'+d)*(mn);
					Cy[i][j]-=(F[i][j+K-1]-'0'+d)*(mn);
					Cy[i][j]+=(F[i+K-1][j]-'0'+d)*(mn);
					Cy[i][j]+=(F[i+K-1][j+K-1]-'0'+d)*(mn);
				}
			}
			for(int i=0;i<=n-K;i++)
			{
				if (finded) break;
				for(int j=0;j<=m-K;j++)
				{
					if (Cx[i][j]==0&&Cy[i][j]==0)
					{
						printf("%d\n",K);
						finded=true;
						break;
					}
				}
			}
			if (finded) break;
		}
		if (!finded) printf("IMPOSSIBLE\n");
	}
	return 0;
}