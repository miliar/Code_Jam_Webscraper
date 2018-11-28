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


struct tree{
	bool isLeaf;
	double weight;
	string feture;
	tree *Left,*Right;

	tree(string s){
		Left=Right=NULL;
		Parse(s);
	}

	double getprob(set<string> fetures){
		if(isLeaf) return weight;
		if(fetures.count(feture)){
			return weight*Left->getprob(fetures);
		}
		return weight*Right->getprob(fetures);
	}

	void Parse(string s){
		isLeaf=true;
		FORE(it,s)if(isalpha(*it)){
			isLeaf=false;
			break;
		}
		
		if(isLeaf){
			int beg=s.find('(');
			int end=s.find_last_of(')');
			istringstream is(s.substr(beg+1,end-beg-1));
			is >> weight;
		}else{
			int beg=s.find('(');
			int end=s.find_last_of(')');
			string inner;
			istringstream is(inner=s.substr(beg+1,end-beg-1));
			is>>weight>>feture;
			
			int lvl=0;
			string sub;
			VS subs;
			FORE(it,inner){
				if(*it=='('){
					++lvl;
					if(lvl==1)sub="";
				}
				if(lvl>0)sub+=*it;				
				if(*it==')'){
					--lvl;
					if(lvl==0)
						subs.PB(sub);
				}
			}
			assert(SZ(subs)==2);
			
			Left=new tree(subs[0]);
			Right=new tree(subs[1]);
		}
	}
};

void solve(){
	int L,A;
	cin>>L;
	string ss,s;
	getline(cin,ss);
	
	REP(i,L){
		getline(cin,ss);
		s+=ss;
	}
	//DBG(s);
	
	tree t(s);

	cin>>A;
	getline(cin,ss);
	
	static int ct=0;
	
	printf("Case #%d:\n",++ct);
	
	REP(i,A){
		getline(cin,ss);
		istringstream is(ss);
		string str;
		int nf;
		is>>str>>nf;
		set<string> sets;
		REP(i,nf){
			is>>str;
			sets.insert(str);
		}
		double prob=t.getprob(sets);
		//DBG(prob);
		printf("%0.7lf\n",prob);
	}
}

int main(int argc,char* argv[]){
	int n;
	cin>>n;
	REP(i,n){
		solve();
	}
	return 0;
}
