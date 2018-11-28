#include<algorithm>
#include<iostream>
//#include<numeric>
//#include<complex>
#include<sstream>
#include<cstdio>
#include<string>
#include<vector>
#include<cmath>
//#include<queue>
//#include<list>
//#include<set>
//#include<map>
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

int solve2(vector<int64> v1,vector<int64> v2){
    SORT(v1);SORT(v2);
    int64 res=INF64;
    do{
        int t=0;
        FORV(i,v1)
            t+=v1[i]*v2[i];
        res<?=t;
    }while(next_permutation(ALL(v1)));
    return res;
}


int solve1(vector<int64> v1,vector<int64> v2){
    SORT(v1);SORT(v2);REVERSE(v2);
    int64 res=0;
    FORV(i,v1)
        res+=v1[i]*v2[i];
    return res;
}

int main(){
//freopen("input.txt" ,"r",stdin );
freopen("A-small-attempt0.in" ,"r",stdin );
//freopen("A-large.in" ,"r",stdin );
freopen("output.txt","w",stdout);
int TN;cin>>TN;
    REP(Tk,TN){
        cout<<"Case #"<<Tk+1<<": ";
        int N;
        cin>>N;
        vector<int64> v1(N),v2(N);
        FORV(i,v1)
            cin>>v1[i];
        FORV(i,v2)
            cin>>v2[i];
        if(solve1(v1,v2)!=solve2(v1,v2))
            cout<<"Ooops"<<endl;
        cout<<solve1(v1,v2)<<endl;
    }
    return 0;
}
