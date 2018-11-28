#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FORD(i,a,b) for(int i=(int)(a);i>=(int)(b);--i)
#define FORC(i,a,b,n) for(int i=(int)(a);i<=(int)(b);i+=(n))
#define FORDC(i,a,b,n) for(int i=(int)(a);i>=(int)(b);i-=(n))
#define FOREACH(it,c) for(__typeof((c).begin())it=(c).begin();it!=(c).end();++it)
#define CLEAR(t) memset((t),0,sizeof(t))
#define ALL(c) (c).begin(),(c).end()
#define SIZE(x) ((int)((x).size()))
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef vector<string> VS;
typedef long long LL;
#define INF 0x3f3f3f3f
#define EPS 1e-8
template<class T, class U> T CAST(U x) { T y; ostringstream a; a<<x; istringstream b(a.str()); b >> y; return y; }
template<class T> vector<T> SPLIT(string s, string x=" ") { vector<T> r; REP(i, SIZE(s)) { string c; while(i < SIZE(s) && x.find(s[i]) == string::npos) c += s[i++]; if (SIZE(c)) r.push_back(CAST<T>(c)); } return r; }

map<string, int> m; int ids;
vector<int> child[20005];

int id(string s) {
    if (m.find(s) != m.end()) return m[s];
    else return m[s] = ids++;
}

int dfs(int node) {
    vector<int> v;
    FOREACH(c, child[node]) v.push_back(dfs(*c));
    sort(ALL(v)); reverse(ALL(v));
    if (SIZE(v) == 0) return 0;
    if (v[0] == 0) return 1;
    int need = v[0], available = v[0]-1;
    FOR(i, 1, SIZE(v)-1) {
        if (v[i] > available) need += (v[i]-available), available = v[i];
        if (v[i] != 0) available--;
    }
    if (available == 0) need++;
    return need;
}

int main() {
    FILE *fin = fopen("A.in", "r"), *fout = fopen("A.out", "w");

    int C; fscanf(fin, "%d", &C); REP(c, C) {
        ids = 0; m = map<string, int>();
        CLEAR(child);
        int N; fscanf(fin, "%d", &N);
        //each mix
        REP(i, N) {
            char mix[25]; fscanf(fin, "%s", mix);
            int m = id(string(mix));
            int M; fscanf(fin, "%d", &M);
            //each ingredient
            REP(j, M) {
                char str[25]; fscanf(fin, "%s", str);
                int n = id(string(str));
                child[m].push_back(n);
            }
        }
        fprintf(fout, "Case #%d: %d\n", c+1, dfs(0));
    }
}
