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

int N,A[1000],B[1000];

int main() {
	int yay=0,cnt;
	for (int _=GI;_--;) {
		N=GI;
		REP (i,N) A[i]=GI,B[i]=GI;
		if(N==1) printf("Case #%d: 0\n",++yay);
		else {
			cnt=0;
			REP (i,N) FOR (j,i+1,N) {
				if(A[i]<A[j]) {
					if(B[i]>B[j]) cnt++;
				}
				else {
					if(B[i]<B[j]) cnt++;
				}
			}
			printf("Case #%d: %d\n",++yay,cnt);
		}
	}
	return 0;
}

