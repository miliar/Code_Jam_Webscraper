#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>

using namespace std;

int mas[1000][1000];

void solve()
{
	for(int i=0;i<1000;i++)
		for(int j=0;j<1000;j++)
			mas[i][j]=0;

	int r,c,d;
	cin>>r>>c>>d;
	char ch;

	for(int i=0;i<r;i++)
		for(int j=0;j<c;j++)
		{
			cin>>ch;
			mas[i][j]=ch-'0';
		}

	int res;

	double sx,sy;

	for(res=min(r,c);res>2;res--)
	{
		for(int i=0;i+res<=r;i++)
		{
			for(int j=0;j+res<=c;j++)
			{
				sx=0;
				sy=0;
				
				for(int x=0;x<res;x++)
					for(int y=0;y<res;y++)
					{
						sx+=(x-0.5*(res-1))*mas[i+x][j+y];
						sy+=(y-0.5*(res-1))*mas[i+x][j+y];
					}
				sx-=(0-0.5*(res-1))*mas[i][j];
				sy-=(0-0.5*(res-1))*mas[i][j];

				sx-=(0-0.5*(res-1))*mas[i][j+res-1];
				sy-=(0.5*(res-1))*mas[i][j+res-1];

				sx-=(0.5*(res-1))*mas[i+res-1][j];
				sy-=(0-0.5*(res-1))*mas[i+res-1][j];

				sx-=(0.5*(res-1))*mas[i+res-1][j+res-1];
				sy-=(0.5*(res-1))*mas[i+res-1][j+res-1];

				if(sx==0.0 && sy==0.0)
				{
					cout<<res;
					return;
				}

				//cout<<res<<' '<<i<<' '<<j<<" failed"<<endl;
			}
		}
	}
	

	cout<<"IMPOSSIBLE";
}

int main()
{
	cout.precision(10);
	freopen("file.in","r",stdin);
	freopen("file.out","w",stdout);

	int t;
	cin>>t;

	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<(i+1)<<": ";
		solve();
		cout<<endl;
	}

	return 0;
}