#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
using namespace std;

#define MAX(A,B) ((A)>(B)?(A):(B))
#define MIN(A,B) ((A)<(B)?(A):(B))
#define S(X) ((X)*(X))
#define ABS(X) ((X)>0?(X):(-(X)))
#define SZ(X) (int)(X.size())
typedef pair<int,int> PII;
typedef __int64 LL;

bool cmp(PII A, PII B)
{
	return A.second < B.second;
}

int main()
{
//	freopen("A-small-attempt0.in","r",stdin); freopen("A-small-output0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin); freopen("A-small-output1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin); freopen("A-small-output2.out","w",stdout);
	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);

	int T, ks;

	double S,R,t,ans,done,xtra,time_need;
	int N,X;
	int now, sum;
	int bi,ei,wi;
	int i;

	scanf("%d",&T);
	vector<PII> V;
	for(ks=1;ks<=T;ks++)
	{
		V.clear();
		printf("Case #%d: ",ks);

		scanf("%d%lf%lf%lf%d",&X,&S,&R,&t,&N);

		now = 0;
		sum = 0;
		for(i=0;i<N;i++)
		{
			scanf("%d%d%d",&bi,&ei,&wi);

			V.push_back( PII(ei-bi,wi) );
			sum += bi-now;
			now = ei;
		}

		sum += X - now;
		V.push_back( PII(sum, 0) );

		sort(V.begin(),V.end(),cmp);

		ans = 0;
		done = 0;
		for(i=0;i<V.size();i++)
		{
			time_need = V[i].first/(V[i].second + R);
			if(time_need+done <= t)
			{
				done += time_need;
				ans += time_need;
			}
			else
			{
				xtra = t - done;
				done = t;
				ans += xtra + (V[i].first - xtra*(V[i].second+R))/(V[i].second + S);
			}
		}

		printf("%.10lf\n",ans);

	}

	return 0;
}