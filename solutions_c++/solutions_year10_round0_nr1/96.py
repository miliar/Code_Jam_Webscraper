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

LL mypow(int a, int b){
	LL sol = 1;
	REP(i,b) sol*=a;
	return sol;
}

void run1(int caso){
	LL N,K;
	cin >> N >> K;
	if(((K+1)%mypow(2,N))==0)
		cout << "Case #"<<caso<<": "<< "ON"<<endl;
	else cout << "Case #"<<caso<<": "<< "OFF"<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}