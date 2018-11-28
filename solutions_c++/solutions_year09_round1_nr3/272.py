#pragma warning( disable : 4786 )
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <queue>
using namespace std;

typedef long long i64; 
typedef unsigned long long u64;
#define I64 "%lld"
#define U64 "%llu"

#define mabs(x) ((x)<0?(-(x)):(x))
#define mmin(a,b) ((a)>(b)?(b):(a))
#define mmax(a,b) ((a)<(b)?(b):(a))
#define sq(x) ((x)*(x))

#define EPS 1e-7

#define eq(a,b) (a - b < EPS && b - a < EPS) 
#define les(a, b) (b - a > EPS) 

typedef vector<int> VI; 

#define rep(i,n) for((i)=0;(i)<(n);++(i))

#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),c) != (c).end()) 

#define FOR(v, it) for(it = v.begin(); it!=v.end(); ++it)
#define foreach(vtype, v, it) for(vtype::iterator it = v.begin(); it!=v.end(); ++it)

// tostring
string itos (int i){ stringstream s; s << i; return s.str(); }
string i64tos (i64 i){ char s[51];sprintf(s,I64,i);string ss=s;return ss; }

template <class T>
void SWAP(T &x, T &y){T z=x; x=y; y=z;}

#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define dbge(x) cout << #x << " -> " << (x) << endl;

#define CLR(c, v) memset(c, v, sizeof(c))

int getInt(void){
	int d;
	scanf("%d",&d);
	return d;
}
#define INT getInt()

char InputFileNames[4][20] = {"C-sample.in", "C-small.in", "C-large.in", "C-test.in"};
char OutputFileNames[4][20] = {"C-sample.out", "C-small.out", "C-large.out", "C-test.out"};

enum{SAMPLE=0, SMALL, LARGE, TEST};

int N, C;

double memo[1<<10];

vector<int> states[11];

double go(int state){
    double &ret = memo[state];
    if(ret>-0.5)return ret;

    if(state==(1<<C)-1)return ret = 0.;

    bool found = false;
    ret = 0.;
    int c = 0;
    int t = 0;
    for(int i = 0; i<states[N].size(); ++i){
        int ns = states[N][i];
        if(ns>=(1<<C))continue;
        if((ns|state)==state){
            found = true;
            t++;
            continue;
        }

        c++;
        ret += go(state|ns);
    }

    if(t>0){
        ret = (ret + t + c) / (c); 
    }
    else{
        ret = ret / c + 1;
    }
    return ret;
}

int main (void){
    int i, j, k;
	int CUR = SMALL;
	freopen(InputFileNames[CUR], "r", stdin);
	freopen(OutputFileNames[CUR], "w", stdout);

    rep(i, 11)states[i].clear();

    for(i=0; i<(1<<10); ++i){
        int c = 0;
        rep(j, 15)if((1<<j)&i)c++;
        states[c].push_back(i);
    }


	int T = INT;
    
	for(int t=1; t<=T; ++t){
        double res = -1;
        C = INT;
        N = INT;

        rep(i, (1<<C))memo[i] = -1;
        res = go(0);

		printf("Case #%d: %.10lf\n",t,res);
	}

	return 0;
}
