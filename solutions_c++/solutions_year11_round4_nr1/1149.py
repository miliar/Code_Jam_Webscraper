#include<iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef vector<int> VI;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
typedef long double LD;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-10
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

int TT;
int R,S,X,t,N;
VPII V;

double zakolkoprejdem(double dlzka, double rychlost){
    return dlzka/rychlost;
}

double dlz(double cas, double rychlost){
    return cas*rychlost;
}

int main(){
    scanf("%d ",&TT);
    FOR(tt,TT){
        double cas = 0.0;
        V.resize(0);
        scanf("%d %d %d %d %d ",&X,&S,&R,&t,&N);
//        cout << X << " " << S << " " << R << " " << t << " " << N << endl;
        int zvysok = X;
        double estepobezim = t;
        FOR(i,N){
            int b, e,  w;
            scanf("%d %d %d ",&b,&e,&w);
            V.PB(MP(w,e-b));
            zvysok -= (e-b);
        }
        V.PB(MP(0,zvysok));
        sort(V.begin(),V.end());
        //cout << "zac: " << V[0].first << " " << V[0].second << endl;
        //reverse(V.begin(),V.end());
        FOR(i,V.size()){
            double sbehom = zakolkoprejdem(V[i].second,V[i].first+R);
            if (sbehom <= estepobezim){
                estepobezim -= sbehom;
                cas += sbehom;
            }else{
            //    cout << estepobezim << " " << V[i].first + R << endl;
                double prebehnem = dlz(estepobezim,V[i].first+R);
              //  cout << V[i].second << " " << prebehnem << endl;
                double ostalo = (double)V[i].second - prebehnem;
            //    cout << ostalo << endl;
                cas += zakolkoprejdem(prebehnem,V[i].first+R);
                //estepobezim -= zakolkoprejdem(prebehnem,V[i].first+R);
                estepobezim = 0;
                cas += zakolkoprejdem(ostalo,V[i].first+S);
            }
        }
        printf("Case #%d: %.10lf\n",tt+1,cas);
    }
}
