#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
#define MAXN 1010

int X,S,R;

int n,d;
pair<int,int> parts[MAXN];

double remain;
double ans;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int caseN;
	scanf("%d",&caseN);
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		scanf("%d%d%d%lf%d",&X,&S,&R,&remain,&n);
		for (int i=0;i<n;i++)
		{
			int b,e,w;
			scanf("%d%d%d",&b,&e,&w);
			parts[i]=make_pair(w+S,e-b);
			X-=e-b;
		}
		parts[n++]=make_pair(S,X);
		sort(parts,parts+n);
		d=R-S;
		ans=0;
		for (int i=0;i<n;i++)
		{
			double tneed=parts[i].second*1.0/(parts[i].first+d);
			if (tneed<=remain)
			{
				remain-=tneed;
				ans+=tneed;
			}
			else
			{
				double run_len=remain*(parts[i].first+d);
				double rest_time=(parts[i].second-run_len)/parts[i].first;
				ans+=remain+rest_time;
				remain=0;
			}
//			cerr<<parts[i].first<<' '<<parts[i].second<<' '<<ans<<endl;
		}
		printf("Case #%d: %.8lf\n",caseI,ans);
	}
	return 0;
}
