#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <complex>
#include <climits>
#include <queue>
#include <ctime>

using namespace std;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (int)(n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

int a[10001];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
#endif
	int t,n;
	scanf("%d",&t);
	rep(tt,0,t)
	{
		scanf("%d",&n);
		rep(i,0,n)
			scanf("%d",&a[i]);
		vector<pair<int,int> >v;
		rep(i,1,(1<<n))
		{
			int x = 0;
			rep(j,0,n)
				if(i&(1<<j))
					x+=a[j];
			v.push_back(make_pair(x,i));
		}
		printf("Case #%d:\n",tt+1);
		sort(ALL(v));
		rep(i,1,v.size())
			if(v[i].first==v[i-1].first)
			{
				char*ss="";
				rep(j,0,n)
					if(v[i].second&(1<<j))
						printf("%s%d",ss,a[j]),ss=" ";
				printf("\n");
				ss="";
				rep(j,0,n)
					if(v[i-1].second&(1<<j))
						printf("%s%d",ss,a[j]),ss=" ";
				printf("\n");
				break;
			}
	}
	return 0;
}
