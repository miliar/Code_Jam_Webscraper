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

int n,w,l;
double D;
VI r;
VI x, y;

void read_test(){
    cin >> n >> w >> l;
    r.resize(n);
    REP(i,n)
        cin >> r[i]; 
}

bool valid(){
	REP(i,n-1)
		FOR(j,i+1,n)
			if (abs(x[i]-x[j]) <= r[i]+r[j] && abs(y[i]-y[j]) <= r[i]+r[j])
				return false;
	return true;
}

void solve_test(){
	x = VI(n);
	y = VI(n);
	do{
		REP(i,n){
			x[i] = rand()%(w+1);
			y[i] = rand()%(l+1);
		}
	} while(!valid());
}

void dump_sol(int i){
	cout << "Case #" << i << ":";
	REP(i,n)
		cout << " " << x[i] << " " << y[i];
	cout << endl;
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
