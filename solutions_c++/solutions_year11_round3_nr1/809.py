#include <iostream>
using namespace std;
char map[55][55];
int main()
{
	int t,r,c;
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cin>>r>>c;
		memset(map,0,sizeof(map));
		for (int j=0;j<r;j++)
			cin>>map[j];
		bool flag=1;
		for (int j=0;j<r;j++)
		{
			for (int k=0;k<c;k++)
			{
				if (map[j][k]=='#')
				{
					if (j+1>=r||k+1>=c)
					{
						flag=0;
						break;
					}
					if (map[j+1][k]=='#'&&map[j][k+1]=='#'&&map[j+1][k+1]=='#')
					{
						map[j][k]=map[j+1][k+1]='/';
						map[j][k+1]=map[j+1][k]='\\';
					}
					else
					{
						flag=0;
						break;
					}
				}
			}
			if (flag==0)
				break;
		}
		cout<<"Case #"<<i<<":"<<endl;
		if (flag==0)
			cout<<"Impossible"<<endl;
		else
		{
			for (int j=0;j<r;j++)
				cout<<map[j]<<endl;
		}
	}
	return 0;
}