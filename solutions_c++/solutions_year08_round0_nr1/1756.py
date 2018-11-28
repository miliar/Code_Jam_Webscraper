#include <map>
#include <cmath>
#include <vector>
#include <numeric>
#include <sstream>
#include <iostream>
using namespace std ;

#define PI 3.14159265358
#define pb push_back
#define LOOP(i,a,b) for (int i=a; i<b; i++)
#define FOR(i,n) LOOP(i,0,n)
#define REP(i,n) LOOP(i,1,n)
#define fill(f,n,v) FOR(i,n) f[i]=v
#define sz(a) (int)a.size()

int main() {
	const int INF = 100000;
	int N, Q, S;
	string q[1001], s[101]; 
	int f[1001][101];
	
	//input
	cin >> N;
	FOR(n,N) {
		
		//input
		cin >> S;
		getline(cin, s[0]);
		FOR(i,S) getline(cin, s[i]);
		
		cin >> Q;
		getline(cin,q[0]);
		FOR(i,Q) getline(cin, q[i]);
			
		if(Q == 0) {
			cout <<"Case #" << (n+1) << ": 0" << endl;
			continue;
		}
		
		
		FOR(i,Q) FOR(j,S) f[i][j] = INF;
		int bIn = 0;
		FOR(i,S) if(s[i] != q[0]) f[0][i] = 0, bIn = i;	
		
		REP(i,Q) {
			int bIn1 = 0;
			FOR(j,S) {
				if(q[i] == s[j]) continue;
				
				if(j==bIn) f[i][j] = f[i-1][j];
				else f[i][j] = min(f[i-1][j], f[i-1][bIn]+1);
				if(f[i][j] < f[i][bIn1]) bIn1 = j;
			}
			bIn = bIn1;
		}
		int res = INF;
		FOR(i,S) res = min(res, f[Q-1][i]);
		
		//output
		cout << "Case #" << (n+1) << ": " << res << endl; 
		
	}
	return 0;
}