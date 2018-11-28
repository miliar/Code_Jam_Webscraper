#include<iostream>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
const int cc[4][2]={{-1,0},{0,-1},{1,0},{0,1}};
int	n,m,ans,tt;
char c;
int map[1010][1010];
int st[1010][2];

int main()
{
	freopen("cl.in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>tt;
	fo(ii,1,tt)
	{
		cin>>n>>m;
		ans=0;
		fo(i,1,n)
			fo(j,1,m/4)
			{
				cin>>c;
				int k;
				if (c<='9')
					k=c-48;
				else
					k=c-55;
				fo(t,1,4)
					map[i][(j-1)*4+t]=(k&(1<<(4-t)))>0;
			}
	/*	fo(i,1,n)
		{
			fo(j,1,m)
				cout<<map[i][j];
			cout<<endl;
		}*/
		for(int k=min(n,m);k;k--)
		{
			int s=0;
			fo(i,1,n-k+1)
				fo(j,1,m-k+1)
				{
					bool ok=true;
					fo(ii,i,i+k-1)
					{
						if (!ok)break;
						fo(jj,j,j+k-1)
						{
							fo(kk,0,3)
							{
								int x=ii+cc[kk][0],y=jj+cc[kk][1];
								if ((x>=i)&&(x<=i+k-1)&&(y>=j)&&(y<=j+k-1)&&(map[x][y]==map[ii][jj]))
									ok=false;
							}
							if (map[ii][jj]==2)
								ok=false;
							if (!ok)break;
						}
					}
					if (ok)
					{
						fo(ii,i,i+k-1)
							fo(jj,j,j+k-1)
								map[ii][jj]=2;
						s++;
					}
				}
			if (s>0)
			{
				st[++ans][0]=k;
				st[ans][1]=s;
			}
		}		
									
		cout<<"Case #"<<ii<<": "<<ans<<endl;
		fo(i,1,ans)
			cout<<st[i][0]<<" "<<st[i][1]<<endl;
	}
	return 0;
}
	
