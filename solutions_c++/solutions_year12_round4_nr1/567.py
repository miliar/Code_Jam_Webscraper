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

int n;
double D;
VI d;
VI l;
bool result;

void read_test(){
    cin >> n;
    d.resize(n);
    l.resize(n);
    REP(i,n)
        cin >> d[i] >> l[i];
	cin >> D; 
}

void solve_test(){
	VI grip(n,0);
	int maxD = 0;
	grip[0] = d[0];
	result = false;
	REP(i,n){
		if (grip[i]+d[i] >= D){
			result = true;
			return;		
		}
		for(int j=i+1; j < n && d[j] <= grip[i]+d[i]; j++)
			grip[j] = max(grip[j],min(l[j],d[j]-d[i]));
	}
}

void dump_sol(int i){
	cout << "Case #" << i << ": ";
	if (result)
		cout << "YES" << endl;
	else
		cout << "NO" << endl;
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
