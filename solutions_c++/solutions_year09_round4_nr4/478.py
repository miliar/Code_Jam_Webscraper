#include<algorithm>
#include<iostream>
#include<numeric>
#include<complex>
#include<sstream>
#include<cstdio>
#include<string>
#include<vector>
#include<cmath>
#include<queue>
#include<list>
#include<set>
#include<map>
using namespace std;

//===============================SHORTENINGS====================================
typedef long long int64;
typedef pair<int,int> PII;
#define X first
#define Y second
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
#define VAR(a,b) __typeof(b) a=(b)
template<typename T> T inline sqr(T q){return q*q;}
#define sz(X) ((int)(X).size())
#define pb push_back
#define ALL(c) (c).begin(),(c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) (c).resize(unique(ALL(c))-(c).begin())
//===============================CONSTANTS======================================
const int INF=1000000001;
const int64 INF64=sqr((int64)INF);
const double EPS=1E-7;
//=================================LOOPS========================================
#define FOR(I,S,N) for(int I=S;I<N;I++)
#define REP(I,N) FOR(I,0,N)
#define FORD(I,S,N) for(int I=S;I>=N;I--)
#define FORV(i,v) FOR(i,0,sz(v))
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
//===============================STRINGS========================================
typedef stringstream SS;
template<typename T> string tos(T q,int w=0)
{ SS A;A.precision(w);A<<fixed<<q; return A.str();}
template<typename T> T sto(string s){SS A(s);T t;A>>t;return t;}
template<typename T> vector<T> s2v(string s,string d=" "){
    FORV(i,s)FORV(j,d)if(s[i]==d[j])s[i]=' ';
    int n=sz(s);while(n&&s[n-1]==' ')n--;
    s.resize(n);SS A(s);vector<T> ans;
    for(T t;A>>t;)ans.pb(t);
    return ans;
}
//================================DEBUG=========================================
template<typename T1,typename T2>ostream &operator<<(ostream &out,const 
pair<T1,T2> &t ){out << "( " <<  t.X << " , " << t.Y << " )";return out;}
template<typename T>ostream &operator<<(ostream &out,const vector<T> &t){
out<<"{ ";FORV(i,t){if(i)out<<", ";out<<t[i];}out<<" }";return out;}
#define PR(X) cout<<#X<<" = "<<(X)<<" "
#define PRL cout<<endl
//================================MAIN==========================================

struct Pnt{
    int x,y,r;
    Pnt(int x = 0, int y = 0, int r = 0):x(x),y(y),r(r){}
};

int CountBit(int x){
    return x? CountBit(x/2)+x%2 : 0;
}

double Dst(Pnt A, Pnt B){
    return sqrt( 1.*sqr(A.x-B.x) + sqr(A.y-B.y) );
}

double F(vector<Pnt> P){
    if( sz(P) == 0 )
        return 0;
    if( sz(P) == 1 )
        return P[0].r;
    if( sz(P) == 2 )
        return (P[0].r+P[1].r + Dst(P[0],P[1]))/2.0;
    return 1E100;
}

int main(){
//freopen("input.txt" ,"r",stdin );
freopen("D-small-attempt0.in" ,"r",stdin );
freopen("output.txt","w",stdout);
cout<<fixed;
cout.precision(9);
    int T;
    cin>>T;
    REP(tc, T){
        cout<<"Case #"<<tc+1<<": ";
        int N;
        cin>>N;
        vector<Pnt> P(N);
        REP(i,N)
            cin>>P[i].x>>P[i].y>>P[i].r;
        
        double ans = 1E10;
        
        REP(mask, 1<<N){
            vector<Pnt> A,B;
            REP(i,N)
                if( mask & (1<<i) )
                    A.pb(P[i]);
                else
                    B.pb(P[i]);
            ans <?= max(F(A),F(B));
        }
        cout<<ans<<endl;
    }
    return 0;
}
