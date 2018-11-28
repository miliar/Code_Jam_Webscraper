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
#define VD			vector<double>
#define VS          vector<string >
#define VII        vector<II >
#define VDD         vector< DD >

#define DUMP(a)       cerr << #a << ": " << a << endl;

using namespace std;

char msg[100];

vector<char> data;

void read_test(){
	cin.getline(msg,1000);
	data.clear();
	data.PB('0');
	REP(i,strlen(msg))
		data.PB(msg[i]);
}


void solve_test(){
	next_permutation(ALL(data));
}

void dump_sol(int i){
	cout << "Case #" << i << ": ";
	FOR(i,(data[0] != '0')? 0 : 1,SIZE(data))
		cout << data[i];
	cout << endl;
}

int main(){
	int tests;
	cin >> tests;
	cin.getline(msg,1);
	for(int i=0; i < tests; i++){
		read_test();
		solve_test();
		dump_sol(i+1);
	}
}
