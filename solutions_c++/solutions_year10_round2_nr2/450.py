#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<cmath>
#include<string>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<utility>
#include<list>
#include<set>
#include<map>
 
using namespace std;

#define eps 1e-9
#define INF INT_MAX
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).end(),(v).begin()
#define mp make_pair
#define pb push_back

#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define CLEAR(t) memset((t),0,sizeof(t))

typedef pair < int, int > pii;
typedef long long LL;
int N, K, B , T;

bool puede(pii chick){
	return ((B - chick.first)/(chick.second*1.0)) < (T*1.0+eps);
}

void run1(int caso){
	cin >> N>>K>>B>>T;
	vector<pii> val(N);
	
	REP(i,N) cin >> val[i].first;
	REP(i,N) cin >> val[i].second;
	
	int win = 0, cont = 0, loose=0;
	int ind = N-1;
	while(ind>=0 && win<K){
		if(puede(val[ind])) {
			cont+=loose;
			win++;
		}
		else loose++;
		ind--;
	}
	if(win>=K)
		cout << "Case #"<<caso<<": "<< cont<<endl;
	else cout << "Case #"<<caso<<": "<< "IMPOSSIBLE"<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}