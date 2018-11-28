// Marek Rogala; Code Jam 2009
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
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

int const MAXN=1000000;
string welcome="welcome to code jam";

int gotLetter[19];

void zrob(int t){
	REP(i,19) gotLetter[i]=0;
	char c=getchar();
	while(c!='\n'&&c!=EOF){
		if(c==welcome[0]) gotLetter[0]++;
		for(int i=1;i<welcome.length();i++){
			if(c==welcome[i]) gotLetter[i]+=gotLetter[i-1];
		}
		REP(i,welcome.length()) gotLetter[i]%=1000;
		c=getchar();
	}
	printf("Case #%d: %04d\n",t,gotLetter[welcome.length()-1]);
}

int main() {
	int T; scanf("%d\n",&T); FOR(i,1,T) zrob(i);
	return 0;
}


