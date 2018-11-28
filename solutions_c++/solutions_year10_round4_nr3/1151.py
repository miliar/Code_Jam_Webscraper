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

char A[101][101];
char B[101][101];

int Solve(){
    int R;
    cin>>R;
    memset(A,0,sizeof(A));
    REP(i,R){
        int x1,x2,y1,y2;
        cin>>x1>>y1>>x2>>y2;
        FOR(x, x1, x2+1)
            FOR(y, y1, y2+1)
                A[x][y] = 1;
    }
    for(int res = 0; ; res++){
        memcpy(B, A, sizeof(A));
        bool found = false;
        FOR(i, 1, 101)
            FOR(j, 1, 101){
                if( A[i-1][j] == 0 && A[i][j-1] == 0 )
                    B[i][j] = 0;
                if( A[i][j] == 0 && A[i-1][j] == 1 && A[i][j-1] == 1 )
                    B[i][j] = 1;

                if( A[i][j] == 1 )
                    found = true;
            }
        if( !found )
            return res;
        memcpy(A, B, sizeof(A));
    }
    return -1;
}

int main(){
//freopen("input.txt" ,"r",stdin );
freopen("C-small-attempt0.in" ,"r",stdin );
//freopen("C-large.in" ,"r",stdin );
freopen("output.txt","w",stdout);
    int Tc;
    cin>>Tc;
    REP(tc, Tc){
        cout<<"Case #"<<tc+1<<": "<<Solve()<<endl;
    }
    return 0;
}
