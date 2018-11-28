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

int C[1024][128];

int main(){
//freopen("input.txt" ,"r",stdin );
//freopen("A-small.in" ,"r",stdin );
freopen("A-large.in" ,"r",stdin );
freopen("output.txt","w",stdout);
    int T;cin>>T;
    REP(tc,T){
        cout<<"Case #"<<tc+1<<": ";
        int N,M;
        scanf("%d\n",&N);
        char buf[1024];
        vector<string> S(N);
        FORV(j,S){
            gets(buf);
            S[j]=buf;
        }
        scanf("%d\n",&M);
        vector<string> Q(M);
        FORV(i,Q){
            gets(buf);
            Q[i]=buf;
        }
        FORV(j,S)
            C[0][j]=(S[j]==Q[0]);
        FOR(i,1,sz(Q))
            FORV(j,S){
                C[i][j]=INF;
                if(S[j]!=Q[i])
                    C[i][j]=C[i-1][j];
                else
                    FORV(k,S)
                        if(k!=j)
                            C[i][j]<?=C[i-1][k]+1;
            }
        int ANS=INF;
        FORV(i,S)
            ANS<?=C[sz(Q)-1][i];
        cout<<ANS<<endl;
    }
    return 0;
}
