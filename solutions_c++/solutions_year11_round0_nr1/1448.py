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
	//freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);
	int t, n, a, b, r, x, ta, tb;
	char ch;
	scanf("%d", &t);
	for(int cas=1; cas<=t ;cas++){
		scanf("%d", &n);
		a = b = 1;
		ta = tb = r = 0;
		F(i, n){
			cin>>ch>>x;
			if(ch == 'O'){//a
				if(r-ta >= abs(x-a)) r++;
				else r += (abs(x-a) - (r-ta)) + 1;
				a = x;
				ta = r;
			}
			else{//b
				if(r-tb >= abs(x-b)) r++;
				else r += (abs(x-b) - (r-tb)) + 1;
				b = x;
				tb = r;
			}
		}
		printf("Case #%d: %d\n", cas, r);
	}
}

