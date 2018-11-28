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
#define FOR(I,S,N) for(int I=(S);I<(N);I++)
#define REP(I,N) FOR(I,0,N)
#define FORD(I,S,N) for(int I=(S);I>=(N);I--)
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
//================================TIME==========================================
double Clock() {
    unsigned long long time;
    __asm__ volatile ("rdtsc" : "=A" (time));
    return time / 2.8e9; 
}
//================================MAIN==========================================

int64 M[512][512];
int64 S[512][512];
int64 Sx[512][512];
int64 Sy[512][512];

int centered(int i, int j, int k){
	int64 m = S[i+k][j+k] - S[i+k][j] - S[i][j+k] + S[i][j];
	m -= M[i+k-1][j+k-1] + M[i+k-1][j] + M[i][j+k-1] + M[i][j];

	int64 mx = Sx[i+k][j+k] - Sx[i+k][j] - Sx[i][j+k] + Sx[i][j];
	mx -= M[i+k-1][j+k-1]*(i+k-1) + M[i+k-1][j]*(i+k-1) + M[i][j+k-1]*i + M[i][j]*i;

	int64 my = Sy[i+k][j+k] - Sy[i+k][j] - Sy[i][j+k] + Sy[i][j];
	my -= M[i+k-1][j+k-1]*(j+k-1) + M[i+k-1][j]*j + M[i][j+k-1]*(j+k-1) + M[i][j]*j;
	
	return 2 * mx == (2*i+k-1) * m && 2 * my == (2*j+k-1) * m;
}

int main(){
//freopen("input.txt" ,"r",stdin );
//freopen("B-small-attempt0.in" ,"r",stdin );
freopen("B-large.in" ,"r",stdin );
freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    REP(tc, T){
        cout<<"Case #"<<tc+1<<": ";
        int R,C,D;
        cin >> R >> C >> D;
        REP(i,R)
        	REP(j,C){
				char c;
				cin >> c;
				M[i][j] = D + c - '0';
			}
        
        memset(S, 0, sizeof(S));
        memset(Sx, 0, sizeof(Sx));
        memset(Sy, 0, sizeof(Sy));
        
        REP(i,R)
        	REP(j,C){
        		S[i+1][j+1] = S[i][j+1] + S[i+1][j] - S[i][j] + M[i][j];
        		Sx[i+1][j+1] = Sx[i][j+1] + Sx[i+1][j] - Sx[i][j] + M[i][j] * i;
        		Sy[i+1][j+1] = Sy[i][j+1] + Sy[i+1][j] - Sy[i][j] + M[i][j] * j;
			}
        
        FORD(k, min(R,C), 3){
			REP(i, R-k+1)
				REP(j, C-k+1)
					if( centered(i, j, k) ){
						cout << k << endl;
						goto nextTestCase;
					}
		}
        
        cout << "IMPOSSIBLE" << endl;
        nextTestCase:;
    }
    return 0;
}
