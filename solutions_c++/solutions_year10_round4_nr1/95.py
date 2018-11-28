#include<iostream>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
int n,m,tt,ii,ans;
int map[300][300];
int f[300][300];

bool check(int t)
{
	 fo(i,1,t)
	 	fo(j,1,i)
	 	{
	 		if (f[i][j]==0)f[i][j]=f[j][i];
	 		if (f[j][i]==0)f[j][i]=f[i][j];
	 		if (f[i][j]!=f[j][i])
			 {
				//	cout<<i<<"!"<<j<<endl;
					return false;
				}
		}
	 fo(i,1,t)
	 	fo(j,i,t)
	 	{
	 		if (f[i][j]==0)f[i][j]=f[t-j+1][t-i+1];
	 		if (f[t-j+1][t-i+1]==0)f[t-j+1][t-i+1]=f[i][j];
	 		if (f[i][j]!=f[t-j+1][t-i+1]){
				//	cout<<i<<" "<<j<<endl;
					return false;
				}
		}
	return true;
}
	 		

int main()
{
	freopen("al.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>tt;
	fo(ii,1,tt)
	{
		cin>>n;
		fo(i,1,n)
			fo(j,1,i)
				cin>>map[j][n+j-i];
		for(int i=n-1;i;i--)
			fo(j,1,i)
				cin>>map[n+j-i][j];
	/*	fo(i,1,n)
		{
			fo(j,1,n)
				cout<<map[i][j];
			cout<<endl;
		}*/
		fo(t,n,220)
		{
			bool ok=false;
			fo(i,1,t-n+1)
				if (!ok)
				fo(j,1,t-n+1)
				{	
					memset(f,0,sizeof(f));
					fo(ii,1,n)
						fo(jj,1,n)
							f[i+ii-1][j+jj-1]=map[ii][jj]+1;
					if (check(t))
					{
						ok=true;
						break;
					}
				}
			if (ok)
			{
				cout<<"Case #"<<ii<<": "<<t*t-n*n<<endl;
				break;
			}
		}
	}
	return 0;
}
	
