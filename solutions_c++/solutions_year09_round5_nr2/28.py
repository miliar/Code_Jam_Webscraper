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
#include <sstream>
#include <cstring>
#include <iomanip>
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
#define INF 100000007
#define MOD 10009
template <class Ty, class Tx>
Ty cast(const Tx &x) {
	 Ty y; stringstream ss(""); ss<<x; ss.seekg(0); ss>>y; return y;
}


string pol;
int T,K,n;
string dic[10007];

inline vi operator+(const vi& a,const vi& b){
	vi res(a.size());
	REP(i,a.size()) res[i]=a[i]+b[i];
	return res;
}



map<vi, int> M[13];
vi war[100007];

vi go(string il){
	int m=il.size();
	REP(i,n){
		war[i]=vi(m,0);
		FORE(j,dic[i]) REP(k,m)
			if(*j == il[k])
				war[i][k]++;
	}
	vi res;
	REP(i,13) M[i].clear();
	M[0][vi(m,0)]=1;
	FOR(k,1,K){
		FORE(i,M[k-1]) REP(j,n){
			vi nowy=i->xx+war[j];
			M[k][nowy]= (M[k][nowy] + i->yy)%MOD;
		}
		int odp=0;
		FORE(i,M[k]){
			int ak=1;
			FORE(j,i->xx) {ak*=*j; ak%=MOD;}
			odp=(odp+ak*i->yy)%MOD;
		}
		res.PB(odp);
	}
	return res;
}

int main(){
	cin >> T;
	FOR(cas,1,T){
		//in
		cin >> pol >> K;
		cin >> n;
		REP(i,n) cin >> dic[i];
		//rozw
		FORE(i,pol) if(*i == '+') *i=' ';
		stringstream ss(pol);
		string s;
		vi res(K,0);
		while(ss >> s){
			if(s == "") continue;
			vi v=go(s);
			REP(i,K) {res[i]+=v[i]; res[i]%=MOD;}
		}
		///out
		cout << "Case #" << cas << ": ";
		FORE(i,res) cout << *i << " ";
		cout << endl;
	}
	return 0;
}
