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
VI t;
VI s1, s2;

void read_test(){
    cin >> n;
    t.resize(n);
    REP(i,n)
        cin >> t[i]; 
}

VI dyn;

VI backtrack(int i){
	VI s;
	while (i != 0){
		s.PB(dyn[i]);
		i = i - t[dyn[i]];	
	}
	return s;
}

void solve_test(){
	int M = 20*100000; 
	dyn = VI(M+1,-1);
	dyn[0] = 0;
	REP(i,n){
		for(int j=M-t[i]; j >= 0; j--)
			if (dyn[j] != -1){
				if (dyn[j+t[i]] != -1) { // end
					s1 = backtrack(j+t[i]);
					s2 = backtrack(j);
					s2.PB(i);
					return;
				} else
					dyn[j+t[i]] = i;
			}
	}
}

void dump_sol(int i){
	cout << "Case #" << i << ": " << endl;
	if (SIZE(s1) == 0){
		cout << "Impossible" << endl;
		return;	
	}
	REP(i,SIZE(s1)){
		cout << t[s1[i]];
		if (i == SIZE(s1)-1)
			cout << endl;
		else
			cout << " ";
	}
	REP(i,SIZE(s2)){
		cout << t[s2[i]];
		if (i == SIZE(s2)-1)
			cout << endl;
		else
			cout << " ";
	}
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
