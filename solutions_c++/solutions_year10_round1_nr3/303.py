#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;

#define sz(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define pb push_back
#define pii pair<int,int>
#define inf (1<<25)
#define infL 10000000000000000LL
#define F first
#define S second
#define all(x) x.begin() , x.end()

int a1,b1,a2,b2;
map<pii ,int> g[2];

int ganha1(int a, int b);

int ganha2(int a, int b) {
	if(a > b) swap(a,b);
	if(g[1].count( pii(a,b) ))
		return g[1][ pii(a,b) ];
	if(a == b) return 0;
	if(b % a == 0) return 1;

	int r = 0;

	for(int i=1; ;i++) {
		if(a*i >= b) break;
		if(ganha1(a, b-a*i)) continue;
		else { r = 1; break; }
	}

	return g[1][ pii(a,b) ] = r;
}




int ganha1(int a, int b) {
	if(a > b) swap(a,b);
	if(g[0].count( pii(a,b) ))
		return g[0][ pii(a,b) ];
	if(a == b) return 0;
	if(b % a == 0) return 1;

	int r = 0;

	for(int i=1; ;i++) {
		if(a*i >= b) break;
		if(ganha2(a, b-a*i)) continue;
		else { r = 1; break; }
	}

	return g[0][ pii(a,b) ] = r;
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(t,T) {
		printf("Case #%d: " , t+1);
		cin >> a1 >> a2 >> b1 >> b2;
		
		int r = 0;
		g[0].clear();
		g[1].clear();
		for(int a = a1; a <= a2; a++)
			for(int b = b1; b <= b2; b++) {
				if(ganha1(a,b)) r++;
			}
		cout << r << endl;
	}

    return 0;
}

