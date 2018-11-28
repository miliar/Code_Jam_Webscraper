#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()

string solve(int n, int k){
	if(k == 0) return "OFF";
	n = (1<<n)-1;		
	if((n&k) == n)
		return "ON";
	else
		return "OFF";
}

int main() {
//	freopen("a.in", "r", stdin);
//	freopen("A-small.in", "r", stdin);
//	freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int n;
	scanf("%d", &n);
	F(caso, n){
		printf("Case #%d: ", caso+1);
		int a, b;
		scanf("%d %d", &a, &b);
		cout<<solve(a, b)<<endl;
	}
}
