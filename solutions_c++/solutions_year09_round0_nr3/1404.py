#include<iostream>
#include<valarray>
#include<complex>
#include<bitset>
#include<queue>
#include<stack>
#include<set>
#include<map>
using namespace std;

#define PB(v) push_back(v)
#define PF(v) push_front(v)
#define MP(a,b) make_pair(a,b)
#define SZ(c) ((int)(c).size())
#define BG(c) (c).begin()
#define ED(c) (c).end()
#define BE(c) BG(c),ED(c)
#define TYPE(v) __typeof(v)
#define FORE(i,c) for(TYPE(ED(c))i=BG(c);i!=ED(c);++i)
#define FOR(i,a,b) for(TYPE(b)i(a),_##i(b);i<_##i;++i)
#define REP(i,n) FOR(i,0,n)
#define FORR(i,a,b) for(TYPE(b)i(a),_##i(b);i<=_##i;++i)
#define REPR(i,n) FORR(i,0,n)
#define BOUND(i,a,b) ((i)>=(a)&&(i)<(b))
#define SQR(x) ((x)*(x))
#define LET(var,val) TYPE(val)var=val;

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int>VI;
typedef vector<VI>VVI;
typedef vector<LL>VL;
typedef vector<string>VS;
typedef vector<double>VD;
typedef pair<int,int>pii;
typedef map<int,int>mii;

template<class T>string vtos(const T& v){ostringstream os;os<<v;return os.str();}
template<class T>T stov(const string& s){T v;istringstream(s)>>v;return v;}
template<class T>inline T expn(T a,unsigned n) {T r=1;for(;;a*=a){if(n&1)r*=a;if(!(n>>=1))break;}return r;}
template<class T>inline T gcd(T a,T b){while(b){T r=a%b;a=b;b=r;}return a;}

#define ZPO {o<<'('<<SZ(v)<<"){ ";FORE(i,v)o<<'\"'<<*i<<"\" ";return o<<'}';}
#define ZPP {return o<<'('<<v.first<<','<<v.second<<')';}
#define ZPS(C) template<class T>ostream& operator<<(ostream& o,const C<T>& v)ZPO
#define ZPD(T,P) template<class K,class V>ostream& operator<<(ostream& o,const T<K,V>&v)P
ZPS(vector)ZPS(set)ZPS(deque)ZPD(map,ZPO)ZPD(pair,ZPP)
template<class I>void view(I b,I e,ostream& o=cerr){o<<"{ ";while(b!=e)o<<'\"'<<*b++<<"\" ";o<<"}\n";}
#define DBG(v) cerr<<#v<<" = "<<(v)<<endl;


//real code starts here


string t="welcome to code jam";

void solvecase(string s){
	VVI dp(SZ(s)+2,VI(SZ(t)+2));
	dp[0][0]=1;
	
	REP(i,SZ(s))
	REP(j,SZ(t)){
		if(s[i]==t[j]){
			//dp[i+1][j+1]=dp[k:0..i][j]
			REP(k,i+1)
				dp[i+1][j+1]+=dp[k][j];
				dp[i+1][j+1]%=10000;
		}
	}
	
	int tot=0;
	REP(i,SZ(s)+1){
		//DBG(dp[i][SZ(t)]);
		tot+=dp[i][SZ(t)];
	}
	static int ct=0;
	printf("Case #%d: %04d\n",++ct,tot%10000);
}

void solve(){
	string s;
	while(getline(cin,s)){
		if(s!=""){
			solvecase(s);
		}
	}
	
}

int T;
int main(int argc,char* argv[]){
	cin>>T;
	REP(i,T)solve();
	
	return 0;
}
