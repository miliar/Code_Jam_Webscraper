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

int solve(int n, int m, vector<string> a, vector<string> b) {
	set<string> s;
	F(i, n){
		while(a[i] != "/" && a[i].S){
			s.insert(a[i]);
			int it = a[i].S-1;
			while(a[i][it] != '/') it--;
			a[i] = a[i].substr(0, it);
		}
	}
	int r = s.S;
	F(i, m){
		while(b[i] != "/" && b[i].S){
			s.insert(b[i]);
			int it = b[i].S-1;
			while(b[i][it] != '/') it--;
			b[i] = b[i].substr(0, it);
		}
	}
	return s.S-r;
}

int main() {
//	freopen("a.in", "r", stdin);
//	freopen("C:/Users/vudduu/Downloads/A-small-attempt0.in", "r", stdin);
//	freopen("C:/Users/vudduu/Downloads/A-small-attempt0.out", "w", stdout);
	freopen("C:/Users/vudduu/Downloads/A-large.in", "r", stdin);
	freopen("C:/Users/vudduu/Downloads/A-large.out", "w", stdout);
	int NN;
	scanf("%d", &NN);
	for (int caso=1; caso<=NN ;caso++) {
		printf("Case #%d: ", caso);
		int N, M;
		scanf("%d %d", &N, &M);
		vector<string> a(N), b(M);
		F(i, N){
			cin>>a[i];
		}
		F(i, M){
			cin>>b[i];
		}
		cout<<solve(N, M, a, b)<<endl;
	}
}
