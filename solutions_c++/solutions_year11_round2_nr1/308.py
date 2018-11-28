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
#include <cctype>
#include <string>
#include <cstring>
#include <queue>

#define fr(i,a,n) for((i)=(a);(i)<(n);(i)=(i)+1)
#define fre(i,a,n) for((i)=(a);(i)<=(n); (i)=(i)+1)
#define frre(i,j,n) for((i)=(j);(i)>=(n);(i)--)

#define pb(X) push_back((X))
#define vs vector <string>
#define vi vector <int>
#define vvi vector < vi >

#define _bc(i) __builtin_popcount(i)
#define INF 0x3f3f3f3f //1061109567
typedef long long lint;
typedef unsigned long long ull;

using namespace std;


int main()
{
	int i,t,n,j,k,tt,cnt,wn[102],mt[102];
	char a[103][103];
	double wp[102],owp[102],oowp[102],sum;
	scanf("%d",&t);
	for(tt=1; tt<=t; tt++)
	{
		scanf("%d",&n);
		for(i=0;i<n; i++)
			scanf("%s",a[i]);
		for(i=0; i<n; i++)
		{
			wn[i]=0,mt[i]=0;
			for(j=0; j<n; j++)
			{
				if(a[i][j]=='1')
				{
					wn[i]++;
					mt[i]++;
				}
				if(a[i][j]=='0')
					mt[i]++;	
			}
			wp[i]=(double)wn[i]/(double)mt[i];
			//owp[i]=(double)(mt-wn)/(double)mt;
		}
		for(i=0; i<n; i++)
		{
			double x=0;
			cnt=0;
			sum=0.0;
			for(j=0; j<n; j++)
			{
				if(a[i][j]!='.')
					cnt++;
				if(i==j)
					continue;
				if(a[j][i]=='1')
				{
					x+=(double)(wn[j]-1)/(double)(mt[j]-1);
				}
				else if(a[j][i]=='0')
					x+=(double)wn[j]/(double)(mt[j]-1);
			}
			owp[i]=x/(double)cnt;
		}
		for(i=0; i<n; i++)
		{
			sum=0;
			cnt=0;
			for(j=0; j<n; j++)
			{
				if(a[i][j]!='.')
				{
					cnt++;
					sum+=owp[j];
				}
			}
			oowp[i]=sum/(double)cnt;
		}
		printf("Case #%d:\n",tt);
		for(i=0; i<n; i++)
		{
			//printf("%lf %lf %lf\n",wp[i],owp[i],oowp[i]);
			double RPI=0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf("%lf\n",RPI);
		}
			
	}
	return 0;
}
