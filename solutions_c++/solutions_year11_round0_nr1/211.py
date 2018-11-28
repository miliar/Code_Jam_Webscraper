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
		int pos[500];
		pos['B']=pos['O']=1;
		char cur='B';
		int time = 0, buf = 0;
		FOR(i,0,n){
			char c;
			int np;
			cin >> c >> np;

			int save=0;
			if (cur!=c) save=buf, buf=0;
			int taken = max(abs(np-pos[c])-save,0)+1;
			time += taken;
			buf += taken; 
			pos[c] = np;
			cur = c;
//			printf("time %d buf %d use %d save %d cur %c pos %d %d\n",time,buf,taken,save,cur,pos['B'],pos['O']);
		}
		printf("Case #%d: %d\n",z,time);
	}
	return 0;
}
