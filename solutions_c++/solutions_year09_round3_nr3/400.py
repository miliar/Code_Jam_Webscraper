#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <queue>
#include <list>
#include <vector>
#include <cmath>

#define REP(i,n) for (int i = 0; i < n; i++)
#define FOR(i,n,m) for (int i = n; i <= m; i++)
#define FORD(i,n,m) for (int i = n; i >= m; i--)
#define FOREACH(a,c) for (typeof((c).begin()) a = (c).begin(); a != (c).end(); a++)

typedef long long int LL;
//typedef set<int> SI;
//typedef list<int> LI;
using namespace std;
int table[10000];
int solve(int begin, int end, int B, int E){
	if (B==E || begin == end)
		return 0;
	int mini = 99999999;
	FOR(i,B,E-1){
		mini = min(mini, solve(begin, table[i]-1, B, i) + solve(table[i], end, i+1, E) + end-begin-1); 
	}
//	printf ("%d %d %d %d %d\n", begin, end, B, E, mini);
	return mini;
}
int T;

int main(){
	scanf ("%d", &T);
	REP(x,T){
		int P, Q;
		scanf ("%d %d", &P, &Q);
		REP(i,Q)
			scanf ("%d", &table[i]);
		printf ("Case #%d: %d\n", x+1, solve(0, P, 0, Q));
	}
	return 0;
}
