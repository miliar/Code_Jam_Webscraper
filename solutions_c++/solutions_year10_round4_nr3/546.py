#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
using namespace std;

int d[200][200],e[200][200];

int main()
{
	//freopen("C.in","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
	//freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
	//freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
	//freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);

	int T,C=0,R,i,j,x1,x2,y1,y2,t,mx,my,f;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++C);
		scanf("%d",&R);
		memset(d,0,sizeof(d));
		mx=0;my=0;
		while(R--)
		{
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);

			if(x2>mx)mx=x2;
			if(y2>my)my=y2;
			for(i=x1;i<=x2;i++)
				for(j=y1;j<=y2;j++)
				{
					d[i][j]=1;
				}
		}
		for(t=1;;t++)
		{
			f=0;
			for(i=1;i<=mx;i++)
				for(j=1;j<=my;j++)
				{
					if(d[i][j])
					{
						if(d[i-1][j] || d[i][j-1])
							e[i][j]=1,f=1;
						else
							e[i][j]=0;
					}
					else
					{
						if(d[i-1][j] && d[i][j-1])
							e[i][j]=1,f=1;
						else
							e[i][j]=0;
					}
				}
				if(!f)break;
				memcpy(d,e,sizeof(d));
		}
		printf("%d\n",t);
	}
	return 0;
}
