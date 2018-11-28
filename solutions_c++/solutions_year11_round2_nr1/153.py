#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <ctime>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000
#define maxn 1000000

//typedef long long  LL;
//typedef __int64 LL;

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;


char game[105][105];
double ans[205],wp[205],owp[205],oowp[205];

int main()
{
	int i,j,k,tests,cs=0,n;


	freopen("E:\\GCJ\\A-large.in","r",stdin);
	freopen("E:\\GCJ\\Alarge.out","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{

		cin>>n;
		for(i=0;i<n;i++)
		{
			scanf("%s",game[i]);
			ans[i]=0.0;
		}

		for(i=0;i<n;i++)
		{
			double tot=0.0;

			owp[i]=0.0;

			for(j=0;j<n;j++)
			{
				if(game[i][j]=='.') continue;

				double cnt=0.0,w=0.0;

				for(k=0;k<n;k++)
				{
					if(game[j][k]=='.' || k==i) continue;
					cnt++;
					if(game[j][k]=='1') w++;
				}
				tot++;
				//printf("%lf %lf\n",w,cnt);
				owp[i]+= w/cnt;
			}
			owp[i]/=tot;
		//	break;
		}

		for(i=0;i<n;i++)
		{
			double wp=0.0,oowp=0.0,tot=0.0;

			for(j=0;j<n;j++)
			{
				if(game[i][j]=='.') continue;
				tot++;
				if(game[i][j]=='1') wp++;
				oowp+=owp[j];
			}
			wp/=tot;
			oowp/=tot;
			//printf("%lf %lf %lf\n",wp,owp[i],oowp);
			ans[i]=0.25*wp + 0.50*owp[i] + 0.25 *oowp;
		}

		//for(i=0;i<n;i++)
			//printf("%lf\n",owp[i]);

		printf("Case #%d:\n",++cs);
		for(i=0;i<n;i++)
			printf("%.9lf\n",ans[i]);
	}

	return 0;
} 


