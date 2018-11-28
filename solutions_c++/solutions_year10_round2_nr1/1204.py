#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t;scanf(" %d",&t);t;})
#define GC(x) scanf(" %c",&x)
#define sz size()
#define rz resize
#define cl clear()
#define inf (int)1e9
#define pb push_back
#define bs binary_search
#define lb lower_bound
#define ub upper_bound

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double DD;
typedef long long LL;

int N,M;
set <string> test;

int main() {	
	string temp,fin;
	int p,yay=0,cnt;
	for (int _=GI;_--;) {
		test.cl;
		N=GI;
		M=GI;
		REP (i,N) {
			cin>>temp;
			test.insert(temp);
			while(temp.sz>0) {
				while(*(temp.end()-1) != '/') temp.erase(temp.end()-1);
				temp.erase(temp.end()-1);
				test.insert(temp);
			}
		}
		cnt=0;
		N=M;
		REP (j,M) {
			cin>>temp;
			if(test.find(temp)!=test.end()) continue;
			test.insert(temp);
			while(temp.sz>0) {
				cnt++;
				while(*(temp.end()-1) != '/') temp.erase(temp.end()-1);
				temp.erase(temp.end()-1);
				if(test.find(temp)!=test.end()) break;
				test.insert(temp);
			}
		}
		printf("Case #%d: %d\n",++yay,cnt);
	}
	return 0;
}

