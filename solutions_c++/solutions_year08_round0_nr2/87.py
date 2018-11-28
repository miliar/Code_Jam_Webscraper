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


int main(){
//freopen("input.txt" ,"r",stdin );
//freopen("B-small.in" ,"r",stdin );
freopen("B-large.in" ,"r",stdin );
freopen("output.txt","w",stdout);
//char w[1024];
//while(gets(w))    puts(w);
//return 0;
    int TcN;cin>>TcN;
    REP(tc,TcN){
        cout<<"Case #"<<tc+1<<": ";
        int NA,NB,T;
        cin>>T>>NA>>NB;
        char c1,c2,c3,c4;
        VI Ag,Ac,Bg,Bc,Times;
        REP(i,NA){
            cin>>c1>>c2>>c3>>c3>>c4;
            Ag.pb((c1-'0')*600+(c2-'0')*60+(c3-'0')*10+(c4-'0'));
            cin>>c1>>c2>>c3>>c3>>c4;
            Bc.pb((c1-'0')*600+(c2-'0')*60+(c3-'0')*10+(c4-'0')+T);
            Times.pb(Ag.back());
            Times.pb(Bc.back());
        }
        REP(i,NB){
            cin>>c1>>c2>>c3>>c3>>c4;
            Bg.pb((c1-'0')*600+(c2-'0')*60+(c3-'0')*10+(c4-'0'));
            cin>>c1>>c2>>c3>>c3>>c4;
            Ac.pb((c1-'0')*600+(c2-'0')*60+(c3-'0')*10+(c4-'0')+T);
            Times.pb(Bg.back());
            Times.pb(Ac.back());
        }
        SORT(Times);UNIQUE(Times);
        Ag.pb(INF);Ac.pb(INF);Bg.pb(INF);Bc.pb(INF);
        SORT(Ag);SORT(Ac);SORT(Bg);SORT(Bc);
        REVERSE(Ag);REVERSE(Ac);REVERSE(Bg);REVERSE(Bc);
        int A=0,B=0,mA=0,mB=0;
        FORV(k,Times){
            while(Times[k]==Ac.back())
                A++,Ac.pop_back();
            while(Times[k]==Bc.back())
                B++,Bc.pop_back();
            while(Times[k]==Ag.back())
                A--,Ag.pop_back();
            while(Times[k]==Bg.back())
                B--,Bg.pop_back();
            mA<?=A;mB<?=B;
        }
        cout<<-mA<<" "<<-mB<<endl;
    }
    return 0;
}
