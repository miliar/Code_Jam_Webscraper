#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional> 
#include <numeric>
using namespace std;
#define foreach(i,v) for(__typeof((v).end()) i=(v).begin();i!=(v).end();++i)
#define rforeach(i,v) for(__typeof((v).rend()) i=(v).rbegin();i!=(v).rend();++i)
#define FOR(i,b,e) for(int i=(b);i<(e);++i)
#define FORE(i,b,e) for(int i=(b);i<=(e);++i)
typedef long long LL;

int main(){
	int T;
	cin >> T;
	FORE(z,1,T){
		LL n, k;
		cin >> n >> k;
		bool on = true;
		FOR(i,0,n)
			if (!(k&(1LL<<i))) on = false;
		printf("Case #%d: %s\n",z,on?"ON":"OFF");
	}
	return 0;
}
