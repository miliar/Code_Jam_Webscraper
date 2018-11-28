#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;


bool mp[110][110];
int main()
{
	freopen("e:\\C1.txt","r",stdin);
//freopen("e:\\c1.out","w",stdout);
	int y,z,i,j,k,l,o;
	int x1,y1,x2,y2;
	scanf("%d",&z);
	for (y=1;y<=z;y++)
	{
		scanf("%d",&o);
		memset(mp,false,sizeof(mp));
		while(o--)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (j=x1;j<=x2;j++)
				for (k=y1;k<=y2;k++)
					mp[j][k]=true;
		}
		int ans=0;
		bool ifadd=true;
		while(ifadd)
		{
			ifadd=false;
		//	for(i=0;i<7;i++,cout<<endl)
			//	for(j=0;j<7;j++)
				//	printf("%d ",mp[i][j]?1:0);
//			cout<<endl;
		for(i=105;i>0;i--)
		{
			for(j=105;j>0;j--)
			{
				if(mp[i][j] && mp[i-1][j]==false && mp[i][j-1]==false)
					mp[i][j]=false;
				else if(mp[i][j]==false && mp[i-1][j]==true && mp[i][j-1]==true)
					ifadd=mp[i][j]=true;
				else if(mp[i][j])
					ifadd=true;
			}
		}
			ans++;
		}
		printf("Case #%d: %d\n",y,ans);
	}
	for(;;);
	return 0;
}
