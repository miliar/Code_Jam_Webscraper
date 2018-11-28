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
	//freopen("A-small-attempt2.in","r",stdin); freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);
	int t;
	scanf("%d", &t);
	for(int cas=1; cas<=t ;cas++){
		printf("Case #%d: ", cas);
		LL n, pd, pg;
		cin>>n>>pd>>pg;
		bool flag = false;
		if(pg == 100LL){
			if(pd == 100LL) flag = true;
		}
		else if(pg == 0LL){
			if(pd == 0LL) flag = true;
		}
		else if(pd == 0LL){
			flag = true;
		}
		else{
			for(int i=1; i<=pd && i<=n ;i++){
				if(LL(i * 100) % pd == 0){
					LL aux = (i*100LL) / pd;
					if(aux <= n){
						 flag = true;
						break;
					}
				}
			}
		}
		if(flag) printf("Possible\n");
		else printf("Broken\n");
	}
}

