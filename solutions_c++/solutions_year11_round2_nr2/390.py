#include <vector>
#include <iostream>
#include <sstream>
#include <math.h>
#include <sys/time.h>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <cstring>

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

int tests;

double result;

int n;
double D;
VD p;
VD v;

void read_test(){
    cin >> n >> D;
    p.resize(n);
    v.resize(n);
    REP(i,n)
        cin >> p[i] >> v[i]; 
}

void solve_test(){
    VD psum(n+1);
    psum[0] = 0;
    double s = 0;
    REP(i,n){
        s = s + v[i];
        psum[i+1] = s;    
    }

    result = 0;
    REP(i,n) FOR(j,i,n)
        result = max(result,(D*(psum[j+1]-psum[i]-1)-(p[j]-p[i]))/2);
}

void dump_sol(int i){
	cout << "Case #" << i << ": ";
	cout << fixed << result << endl;
    cout.flush();
}

int main(int argc, char *argv[]){
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
    		solve_test();
	    	dump_sol(i+1);
	}
}
