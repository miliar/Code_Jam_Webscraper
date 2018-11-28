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

struct DisSet{
    VI p;int nSets;
    DisSet(int N):nSets(N),p(N,-1){}
    int findRoot(int v){
        return p[v]<0 ? v : p[v]=findRoot(p[v]);
    }
    void unite(int u,int v){
        u=findRoot(u),v=findRoot(v);
        if(u!=v)
            p[v]=u,nSets--;
    }
};

int dx[]={-1, 0, 0, 1 };
int dy[]={ 0,-1, 1, 0 };

int H,W;
int A[128][128];
char P[128*128];

int main(){
freopen("input.txt" ,"r",stdin );
freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    REP(t,T){
        cin>>H>>W;
        REP(i,H)
            REP(j,W)
                cin>>A[i][j];

        DisSet ds(H*W);

        REP(i,H)
            REP(j,W){
                int MinAlt = INF;
                REP(d,4){
                    int x = i + dx[d], y = j + dy[d];
                    if( x >= 0 && x < H && y >= 0 && y < W )
                        MinAlt <?= A[x][y];
                }
                if( MinAlt < A[i][j] )
                    REP(d,4){
                        int x = i + dx[d], y = j + dy[d];
                        if( x >= 0 && x < H && y >= 0 && y < W && MinAlt == A[x][y]){
                            ds.unite( x*W + y, i*W + j );
                            break;
                        }
                    }
            }
//        PR( ds.nSets );PRL;
        
        cout<<"Case #"<<t+1<<":"<<endl;
        
        memset(P,0,sizeof(P));
        char l = 'a';
        REP(i,H){
            REP(j,W){
                int lab = ds.findRoot( i*W + j );
                if( !P[ lab ] )
                    P[lab] = l++;
                if( j )
                    cout<<" ";
                cout<<P[lab];
            }
            cout<<endl;
        }
        
    }
    
    return 0;
}
