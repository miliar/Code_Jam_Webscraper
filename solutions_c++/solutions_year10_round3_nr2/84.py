#include<iostream>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
int l,r,cc,ans,tt;
int f[1010][1010][11];

int main()
{
	freopen("bs.in","r",stdin);
	freopen("b.out","w",stdout);
	cin>>tt;	l=1;r=1000;
	fo(c,2,10)
	fo(ll,1,r-l+1)
		fo(i,l,r-ll+1)
		{
				int j=i+ll-1;
				if (i*c>=j)
				{
					f[i][j][c]=0;
					continue;
				}		
				f[i][j][c]=1000;
				fo(k,i+1,j-1)
					f[i][j][c]=min(f[i][j][c],max(f[i][k][c],f[k][j][c])+1);
		}
	fo(ii,1,tt)
	{
		cin>>l>>r>>cc;
		cout<<"Case #"<<ii<<": "<<f[l][r][cc]<<endl;
	}
	return 0;
}
	
