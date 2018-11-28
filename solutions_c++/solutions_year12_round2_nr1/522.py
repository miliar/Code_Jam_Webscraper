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
VI scores;
VD results;

void read_test(){
    cin >> n;
    scores.resize(n);
    REP(i,n)
        cin >> scores[i]; 
}

double solve_test(int i){
	int score = scores[i];
	VI sc=scores;
	sc[i] = sc.back();
	sc.pop_back();
	sort(ALL(sc));

	VI sum(n-1);
	int s = 0;
	REP(i,n-1){
		s += sc[i];
		sum[i] = s;	
	} 
	int total = sum[n-2]+score;
	sc.push_back(10*total);

	if (n*score >= 2*total)
		return 0;

	REP(i,n-1){
		double level = 1.0*(sum[i]+score+total)/(i+2);
		//cout << level << " " << sc[i+1] << endl;
		if (level <= sc[i+1])
			return (level-score)/total;
	}
}

void solve_test(){
	results.resize(n);
	REP(i,n)
		results[i] = solve_test(i);
}

void dump_sol(int i){
	cout << "Case #" << i << ": ";
	cout << fixed;
	REP(i,n-1)
		cout << 100*results[i] << " ";
	cout << 100*results[n-1] << endl;
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
