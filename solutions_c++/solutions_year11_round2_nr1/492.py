#include <iostream>
#include <set>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <math.h>
#include <cstdlib>
#include <memory.h>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)>(0)?(a):(-(a)))
#define mp make_pair
#define pnt pair<int,int>
#define MEMS(a,b) memset((a),(b),sizeof(a))
#define pb push_back
#define LL long long
#define U unsigned
char a[210][210];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(itt,0,test)
	{
		int n;
		cin>>n;
		printf("Case #%d:\n",itt+1);
		FOR(i,0,n)
			scanf("%s",&a[i]);
		FOR(i,0,n)
		{
			int cnt=0;
			FOR(j,0,n)
				if (a[i][j]!='.')
					cnt++;
			double wp;
			int cnt1=0,cnt2=0;
			FOR(j,0,n)
			{
				if ((a[i][j]=='0') || (a[i][j]=='1'))
					cnt2++;
				if (a[i][j]=='1')
					cnt1++;
			}
			wp=cnt1/(double)cnt2;
			double owp=0;
			FOR(j,0,n)
			{
				if (j==i)
					continue;
				if (a[i][j]=='.')
					continue;
				int cnt1=0,cnt2=0;
				FOR(k,0,n)
				{
					if (k!=i)
					{
						if ((a[j][k]=='0') || (a[j][k]=='1'))
							cnt2++;
						if (a[j][k]=='1')
							cnt1++;
					}
				}
				owp+=(cnt1/(double)cnt2);
			}
			owp/=cnt;
			double oowp=0;
			FOR(it,0,n)
			{
				if (a[i][it]=='.')
					continue;
				int c=0;
				FOR(j,0,n)
					if (a[it][j]!='.')
						c++;
				double owp=0;
				FOR(j,0,n)
				{
					if (j==it)
						continue;
					if (a[it][j]=='.')
						continue;
					int cnt1=0,cnt2=0;
					FOR(k,0,n)
					{
						if (k!=it)
						{
							if ((a[j][k]=='0') || (a[j][k]=='1'))
								cnt2++;
							if (a[j][k]=='1')
								cnt1++;
						}
					}
					owp+=(cnt1/(double)cnt2);
				}
				owp/=c;
				oowp+=owp;
			}
			oowp/=cnt;
			double res=0.25*wp+0.5*owp+0.25*oowp;
			printf("%.10lf\n",res);
		}
	}
	return 0;
}