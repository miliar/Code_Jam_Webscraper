#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

int64 pow2(int64 x) { return x*x; }

int main(void) {
	int n; SC(&n);

	FOR(_i,n) {
		int64 n,A,B,C,D,x0,y0,M;
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		vector<pI> points;
		FOR(i,n) {
			points.push_back(make_pair((int)x0,(int)y0));		
			x0 = (A*x0 + B) % M;
			y0 = (C*y0 + D) % M;
		}

		int64 div[3][3]={0};
		FOR(i,n) {
			div[points[i].first % 3][points[i].second % 3]++;
		}
		
		int64 res = 0;
		FOR(i0,3) FOR(j0,3) FOR(i1,3) FOR(j1,3) FOR(i2,3) FOR(j2,3) {
		if ((i0+i1+i2)%3 || (j0+j1+j2)%3) continue;
			int64 x = div[i0][j0];
			int64 y = div[i1][j1];
			if (i1==i0 && j1==j0) --y;
			int64 z = div[i2][j2];
			if (i2==i0 && j2==j0) --z;
			if (i2==i1 && j2==j1) --z;
			if (x<=0 || y<=0 || z<=0) continue;
			
			res += x*y*z;
		}

		printf("Case #%d: %lld\n", _i+1, res/6);
	}
	return 0;
}
