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

int solve(int n, vector<pair<int,int> > v) {
	sort(ALL(v));
	int r = 0;
	F(i, n){
		FOR(j, 0, i){
			if(v[j].second > v[i].second)
				r++;
		}
	}
	return r;
}

int main() {
//	freopen("a.in", "r", stdin);
//	freopen("C:/Users/vudduu/Downloads/A-small-attempt3.in", "r", stdin);
//	freopen("C:/Users/vudduu/Downloads/A-small-attempt3.out", "w", stdout);
	freopen("C:/Users/vudduu/Downloads/A-large.in", "r", stdin);
	freopen("C:/Users/vudduu/Downloads/A-large.out", "w", stdout);
	int NN;
	scanf("%d", &NN);
	for (int caso=1; caso<=NN ;caso++) {
		printf("Case #%d: ", caso);
		int n;
		scanf("%d", &n);
		vector<pair<int,int> > v(n);
		F(i, n){
			cin>>v[i].first>>v[i].second;
		}
		cout<<solve(n, v)<<endl;
	}
}
