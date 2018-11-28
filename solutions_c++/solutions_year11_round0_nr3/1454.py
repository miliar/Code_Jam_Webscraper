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

using namespace	std;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

int n,v[1001];

int main()
{
	freopen("c.txt","rt",stdin);
	freopen("c.out","wt",stdout);
	int r,t;
	scanf("%d",&t);
	rep(tt,0,t){
		scanf("%d",&n);
		rep(i,0,n){
			scanf("%d",&v[i]);
			if(i==0)
				r=v[i];
			else
				r^=v[i];
		}
		printf("Case #%d: ",tt+1);
		if(r!=0){
			printf("NO\n");
		}
		else{
			sort(v,v+n,greater<int>());
			int res=0;
			rep(i,0,n-1)
				res+=v[i];
			printf("%d\n",res);
		}
	}

	return 0;
}
