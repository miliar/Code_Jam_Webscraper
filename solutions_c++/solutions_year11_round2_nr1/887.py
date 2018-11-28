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
#include <cstring>
#include <string>
using namespace std;
char g[128][128];
double owparr[128];
double wparr[128];
int main()
{
	int X;
	scanf("%d",&X);
	int kase=1;
	while(X--)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)scanf("%s",g[i]);
		printf("Case #%d:\n",kase);
		double wp,owp,oowp;
		double res;
		int total,win,cnt=0;
		for(int i=0;i<n;i++)
		{
			win=0;total=0;
			for(int j=0;j<n;j++)
			{
				if(g[i][j]!='.')total++;
				if(g[i][j]=='1')win++;
			}
			wp=win*1.0/total;
			wparr[i]=wp;
			owp=0;
			cnt=0;
			for(int j=0;j<n;j++)
			{
				if(g[i][j]!='.')
				{
					win=total=0;
					for(int k=0;k<n;k++)
					{
						if(k==i)continue;
						if(g[j][k]!='.')total++;
						if(g[j][k]=='1')win++;

					}
					owp+=(win*1.0/total);
					cnt++;
				}

			}
			owp/=cnt;
			owparr[i]=owp;
			//printf("i si %d wp is %lf owp is %lf\n",wp,owp);
		}
		for(int i=0;i<n;i++)
		{
			wp=wparr[i];
			owp=owparr[i];
			oowp=0;cnt=0;
			for(int j=0;j<n;j++)
			{
				if(g[i][j]!='.')
				{
					oowp+=owparr[j];
					cnt++;
				}
			}
			oowp/=cnt;
			res=0.25 * wp + 0.50 * owp + 0.25 * oowp;
			printf("%0.12lf\n",res);
		}
		kase++;

	}
}

