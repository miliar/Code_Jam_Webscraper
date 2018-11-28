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

int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};

void solve(){
	static int ct=0;
	
	int W,Q;
	cin>>W>>Q;
	VS a;
	REP(i,W){
		string s;
		cin>>s;
		a.PB(s);
	}
	
	vector<vector<map<int,string> > > opti;
	opti.resize(W);
	REP(i,W)opti[i].resize(W);
	
	REP(i,W)REP(j,W){
		if(isdigit(a[i][j])){
			opti[i][j][a[i][j]-'0']=a[i][j];
		}
	}
	
	bool flag=true;
	while(flag){
		flag=false;
		REP(i,W)REP(j,W){
			if(isdigit(a[i][j])){
				REP(d1,4){
					int opx=i+dx[d1];
					int opy=j+dy[d1];
					if(opx<0||opx>=W||opy<0||opy>=W)continue;
					REP(d2,4){
						int rhx=opx+dx[d2];
						int rhy=opy+dy[d2];
						if(rhx<0||rhx>=W||rhy<0||rhy>=W)continue;
						
						int ofs=a[rhx][rhy]-'0';
						if(a[opx][opy]=='-')ofs=-ofs;
						
						FORE(it,opti[i][j]){
							int newval=it->first+ofs;
							
							if(newval<-50||newval>300) continue;
							
							string newexp=it->second+a[opx][opy]+a[rhx][rhy];
							
							string& orig=opti[rhx][rhy][newval];
							if(orig.empty()||SZ(newexp)<SZ(orig)||
							 SZ(newexp)==SZ(orig)&&newexp<orig){
									orig=newexp;
									flag=true;
							}
							
						}
						
					}
				}
			}
		}
	}
	
	
	cout<<"Case #"<<++ct<<":\n";
	REP(i,Q){
		int v;
		cin>>v;
		//DBG(v);
		
		string best;
		REP(i,W)REP(j,W){
			if(opti[i][j].count(v)){
				string& opt=opti[i][j][v];
				if(best=="" || SZ(opt)<SZ(best) || 
				   SZ(opt)==SZ(best)&&opt<best){
					best=opt;
				}
			}
		}
		cout<<best<<endl;
	}
}

int main(int argc,char* argv[]){
	int T;
	cin>>T;
	REP(i,T) solve();
	return 0;
}
