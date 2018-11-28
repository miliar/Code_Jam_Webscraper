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
#include <assert.h>

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
vector<pnt > b;
vector<int> a;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(test,1,t+1)
	{
		printf("Case #%d: ",test);
		int n;
		scanf("%d",&n);
		a.clear();
		b.clear();
		a.resize(n);
		FOR(i,0,n)
			scanf("%d",&a[i]);
		sort(a.begin(),a.end());
		FOR(i,0,n)
		{
			sort(b.begin(),b.end());
			bool f=false;
			FOR(j,0,b.size())
				if (b[j].second==a[i]-1)
				{
					b[j].first++;
					b[j].second=a[i];
					f=true;
					break;
				}
			if (!f)
				b.push_back(mp(1,a[i]));
		}
		int res=2000000000;
		FOR(i,0,b.size())
			res=MIN(res,b[i].first);
		if (res==2000000000)
			res=0;
		printf("%d\n",res);
	}
	return 0;
}