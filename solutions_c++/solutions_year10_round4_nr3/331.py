#include <cstdlib>
#include <cctype>
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

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

#define eps 1e-8
#define inf 1000000000
#define MAXN 1010
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef pair<int,int> PII;

bool mp[2][110][110];
int main()
{
//	freopen("C-small-attempt0","r",stdin);
	freopen("c.out","w",stdout);
	int cs,c,r,i,j,k,x1,y1,x2,y2,ne,st;
	scanf("%d",&cs);
	for (c=1;c<=cs;c++)
	{
		//cout<<c<<endl;
		scanf("%d",&r);
		
		memset(mp,false,sizeof(mp));
		for (i=0;i<r;i++)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			x1--;y1--;x2--;y2--;
			for (j=x1;j<=x2;j++)
				for (k=y1;k<=y2;k++)
					mp[0][j][k]=true;
		}
		st=0;
		for (i=0;;i++)
		{
			
			for (j=0;j<100;j++)
			{
				for (k=0;k<100;k++)
					if (mp[st][j][k]) break;
				if (k<100) break;
			}
			if (j==100 && k==100)
			{
				printf("Case #%d: %d\n",c,i);
				break;
			}
			
/*			for (j=0;j<7;j++)
			{
				for (k=0;k<7;k++)
					cout<<mp[st][j][k];
				cout<<endl;
			}
			cout<<endl;
			system("pause");*/
			ne=(st+1)%2;
			for (j=0;j<100;j++)
				for (k=0;k<100;k++)
					mp[ne][j][k]=mp[st][j][k];
			for (j=0;j<100;j++)
				for (k=0;k<100;k++)
					if (j>0 && k>0)
						if (mp[st][j][k])
						{
							if (!mp[st][j-1][k] && !mp[st][j][k-1])
								mp[ne][j][k]=false;
						}
						else
						{
							if (mp[st][j-1][k] && mp[st][j][k-1])
							mp[ne][j][k]=true;
						}
					else
						if (mp[st][j][k]) mp[ne][j][k]=false;
			st=ne;
		}
	}
	return 0;
}
