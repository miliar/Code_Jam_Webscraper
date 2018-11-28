#include <iostream>
#include <vector>
#include <map>
#include <cctype>
#include <climits>
#include <sstream>
#include <algorithm>
#include <cassert>
#include <cstring>
#include <cstdio>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<_b; i++)
#define REP(i,n) FOR(i,0,n)

#define DEBUG 

#define NOP do {} while(0)

#if !defined(DEBUG)

#define dprintf(x...)   NOP
#define DOUT(x)         NOP
#define DCOLL(x)        NOP
#define DARR(x,n)       NOP

#else
#define DC(x) cout << "# "#x" = "
#define dprintf(x,...) printf("# " x "\n", ##__VA_ARGS__)
#define DOUT(x) DC(x) << x << endl;
#define DCOLL(x) do { DC(x);			\
        FOREACH(it,x){ cout << *it << " "; }	\
        cout << endl; } while(0)
#define DARR(x,n) do { DC(x);			\
        REP(i,n) { cout << x[i] << " "; }	\
        cout << endl; } while(0)
#endif

typedef long long ll;
typedef std::vector<ll> VL;
typedef std::vector<VL> VVL;

using namespace std;

static void solve_case(int i);

int main(void){
    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        solve_case(i+1);
    }
    return 0;
}

enum {ORANGE = 0, BLUE = 1 };

void solve_case(int cn){
    int N, color, button;
    string botname;

    int time[2] = {0,0};
    int loc[2] = {1,1};

    cin >> N;
    REP(i,N){
	cin >> botname >> button;
	color = (botname == "O") ? 0 : 1;

	int dist = button - loc[color];
	if(dist < 0)
	    dist = -dist;

	int op_color = color ^ 1;

	time[color] = max(time[color] + dist, time[op_color]) + 1;
	loc[color] = button;
    } 

    cout << "Case #" << cn << ": " << max(time[0],time[1]) << endl;
}
