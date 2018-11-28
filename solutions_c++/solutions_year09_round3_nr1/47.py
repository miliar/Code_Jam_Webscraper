// Marek Rogala; Code Jam 2009
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define SIZE(x) ((int)x.size())
int COND = 1;
#define DB(x) { if (COND > 0) { COND--; REP (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 
typedef pair<int,int> PII;
typedef vector<PII> VPII;

int digit[260];
char msg[65];

void zrob(int testcase){
	for(int i=0;i<260;i++){
		digit[i]=-1;
	}	
	scanf("%s",msg);
	int n = strlen(msg);

	unsigned long long result = 0;
	int nextDigit=1;
	int base = 2;
	for(int i=0;i<n;i++){
		if(digit[msg[i]] == -1){
			digit[msg[i]] = nextDigit;
			if(nextDigit == 1){
				nextDigit = 0;
			} else if(nextDigit == 0){
				nextDigit = 2;
			} else {
				nextDigit++;
			}
		}
		base = max(base, digit[msg[i]]+1);
	}
	for(int i=0;i<n;i++){
		result*=base;
		result += digit[msg[i]];
	}
	cout << "Case #" << testcase <<": "<<result<<endl;
}

int main() {
	int T; scanf("%d", &T); 
	for(int i=1;i<=T;i++) zrob(i);
	return 0;
}


