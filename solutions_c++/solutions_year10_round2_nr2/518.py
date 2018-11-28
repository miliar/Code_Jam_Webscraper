#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const int Max=60;

set<string> s;

int main(int argc, char **argv)
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int c;
	scanf("%d", &c);
	for(int icase=0; icase<c; icase++){
		long long  n, k, b, t;
		long long x[Max], v[Max]; 
		long long ret;

		scanf("%lld%lld%lld%lld", &n, &k, &b, &t);
		
		for(long long  i=0; i<n; i++){
			scanf("%lld", x+i);
		}
		for(long long  i=0; i<n; i++){
			scanf("%lld", v+i);
		}

		ret=k;
		long long j=n-1;
		
		long long ans=0;

		while( ret>0 && j>=0){
			if(x[j]+v[j]*t<b){
				ans+=ret;
			}else{
				--ret;
			}
			--j;
		}
		if(j<0&&ret>0){
			printf("Case #%d: IMPOSSIBLE\n", icase+1);
		}else{
			printf("Case #%d: %d\n", icase+1, ans);
		}
	}

	return 0;
}