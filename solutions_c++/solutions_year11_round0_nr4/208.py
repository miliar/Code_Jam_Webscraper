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
#define debug(x) cerr << #x << " = " << (x) << "\n"
typedef long long LL;

int main(){
	int t;
	cin >> t;
	FORE(z,1,t){
		int n;
		cin >> n;
		int diff=0, x;
		FORE(i,1,n)
			cin >> x, diff+=(x!=i);
		printf("Case #%d: %d\n",z,diff);
	}
	return 0;
}
