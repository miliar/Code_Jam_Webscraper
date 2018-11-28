#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string>VS;
int n,m,t,i,j,k,c,ii,jj,kk,ax,ay,bx,by,cx,cy;
double aa,bb,cc,pp,ss,a;
bool r;
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
 	freopen("B-small-attempt1.out","w",stdout);
	scanf("%d",&t);
	c=1;
	while (c<=t)
	{
		printf("Case #%d:",c++);
		scanf("%d%d%lf",&n,&m,&a);
		a/=2.0;
		r=false;
		for(i=0;i<=n;i++)
		{
			if (r) break;
			for(ii=0;ii<=m;ii++)
			{
				if (r) break;
				for(j=0;j<=n;j++)
				{
					if (r) break;
					for(jj=0;jj<=m;jj++)
					{
						if (r) break;
						for(k=0;k<=n;k++)
						{
							if (r) break;
							for(kk=0;kk<=m;kk++)
							{
								aa=sqrt(1.0*((i-j)*(i-j)+(ii-jj)*(ii-jj)));
								bb=sqrt(1.0*((i-k)*(i-k)+(ii-kk)*(ii-kk)));
								cc=sqrt(1.0*((j-k)*(j-k)+(jj-kk)*(jj-kk)));
								pp=(aa+bb+cc)/2;
								ss=sqrt(pp*(pp-aa)*(pp-bb)*(pp-cc));
								if (fabs(ss-a)<1e-9) 
								{
									r=true;
									ax=i;ay=ii;bx=j;by=jj;cx=k;cy=kk;
									break;
								}
							}
						}
					}
				}
			}
		}
		if (r) printf(" %d %d %d %d %d %d\n",ax,ay,bx,by,cx,cy);
		else printf(" IMPOSSIBLE\n");
	}
	return 0;
}
								

