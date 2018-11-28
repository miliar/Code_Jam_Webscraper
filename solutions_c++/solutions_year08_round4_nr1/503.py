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

int R[2][16000];
VI A,G,C;

void DFS(int u){
    if(A[u]>=0){
        R[A[u]][u]=0;
        R[!A[u]][u]=INF;
        return;
    }
    DFS(2*u+1);DFS(2*u+2);
    if(G[u]){//AND
        R[1][u]<?=R[1][2*u+1]+R[1][2*u+2];
        R[0][u]<?=min(R[0][2*u+1],R[0][2*u+2]);
        if(C[u]){
            R[1][u]<?=min(R[1][2*u+1],R[1][2*u+2])+1;
            R[0][u]<?=R[0][2*u+1]+R[0][2*u+2]+1;
        }
    }else{//OR
        R[1][u]<?=min(R[1][2*u+1],R[1][2*u+2]);
        R[0][u]<?=R[0][2*u+1]+R[0][2*u+2];
        if(C[u]){
            R[1][u]<?=R[1][2*u+1]+R[1][2*u+2]+1;
            R[0][u]<?=min(R[0][2*u+1],R[0][2*u+2])+1;
        }
    }
}

string solve(){
    REP(i,2)REP(j,16000)
        R[i][j]=INF;
    int M,V;
    cin>>M>>V;
    A.clear();
    G.clear();
    C.clear();
    A.resize(M,-1);
    G.resize(M,-1);
    C.resize(M,-1);
    REP(i,(M-1)/2)
        cin>>G[i]>>C[i];
    REP(i,(M+1)/2)
        cin>>A[(M-1)/2+i];
    DFS(0);
    return R[V][0]<INF?tos(R[V][0]):"IMPOSSIBLE";
}

int main(){
//freopen("input.txt" ,"r",stdin );
//freopen("A-small-attempt1.in" ,"r",stdin );
freopen("A-large.in" ,"r",stdin );
freopen("output.txt","w",stdout);
//char w[1024];while(gets(w))puts(w);return 0;
cout<<fixed;cout.precision(8);
    int TcN;cin>>TcN;
    REP(tc,TcN){
        cout<<"Case #"<<tc+1<<": ";
        cout<<solve()<<endl;
    }
    return 0;
}
