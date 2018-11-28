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


int T;
int ct=0;

int H,W;
VVI a;
vector<vector<pii> > root;

int di[4]={-1,0,0,1};
int dj[4]={0,-1,1,0};

pii findroot(int i,int j){
	

	if(root[i][j]!=MP(-1,-1))return root[i][j];
	
	int cc=a[i][j],xx,yy;
	REP(d,4){
		int ni=i+di[d],nj=j+dj[d];

		if(ni<0||ni>=H||nj<0||nj>=W)continue;
		if(a[ni][nj]<cc){
			cc=a[ni][nj];
			xx=ni;
			yy=nj;
		}
	}
	if(cc==a[i][j])return root[i][j]=MP(i,j);

	if(xx==i&&yy==j)return pii(-1,-1);
	return root[i][j]=findroot(xx,yy);
}

void solve(){
	scanf("%d%d",&H,&W);
	a=VVI(H,VI(W,0));
	root=vector<vector<pii> >(H,vector<pii>(W,MP(-1,-1)));
	
	REP(i,H){
		REP(j,W){
			scanf("%d",&a[i][j]);
		}
	}
	

	
	map<pii,pii> mp;
	REP(i,H)
	REP(j,W)
		mp[findroot(i,j)];

	FORE(it,mp){
		it->second=it->first;
	}
	REP(i,H)REP(j,W){
		
		if(MP(i,j)<mp[root[i][j]])
			mp[root[i][j]]=MP(i,j);

	}
	
	map<pii,char> mc;	
	FORE(it,mp){
		mc[it->second];
	}
	char ccc='a';	
	FORE(it,mc){
		it->second=ccc++;
	}
	
	
	printf("Case #%d:\n",++ct);
	
	REP(i,H){
		REP(j,W){
		if(j!=0)printf(" ");
		printf("%c",mc[mp[root[i][j]]]);
		}
		printf("\n");
	}
}

int main(int argc,char* argv[]){
	scanf("%d",&T);
	REP(i,T)solve();
	
	return 0;
}
