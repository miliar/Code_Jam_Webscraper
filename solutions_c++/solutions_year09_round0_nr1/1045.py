#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <algorithm>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)
#define FORE(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n";
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset(x,0,sizeof x)
#define xx first
#define yy second
typedef long long int lli;
typedef pair<int, int> P;
typedef vector<int> vi;
#define MAXN 5007

int L,N,D;
string dic[MAXN],pat;

bool ok(string pat,string wor){
//	cout << "OK" << pat << " " << wor << endl;
	int pos=0;
	FORE(i,wor){
		if(pat[pos] != '('){
			if(pat[pos] != *i) return false;
			pos++;
			continue;
		}
		while(pat[pos] != *i){
			if(pat[pos] == ')') return false;
			pos++;
		}
		while(pat[pos] != ')') pos++;
		pos++;
	}
	return true;
}

int main(){
	//in
	cin >> L >> D >> N;
	REP(i,D) cin >> dic[i];
	FOR(cas,1,N){
		cin >> pat;
		int res=0;
		REP(i,D) if(ok(pat, dic[i])) res++;
		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}
