#include <vector>
#include <iostream>
#include <sstream>
#include <math.h>
#include <sys/time.h>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <cstring>
#include <string>

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

string input;
string result;

char google[] = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
char original[] = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
char trans[256];

void init(){
	REP(i,256) trans[i] = '\0';
	REP(i,strlen(google))
		trans[google[i]] = original[i];
	trans['q'] = 'z';
	trans['z'] = 'q';
	trans['e'] = 'o';
	trans['y'] = 'a';
	
}

void read_test(){
    getline(cin,input);
}

void solve_test(){
	result = input;
	REP(i,SIZE(input))
		result[i] = trans[input[i]];
}

void dump_sol(int i){
	cout << "Case #" << i << ": ";
	cout << result << endl;
    cout.flush();
}

int main(int argc, char *argv[]){
	init();
	cin >> tests;
	getline(cin,input);
	for(int i=0; i < tests; i++){
		read_test();
    	solve_test();
	    dump_sol(i+1);
	}
}
