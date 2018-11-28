#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>

using namespace std;
 
typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
 
#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(b); --i)
#define ALL(v) (v).begin(), (v).end()
 
#define pb push_back
#define mp make_pair
#define st first
#define nd second

#define DEBUG 0
#define max_n 1005

int N;
double dyst, V,R, t;
double ogr[max_n];
double war[max_n];
double dl[max_n];
double W[max_n];
double wynik;
double sumaDlugosci;

void rob(){
    wynik = 0.;
    REP (i,N){
        wynik += dl[i]/(V+W[i]);
    }
    vector< pair< double, double > > costam;
    REP(i,N){
        costam.pb( mp ( (V-R)/(V+W[i]) , dl[i]/(R+W[i]) ));
    }
    sort(costam.begin(), costam.end());
    double zostalo = t;
    REP(i,N){
        double czas=min(zostalo, costam[i].nd);
        zostalo-=czas;
        wynik += costam[i].st*czas;
    }
}

int main(){
    int Z; scanf("%d",&Z); 
    FOR(z,1,Z+1){
       // scanf("%d%d%d%d%d",&dyst,&V,&R,&t,&N);
        cin>>dyst>>V>>R>>t>>N;
        sumaDlugosci=0;
        REP(i,N){
            double a,b,c; cin>>a>>b>>c;
            //int a,b,c; scanf("%d%d%d",&a,&b,&c);
            dl[i] = b-a; W[i]=c; sumaDlugosci += dl[i];
        }
        dl[N] = dyst-sumaDlugosci; 
        W[N] = 0;
        N=N+1;;
        rob();
        //printf("Case #%d: %lf\n", z, wynik);
        cout<<"Case #"<<z<<": "; printf("%.10lf\n",wynik);
    }
}

