#include <vector>
#include <iostream>
#include <sstream>
#include <math.h>
#include <sys/time.h>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <cstring>
#include <map>
#include <queue>

#define FOR(i,a,b)  for(__typeof(b) i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define FOREACH(x,c)   for(__typeof(c.begin()) x=c.begin();x != c.end(); x++)
#define ALL(c)      c.begin(),c.end()
#define CLEAR(c)    memset(c,0,sizeof(c))
#define SIZE(c) (int) ((c).size())

#define PB          push_back
#define MP          make_pair
#define X           first
#define Y           second

#define ULL         unsigned long long
#define LL          long long
#define LD          long double
#define II         pair<int, int>
#define DD         pair<double, double>

#define VI          vector<int>
#define VVI         vector<VI >
#define VD                      vector<double>
#define VS          vector<string >
#define VII        vector<II >
#define VDD         vector< DD >

#define DUMP(a)       cerr << #a << ": " << a << endl;
using namespace std;

#define X_MAX = 1000000

int tests;

double X, S, R, t;
vector<pair<double,double> > walks;
double result;
double W_SUM;

void read_test(){
    int N;
    cin >> X >> S >> R >> t >> N;

    walks.resize(N);
    int B, E, w;
    W_SUM = 0;
    REP(i,N){
        cin >> B >> E >> w;    
        walks[i] = MP(w,E-B);
        W_SUM += E-B;
    }	
}

void solve_test(){
    sort(ALL(walks));
    double tLeft = t;
    result = 0;
    if ( 1.0*(X-W_SUM) / R > t){
        result = t + 1.0*(X-W_SUM-t*R) / S;
        tLeft = 0;
    } else{
        result = 1.0*(X-W_SUM) / R;
        tLeft -= result;    
    }
    REP(i,SIZE(walks)){
        double v = walks[i].first;
        double s = walks[i].second;            
        if ( s / (R+v) > tLeft){
            result += tLeft + (s-tLeft*(R+v)) / (S+v);
            tLeft = 0;
        } else{
            result += s / (R+v);
            tLeft -= s / (R+v);
        }
    }
}

void dump_sol(int i){
    cout.precision(10);
	cout << "Case #" << i << ": ";
	cout << result << endl;
}

int main(){
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
		solve_test();
		dump_sol(i+1);
	}
}
