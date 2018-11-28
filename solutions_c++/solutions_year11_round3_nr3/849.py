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

vector<int> v;

bool cumple(int val){
	REPSZ(i,v){
		if(val>v[i]){
			if((val%v[i])!=0) return false;
		}else{
			if((v[i]%val)!=0) return false;
		}
	}
	return true;
}

void run1(int caso){
	int N,L,H;
	cin >> N>>L>>H;
	v.clear();

	REP(i,N){
		int a;
		cin >>a;
		v.pb(a);
	}
	int sol=-1;
	FORE(i,L,H){
		if(cumple(i)) {
			sol = i;
			break;
		}
	}
	if(sol==-1) cout << "Case #"<<caso<<": "<< "NO"<<endl;
	else cout << "Case #"<<caso<<": "<< sol<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}
