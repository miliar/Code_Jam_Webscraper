#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_##i=(b);i<_##i;++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define MP          make_pair
#define S           size()
typedef long long   LL;

int main(){
	//freopen("a.in", "r", stdin);
	//freopen("C-small-attempt0.in","r",stdin); freopen("C-small-attempt0.out","w",stdout);
	freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);
	int t, n;
	scanf("%d", &t);
	for(int cas=1; cas<=t ;cas++){
		scanf("%d", &n);
		vector<int> v(n);
		LL tot = 0LL, sum = 0LL;
		F(i, n){
			scanf("%d", &v[i]);
			tot ^= LL(v[i]);
			sum += LL(v[i]);
		}
		if(tot != 0LL) printf("Case #%d: NO\n", cas);
		else{
			sort(ALL(v));
			printf("Case #%d: ", cas);
			cout<<(sum-LL(v[0]))<<endl;
		}
	}
}

