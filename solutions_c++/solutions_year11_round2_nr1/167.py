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

int N;

char Map[128][128];

double WP[128];
double OWP[128];
double OOWP[128];

int main(){
//freopen("input.txt" ,"r",stdin );
//freopen("A-small-attempt0.in" ,"r",stdin );
freopen("A-large.in" ,"r",stdin );
freopen("output.txt","w",stdout);
	cout << fixed;
	cout.precision(15);
    int T;
    cin >> T;
    REP(tc, T){
        cout<<"Case #"<<tc+1<<":"<<endl;
        cin >> N;
        
        REP(i, N)
        	cin >> Map[i];
        
        //WP
        REP(i, N){
			int games = 0, wins = 0;
        	REP(j, N)
				if( Map[i][j] != '.' ){
					games++;
					wins += Map[i][j] - '0';
				}
			WP[i] = 1. * wins / games;
		}
        
        //OWP
        REP(k, N){
			double S = 0;
			int n = 0;
	        REP(i, N)
				if( Map[k][i] != '.' ){
					n++;
					int games = 0, wins = 0;
		        	REP(j, N)
						if( j != k && Map[i][j] != '.' ){
							games++;
							wins += Map[i][j] - '0';
						}
					S += 1. * wins / games;
				}
			OWP[k] = S / n;
		}
		
        //OOWP
        REP(k, N){
			double S = 0;
			int n = 0;
	        REP(i, N)
				if( Map[k][i] != '.' ){
					n++;
					S += OWP[i];
				}
			OOWP[k] = S / n;
		}
		
		//RPI
		REP(i, N){
			double RPI = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			cout << RPI << endl;
		}
    }
    return 0;
}
