// #includes {{{
#include <algorithm>
#include <numeric>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cmath>
using namespace std;
// }}}
// pre-written code {{{
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define RREP(i,a,b) for(int i=(int)(a);i<(int)(b);++i)
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
//#define IFOR(i,it,c) for(__typeof((c).begin())it=(c).begin();it!=(c).end();++it,++i)
#define ALL(c) (c).begin(), (c).end()
#define MP make_pair
//#define PB push_back
#define CLEAR(c,d) memset((c),(d),sizeof(c))
#define TO_STRING(VariableName) # VariableName
//#define DB(c) cout<<TO_STRING(c)<<"="<<(c)<<endl

#define EXIST(e,s) ((s).find(e)!=(s).end())
#define dump(x) cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;
#define debug2(x) cerr << #x << " = [";REP(__ind,(x).size()){cerr << (x)[__ind] << ", ";}cerr << "] (L" << __LINE__ << ")" << endl;

#define clr(a) memset((a),0,sizeof(a))
#define nclr(a) memset((a),-1,sizeof(a))
#define pb push_back

typedef long long Int;
typedef unsigned long long uInt;
typedef long double rn;

typedef pair<int,int> pii;
//{{{ io
struct IO{ }io;//dummy
#define endl "\n"
IO& operator>>(IO &io,int &n){scanf("%d",&n);return io;}
IO& operator>>(IO &io,unsigned int &n){scanf("%u",&n);return io;}
IO& operator>>(IO &io,long long &n){scanf("%lld",&n);return io;}
IO& operator>>(IO &io,unsigned long long &n){scanf("%llu",&n);return io;}
IO& operator>>(IO &io,double &n){scanf("%lf",&n);return io;}
IO& operator>>(IO &io,long double &n){scanf("%Lf",&n);return io;}
IO& operator>>(IO &io,char *c){scanf("%s",c);return io;}
IO& operator>>(IO &io,string &s){
    char c;s.clear();
    while(isspace(c=getc(stdin))){if(c==-1)return io;}
    do{
        s.push_back(c);
    }while(!isspace(c=getc(stdin)));
    if(c!=-1)ungetc(c,stdin);
    return io;
}
IO& operator<<(IO &io,const int &n){printf("%d",n);return io;}
IO& operator<<(IO &io,const unsigned int &n){printf("%u",n);return io;}
IO& operator<<(IO &io,const long long &n){printf("%lld",n);return io;}
IO& operator<<(IO &io,const unsigned long long &n){printf("%llu",n);return io;}
IO& operator<<(IO &io,const double &n){printf("%lf",n);return io;}
IO& operator<<(IO &io,const long double &n){printf("%Lf",n);return io;}
IO& operator<<(IO &io,const char c[]){printf("%s",c);return io;}
IO& operator<<(IO &io,const string &s){
    REP(i,s.size())putc(s[i],stdout);
}
//}}}
// }}}

const rn EPS=1e-13L;
const int M=1010;
int n;
rn P[M],L[M],Q[M];
vector<pair<rn,int> > v;

struct S{
	bool operator()(const pair<rn,int> &l,const pair<rn,int> &r){
		if(abs(l.first-r.first)>EPS)return l.first>r.first;
		return l.second>r.second;
	}
};


void main2(){
	v.clear();
	cin>>n;
	REP(i,n)cin>>L[i];
	REP(i,n)cin>>P[i];
	REP(i,n){
		P[i]/=100;Q[i]=1.0L/(1.0L-P[i]);
//		cout<<Q[i]<<endl;
		v.push_back(MP((1.0L-Q[i])/L[i]/Q[i],i));
	}
	sort(ALL(v),S());
	/*
	REP(i,n){
		cout<<v[i].first<<" "<<v[i].second<<endl;
	}
	*/
	reverse(ALL(v));
	REP(i,n){
		cout<<v[i].second;
		if(i!=n-1)cout<<" ";
	}
	cout<<endl;
}

//{{{ main function
int main() {
	int T;scanf("%d", &T);
	REP(ct, T){ printf("Case #%d: ",ct+1);main2();}
	return 0;
}
//}}}
