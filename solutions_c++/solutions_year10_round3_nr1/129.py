#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cctype>
#include<cmath>

#define FOR(i,a,b) for(int i=(a),_n=(b); i<=_n; i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_n=(b);i>=_n; i--)
#define FILL(i,v) memset((i),(v),sizeof((i)))
#define DEBUG(x) cout <<"  >> "<<#x<<" => "<<x <<endl
#define ABS(x) ((x<0) ? –x : x)
#define ALL(x) x.begin(),x.end()
#define MAX(a,b) ((a<b) ? b : a)
#define MIN(a,b) ((a<b) ? a : b)
#define MP make_pair
#define PB push_back
#define INF 1000000000


using namespace std;
typedef long long LL;
const double EPS = 1.e-9;

void OPEN(string name) {
	string in = name + ".in";
	freopen(in.c_str(), "r", stdin);
	string out = name + ".out.txt";
	freopen(out.c_str(), "w", stdout);
}

int A[1002], B[1002];

int main() {
	OPEN("Alarge");
	int ntc;
	scanf("%d", &ntc);
	for(int TC=1, N; TC <= ntc; TC++) {
		scanf("%d", &N);
		for(int i=0; i<N; i++) scanf("%d %d", &A[i], &B[i]);
		int ans = 0;
		for(int i=0; i<N; i++) {
			for(int k=i+1; k<N; k++) {
				if ( A[i] < A[k] ) {
					if ( B[i] > B[k] ) ans++;
				} else {
					if ( B[i] < B[k] ) ans++;
				}
			}
		}
		printf("Case #%d: %d\n", TC, ans);
	}
	return 0;
}
