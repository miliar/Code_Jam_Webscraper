
#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	freopen("A-Large.in","r",stdin);
	freopen("A-Large.out","w",stdout);
	int caseNum;
	int x,y,z;
	int n,k;
	char map[50][50];
	bool red,blue;

	cin >> caseNum;
	for (int crtCase=1; crtCase<caseNum+1; ++crtCase)
	{
		cin >> n >> k;
		for (int i=0; i<n; ++i)
			for (int j=0; j<n; ++j)
				cin>>map[i][j];
		for (int j=n-2; j>=0; --j)
			for (int i=0; i<n; ++i)
				if (map[i][j]!='.')
				{
					x=j;
					while ((x!=n-1)&&(map[i][x+1]=='.'))
					{
						map[i][x+1]=map[i][x];
						map[i][x]='.';
						++x;
					}
				}

		red = false; blue = false;
		for (int i=0; i<n; ++i)
			for (int j=0; j<n; ++j)
			{
				if (!red)
				{
					x=i;y=j;z=0;
					while ((x!=n)&&(y!=n)&&(x!=-1)&&(y!=-1)&&(map[x][y]=='R'))
					{
						++z;
						++x;
					}
					if (z>=k) red = true;
					x=i;y=j;z=0;
					while ((x!=n)&&(y!=n)&&(x!=-1)&&(y!=-1)&&(map[x][y]=='R'))
					{
						++z;
						++y;
					}
					if (z>=k) red = true;
					x=i;y=j;z=0;
					while ((x!=n)&&(y!=n)&&(x!=-1)&&(y!=-1)&&(map[x][y]=='R'))
					{
						++z;
						++x;
						++y;
					}
					if (z>=k) red = true;
					x=i;y=j;z=0;
					while ((x!=n)&&(y!=n)&&(x!=-1)&&(y!=-1)&&(map[x][y]=='R'))
					{
						++z;
						++x;
						--y;
					}
					if (z>=k) red = true;
				}
				if (!blue)
				{
					x=i;y=j;z=0;
					while ((x!=n)&&(y!=n)&&(x!=-1)&&(y!=-1)&&(map[x][y]=='B'))
					{
						++z;
						++x;
					}
					if (z>=k) blue = true;
					x=i;y=j;z=0;
					while ((x!=n)&&(y!=n)&&(x!=-1)&&(y!=-1)&&(map[x][y]=='B'))
					{
						++z;
						++y;
					}
					if (z>=k) blue = true;
					x=i;y=j;z=0;
					while ((x!=n)&&(y!=n)&&(x!=-1)&&(y!=-1)&&(map[x][y]=='B'))
					{
						++z;
						++x;
						++y;
					}
					if (z>=k) blue = true;
					x=i;y=j;z=0;
					while ((x!=n)&&(y!=n)&&(x!=-1)&&(y!=-1)&&(map[x][y]=='B'))
					{
						++z;
						++x;
						--y;
					}
					if (z>=k) blue = true;
				}
			}

		cout<<"Case #"<<crtCase<<": ";
		if (red&&blue) cout<<"Both"<<endl;
		else if (!red&&!blue) cout<<"Neither"<<endl;
		else if (red&&!blue) cout<<"Red"<<endl;
		else if (!red&&blue) cout<<"Blue"<<endl;
	}
	return 0;
}
