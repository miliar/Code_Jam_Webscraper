#include<iostream>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
const int cc[4][2]={{-1,0},{0,-1},{1,0},{0,1}};
int	n,m,ans,tt,x1,x2,y1,y2;
int map[110][110];

bool check()
{
	fo(i,1,n)
		fo(j,1,n)
			if(map[i][j])
				return false;
	return true;
}

int main()
{
	freopen("cs.in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>tt;
	memset(map,0,sizeof(map));
	fo(ii,1,tt)
	{
		cin>>m;
		n=100;

		fo(i,1,m)
		{
			cin>>x1>>y1>>x2>>y2;
			fo(j,x1,x2)
				fo(k,y1,y2)
					map[j][k]=1;
		}
		int ans=0;
		while(1)
		{
			if (check())break;
			ans++;
			for(int i=n;i;i--)
				for(int j=n;j;j--)
					if ((!map[i-1][j])&&(!map[i][j-1]))
						map[i][j]=0;else
					if ((map[i-1][j])&&(map[i][j-1]))
						map[i][j]=1;
		}

		cout<<"Case #"<<ii<<": "<<ans<<endl;
	}
	return 0;
}
	
