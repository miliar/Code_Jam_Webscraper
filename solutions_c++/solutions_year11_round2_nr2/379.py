// By mirosuaf and rogrog v.3.1
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define SIZE(x) ((int)x.size())
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

int const MAXN=200;
int d,c;

VPII pos;

const double maxtime=2000000000000.0;
double firstpos;

bool okej(double t){
    double lastpos=firstpos-t-d;
    REP(i,SIZE(pos)){
        double p=pos[i].ST;
        REP(j,pos[i].ND){
            lastpos+=d; //odstep, teraz przesuwamy do lastpos

//printf("%lf, %lf, %d\n", lastpos,p-t, d);
            lastpos = max(lastpos, p-t); //nie mozna wiecej niz t w lewo
            //nie mozna wiecej niz t w prawo
        //    printf("umieszczem %d w %lf\n", i,lastpos);
            if(lastpos>p+t) return false;
        }
    }
    return true;
}

double binary(double a, double b){
   // printf("bin(%lf, %lf)\n", a,b);
    if(b-a<0.0000001) return a;
    double s=(a+b)/2;
    if(okej(s)) return binary(a,s);
    else return binary(s,b);
}

double zrob(){
  scanf("%d%d", &c, &d);
  pos.clear();
  REP(i,c) {
    int a,b;
    scanf("%d%d", &a, &b);
    pos.PB(MP(a,b));
  }
  sort(ALL(pos));
  firstpos=pos[0].ST;
  //okej(2.5);
  //return 0;
  return binary(0,maxtime);
}

int main() {
	int T; scanf("%d", &T); FOR(i,1,T) {
	    printf("Case #%d: %lf\n", i,
	    zrob()); }
	return 0;
}

