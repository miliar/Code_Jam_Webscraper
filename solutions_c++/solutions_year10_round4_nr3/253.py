#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <cstring>
#include <cmath>

using namespace std;

bool u[101][101],uu[101][101];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T,t,i,j,k,n=100,m=100,x1,y1,x2,y2;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		memset(u,0,sizeof(u));
		cin>>k;
		while(k--)
		{
			cin>>x1>>y1>>x2>>y2;
			for(i=x1;i<=x2;i++)
				for(j=y1;j<=y2;j++) u[i][j]=true;
		}
		
		for(k=1;;k++)
		{
			for(i=1;i<=n;i++)
				for(j=1;j<=m;j++)
				{
					uu[i][j]=u[i][j];
					if (!u[i][j-1] && !u[i-1][j]) uu[i][j]=false;
					if (u[i-1][j] && u[i][j-1]) uu[i][j]=true;
				}
			bool br=true;
			for(i=1;i<=n;i++)
				for(j=1;j<=m;j++)
				{
					if (uu[i][j]) br=false;
					u[i][j]=uu[i][j];
				}
			if (br) break;
		}
		printf("Case #%d: %d\n",t,k);
	}

	return 0;
}