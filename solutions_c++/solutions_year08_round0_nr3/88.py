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


const double pi=acos((double)0)*2;

double DIV(double x,double y){
    return floor(x/y);
}
double MOD(double x,double y){
    return x-floor(x/y)*y;
}

const double N=2E7;

int main(){
//freopen("input.txt" ,"r",stdin );
//freopen("C-small.in" ,"r",stdin );
freopen("C-large.in" ,"r",stdin );
freopen("output.txt","w",stdout);
//char w[1024];
//while(gets(w))    puts(w);
//return 0;
cout<<fixed;cout.precision(8);
    int TcN;cin>>TcN;
    REP(tc,TcN){
        cout<<"Case #"<<tc+1<<": ";
        double f,R,t,r,g;
        cin>>f>>R>>t>>r>>g;
        g-=2*f;t+=f;r+=f;//i?aa?aoeee iooo a oi?eo
        double Gape=0,Left=0;
        double dx=(R-t)/N;
        for(double x=0;x<R-t;x+=dx){
            double y=sqrt(sqr(R-t)-sqr(x)),m1=MOD(x,2*r+g);
            if(m1>=r&&m1<=r+g){
                double l=DIV(y,2*r+g)*2*r,m=MOD(y,2*r+g);
                if(m<=r+g)
                    l+=min(m,r);
                else
                    l+=m-g;
                Left+=l*dx;
                Gape+=(y-l)*dx;
            }else
                Left+=dx*y;
        }
//        PR(Gape);PRL;PR(Left);PRL;PRL;PR(Gape+Left);PRL;PR(pi*sqr(R-t)/4);PRL;PRL;
        double gp=(pi*sqr(R-t)/4 - Left)+Gape;
        double ANS=(pi*sqr(R)/2-gp)/(pi*sqr(R)/2);
        cout<<ANS<<endl;
//        PRL;
    }
    return 0;
}
