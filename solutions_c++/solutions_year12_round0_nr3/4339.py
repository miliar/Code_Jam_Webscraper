#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <stack>
#include <utility>
#include <cstdlib>
#include <climits>
using namespace std;

#define REP(i, n) for(typeof(n) i=0;i<(n);++i)
#define FOR(i,a,b) for(typeof(b) i=a;i<=b;++i)
#define FORD(i,a,b) for(typeof(b) i=a;i>=b;--i)
#define SZ(x) ((int)((x).size()))
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define foreach(it, c)for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define present(c,x) (find(all(c),x) != (c).end()) 
bool isRecycled(int n, int m) {
	if (n == m) return false;
	char nn[10],mm[10];
	sprintf(nn,"%d",n);
	sprintf(mm,"%d",m);
	string N = string(nn);
	string M = string(mm);
	REP(i,N.size()-1) {
		string temp= N.substr(N.size()-1-i,i+1);
		string temp2 = N.substr(0,N.size()-i-1);
		if (temp+temp2 == M) return true;
	}
	return false;
}
int main() {
	// freopen("C-small-attempt0.in","r",stdin);
	// freopen("out","w",stdout);
	int T;
	cin >> T;
	REP(t,T) {
		int a,b;
		cin >> a>>b;
		int cnt=0;
		for (int i=a;i<b;i++) {
			for (int j=i;j<=b;j++) {
				if (isRecycled(i,j)) cnt++;
			}
		}
		printf("Case #%d: %d\n",t+1,cnt);
	}
	return 0;
}


