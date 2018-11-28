#include<iostream>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<utility>
#include<fstream>
#include<iosfwd>
#include<sstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<cstring>
#include<ctime>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cassert>
#include<complex>
#include<numeric>

using namespace std;

#define DEBUG                            0
#define BUG(x)                           cout<<"Debugging Variable "<< #x <<endl
#define SYS                              system("pause")
#define VAR(x,a)                         __typeof(a) x(a)
#define FORD(i,a,b)                      for(int i = (int)a,_b = (int)b;i>=(_b);--i)
#define FOREACH(it,v)                    for(VAR(it,(v).begin());it!=(v).end();++it)
#define FOR(i,a,b)                       for(int i=(int)(a),_b = (int)b;i<(int)(_b);++i)
#define REP(i,n)                         FOR(i,0,n)
#define REPD(i,n)                        FORD(i,n,0)
#define Size()                           size()
#define PB                               push_back
#define PF                               push_front
#define MP                               make_pair
#define SZ                               size()
#define ALL(X)                           X.begin(),X.end()
#define RALL(X)                          X.rbegin(),X.rend()
#define Clear(X)                         memset(X,0,sizeof(X))
#define PushBack                         push_back
#define PushFront                        push_front
#define MakePair                         make_pair
#define PopBack                          pop_back
#define PopFront                         pop_front
#define BitCount                         __builtin_popcount
#define INF                              100000000
#define INFLL                            10000000000000000LL

typedef vector< int >                    VI;
typedef vector< double >                 VD;
typedef vector< string >                 VS;
typedef vector< char >                   VC;
typedef vector< long double >            VLD;
typedef vector< long long >              VLL;
typedef vector< vector< int > >          VVI;
typedef vector< pair< int,int > >        VPII;
typedef vector< vector< double > >       VVD;
typedef vector< vector< char > >         VVC;
typedef vector< vector< string > >       VVS;
typedef vector< vector< long long > >    VVLL;
typedef string                           SS;
typedef unsigned long long               ULL;
typedef long long                        LL;
typedef long double                      LD;
typedef pair< int,int >                  PII;
typedef unsigned long                    UL;

int RInt(){int N;scanf("%d",&N);return N;}
SS  RSS(){SS S;cin>>S;return S;}
LL  RLL(){LL N;cin>>N;return N;}
VI  RVInt(int N){VI V(N,0);for(int i=0;i<N;++i)scanf("%d",&V[i]);return V;}

void DInt(int X){cout<<"Value Of Variable = "<<X<<endl;}
void DSS(SS S){cout<<"String is "<<S<<endl;}
void DVInt(VI V){cout<<"Vector Size = "<<V.SZ<<endl;cout<<"Elements "<<endl;REP(i,V.SZ)cout<<V[i]<<" ";cout<<endl;}
void DLL(LL X){cout<<"Value Of Variable = "<<X<<endl;}

VI X(31,0);

void precompute() {
    FOR(i,1,X.SZ) {
        FOR(j,1,i)
            X[i]+=X[j];
        X[i]+=i;
    }
}

int main()
{
    precompute();
    ifstream fin("A-large.in",ios::in);
    ofstream fout("AL1.out",ios::out);
    int T,C=1;
    fin>>T;
    while(T--) {
        int N,K;
        fin>>N>>K;
        int Y=0;
        fout<<"Case #"<<C<<": ";
        K=K%(X[N]+1);
        if(K==X[N])
            fout<<"ON\n";
        else
            fout<<"OFF\n";
        C++;
    }
    fin.close();
    fout.close();
    return 0;
}

