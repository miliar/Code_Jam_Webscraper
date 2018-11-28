#include<cstdio>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<sstream>
#include<cmath>
#include<cctype>
#include<cassert>
#include<cstring>
#include<cstdlib>

using namespace std;

#define pf printf
#define sf scanf
#define VI vector<int>
#define pb push_back
#define fo(a,b) for((a)=0;(a)<(b);a++)

#define debug 0
const int inf = 1000000000;

long long ncr[305][305] = {0}; void gen_ncr(int n) { int i, j; fo(i, n+1) ncr[i][0] = 1; for(i=1;i<=n;i++) for(j=1;j<=n;j++) ncr[i][j] = ncr[i-1][j] + ncr[i-1][j-1];}
double dis(double x1, double y1, double x2, double y2) { return sqrt( (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)); }

int flag[10001];
int F;
VI D, L;
bool yes;
int n;
struct node {
	int u;
	int s;
};

void dfs(int u,int s) {


	queue<node> Q;
	int i;
	while( !Q.empty() ) Q.pop();
	node A;
	A.u = u;
	A.s = s;
	Q.push(A);
	//for(i=0; i<n; i++) flag[i] = 0;
	int last = 0;
	while(!Q.empty()) {
		node A = Q.front();
		Q.pop();
		if( D[A.u] + A.s >= F ) yes = true;
		if( yes ) continue;
		//cout << A.u << " " << A.s << endl;;
	//	cin >> i;
		for(i=last+1; i<n; i++) {
			if( D[ A.u ] + A.s >= D[i] ) {
				int ss;
				if( D[i] - D[ A.u ] >= L[i] ) ss = L[i];
				else ss = D[i] - D[A.u];
				node T;
				T.u = i;
				T.s = ss;
				Q.push(T);
			}
			else break;

		}
		last = i-1;
	}

}

int main() {
	int test, cases = 1;
	cin >> test;

	for( cases=1; cases<=test; cases++ ) {
		D.clear(); L.clear();
		cin >> n;
		int i, j;
		for(i=0; i<n; i++) {
			int a, b;
			cin >> a >> b;
			D.pb(a); L.pb(b);
		}
		yes = false;
		cin >> F;

		dfs(0, D[0]);

		pf("Case #%d: ", cases);
		if( yes) pf("YES");
		else pf("NO");
		cout << endl;
	}
	return 0;
}
