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
{ SS A;A.flags(ios::fixed);A.precision(w);A<<q; string s;A>>s;return s;}
template<typename T> T sto(string s){SS A(s);T t;A>>t;return t;}
template<typename T> vector<T> s2v(string s)
{SS A(s);vector<T> ans;while(A&&!A.eof()){T t;A>>t;ans.pb(t);}return ans;}
//================================DEBUG=========================================
template<typename T1,typename T2>ostream &operator<<(ostream &out,const 
pair<T1,T2> &t ){out << "( " <<  t.X << " , " << t.Y << " )";return out;}
template<typename T>ostream &operator<<(ostream &out,const vector<T> &t){
out<<"{ ";FORV(i,t){if(i)out<<", ";out<<t[i];}out<<" }";return out;}
#define PR(X) cout<<#X<<" = "<<(X)<<" "
#define PRL cout<<endl
//================================MAIN==========================================

int H,W,R;
int C[128][128];
int B[128][128];

const int MOD=10007;

int solve(){
    cin>>H>>W>>R;
    memset(C,0,sizeof(C));
    memset(B,0,sizeof(B));
    REP(i,R){
        int u,v;
        cin>>u>>v;
        B[u-1][v-1]=1;
    }
    C[0][0]=1;
    FOR(i,1,H)
        FOR(j,1,W)
            if(!B[i][j]){
                REP(i1,i)
                    REP(j1,j)
                        if(sqr(i-i1)+sqr(j-j1)==5)
                            C[i][j]+=C[i1][j1];
                C[i][j]%=MOD;
            }
    return C[H-1][W-1];
}

int main(){
//freopen("input.txt" ,"r",stdin );
freopen("D-small-attempt0.in" ,"r",stdin );
//freopen("D-large.in" ,"r",stdin );
freopen("D-out.txt","w",stdout);
//char w[1024];while(gets(w))puts(w);return 0;
cout<<fixed;cout.precision(8);
    int TcN;cin>>TcN;
    REP(tc,TcN){
        cout<<"Case #"<<tc+1<<": ";
        cout<<solve()<<endl;
    }
    return 0;
}
