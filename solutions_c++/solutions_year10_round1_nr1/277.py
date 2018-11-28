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

vector<string> board;
int N,K;

bool Wins(char p){
    FORV(i, board)//horizontal
        FORV(j, board[i]){
            int c = 0;
            REP(k,K)
                if( j+k < N && board[i][j+k] == p )
                    c++;
            if( c == K )
                return true;
        }

    FORV(i, board)//vertical
        FORV(j, board[i]){
            int c = 0;
            REP(k,K)
                if( i+k <N && board[i+k][j] == p )
                    c++;
            if( c == K )
                return true;
        }
            
    FORV(i, board)//diagonal_1
        FORV(j, board[i]){
            int c = 0;
            REP(k,K)
                if( i+k <N && j+k < N && board[i+k][j+k] == p )
                    c++;
            if( c == K )
                return true;
        }

    FORV(i, board)//diagonal_2
        FORV(j, board[i]){
            int c = 0;
            REP(k,K)
                if( i+k <N && 0 <= j-k && board[i+k][j-k] == p )
                    c++;
            if( c == K )
                return true;
        }
    return false;
}

void Rotate(){
    vector<string> b1 = board;
    FORV(i, b1)
        FORV(j, b1[i])
            board[j][N-i-1] = b1[i][j];
}

void Gravity(){
    REP(k, 2*N+2)
        FORD(i, N-1, 0)
            FORV(j, board[i])
                if( board[i][j] == '.' && i && board[i-1][j] != '.' )
                    swap( board[i][j], board[i-1][j] );
}

int main(){
//freopen("input.txt" ,"r",stdin );
freopen("A-large.in" ,"r",stdin );
//freopen("A-small-attempt0.in" ,"r",stdin );
freopen("output.txt","w",stdout);
    int Tc;
    cin>>Tc;
    REP(tc, Tc){
        cout<<"Case #"<<tc+1<<": ";
        cin>>N>>K;
        board.resize(N);
        FORV(i,board)
            cin>>board[i];
        Rotate();
        Gravity();
        bool R = Wins('R'), B = Wins('B');
        if( B && R ){
            cout<<"Both"<<endl;
            continue;
        }
        if( B ){
            cout<<"Blue"<<endl;
            continue;
        }
        if( R ){
            cout<<"Red"<<endl;
            continue;
        }
        cout<<"Neither"<<endl;
    }
    return 0;
}
