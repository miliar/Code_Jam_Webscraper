#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<sstream>
#include<queue>
#include<string>
#include<cmath>

using namespace std;

#define pb push_back
#define re return
#define sf scanf
#define pf printf

struct node {
	int a, b;
};

vector<node> V;

int main() {
	int t, i, j;
	int cases = 1;
	sf("%d", &t);
	while(t--) {
		int n;
		sf("%d", &n);
		V.clear();
		int i;
		for(i=0;i<n;i++) {
			node A;
			cin >> A.a >> A.b;
			V.pb(A);
		}
		int result = 0;
		for(i=0;i<n;i++)
		 for(j=i+1;j<n;j++){
			if( V[i].a > V[j].a && V[i].b < V[j].b ) result++;
			else if( V[i].a < V[j].a && V[i].b > V[j].b ) result++;
		 }
		pf("Case #%d: %d\n", cases++, result);
	}
	return 0;
}
