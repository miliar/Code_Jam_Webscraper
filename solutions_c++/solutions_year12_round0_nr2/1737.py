// Marek Rogala; Code Jam 2012
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

int n,s,p,x;

bool check(int sum, int d1,int d2){
  return (sum+d1+d2)%3==0&&(sum+d1+d2)/3>=p&&(sum+d1+d2)/3-max(d1,d2)>=0;
}

void zrob(int testcase){

  int notsupr_cnt=0, supr_cnt=0, both_cnt = 0;

  cin >> n >> s >> p;
  REP(i,n){
    cin >> x;
    bool a = check(x,0,0)||check(x,1,0)||check(x,1,1);
    bool b = check(x,2,1)||check(x,2,2)||check(x,2,0);
    if(a&&b) both_cnt++;
    else if(a) notsupr_cnt++;
    else if(b) supr_cnt++;
  }

  int s1 = 0, s3 = 0;
  s1 = min(supr_cnt, s);
  s -= s1;
  s3 = both_cnt + notsupr_cnt;


	cout << "Case #"<<testcase<<": "<< s1+s3<<endl;
}

int main() {
  ios_base::sync_with_stdio(0);
	int T; cin >> T;
	for(int i=1;i<=T;i++) zrob(i);
	return 0;
}

