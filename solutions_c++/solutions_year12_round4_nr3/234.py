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
VI see;
VI h;
bool possible;

#define MAXH 1000000000
#define EPS 0.001

void read_test(){
    cin >> n;
    see.resize(n+2);
    REP(i,n-1)
        cin >> see[i+1]; 
	see[n] = n+1;
}

bool solve(int prev, int next){
// assign heights to prev+1..next-1, keeping everything below the line determined by the two
	VI trace;
	int i = prev+1;
	while (i < next){
		trace.PB(i);
		if (see[i] > next)
			return false;
		i = see[i];
	}

	i = trace.back();
	h[i] = floor( 1.0*(i-prev)*(h[next]-h[prev])/(next-prev) + h[prev] - EPS);
	if (i + 1 < next){
		if (!solve(i,next))
			return false;	
	}
	
	if (SIZE(trace) == 1)
		return true;

	for(int jInd=SIZE(trace)-2; jInd>=0; jInd--){
		int j = trace[jInd];
		int nextJ = trace[jInd+1];
		h[j] = floor( 1.0*(j-nextJ)*(h[next]-h[nextJ])/(next-nextJ) + h[nextJ]);
		if (j + 1 < nextJ){
			if (!solve(j,nextJ))
				return false;	
		}
	}
	return true;
}

bool solve_test(){
	h = VI(n+2,-1);
	h[0] = MAXH+1;
	h[n+1] = MAXH+1;
	solve(0,n+1);
}

void dump_sol(int i){
	cout << "Case #" << i << ": ";
	if (!possible)
		cout << "Impossible" << endl;
	else{
		REP(i,n-1)
			cout << h[i+1] << " ";
		cout << h[n] << endl;
	}
    cout.flush();
}

int main(int argc, char *argv[]){
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
    		possible = solve_test();
	    	dump_sol(i+1);
	}
}
