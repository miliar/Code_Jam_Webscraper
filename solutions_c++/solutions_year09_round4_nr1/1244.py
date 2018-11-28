// BEGIN CUT HERE

// END CUT HERE
#line 5 "PolygonCover.cpp"

/////////////////////////////////////////////////////////////////////////////////////////////////
//       JUST SOME BASIC STUFF
/////////////////////////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define FOR(i,m,n) for((i)=(m);(i)<(n);(i)++)
#define FORE(i,m,n) for((i)=(m);(i)<=(n);(i)++)
#define _FORIT(it, b, e) for (__typeof(b) it = (b); it != (e); it++)
#define FORIT(x...) _FORIT(x)
#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SI(a) ((a).size())
#define PB push_back
#define MP make_pair
#define CLR(a,v) memset((a),(v),sizeof(a))
#define SORT(v) sort(ALL(v))
#define UNIQUE(v) SORT(v),(v).resize(unique(ALL(v))-(v).begin())


inline string ITOA(int a) {
    char c[500]; sprintf(c, "%d", (a)); return string(c);
}

typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef vector<VD> VVD;
typedef vector<VS> VVS;
typedef pair<int,int> PII;
typedef signed long long i64;
typedef unsigned long long u64;

#define EPS 1E-9
#define INF 0x3F3F3F3F
#define DINF 1E16
#define NULO -1
#define PI 3.1415926535897932384626433832795

inline int cmp(double x, double y = 0, double tol = EPS) {
    return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

VS tokenize(string s, string ch) {
    VS ret;
    for(int p = 0, p2; p < SI(s); p=p2+1) {
        p2 = s.find_first_of(ch, p);
        if(p2==-1) p2 = SI(s);
        if(p2-p > 0) ret.PB(s.substr(p, p2-p));
    }
    return ret;
}

VI tokint(string s, string ch) {
    int i;
    VI ret; VS t = tokenize(s, ch);
    FOR(i,0,SI(t)) ret.PB(atoi(t[i].c_str()));
    return ret;
}

struct mapper {
  map<string,int> m; VS v;
  void reset() { v.clear(); m.clear(); }
  int size() { return SI(v); }
  int get(string str) {
    if (!m.count(str)) { m[str]=SI(v); v.PB(str); }
    return m[str];
  }
  string get(int i) { return v[i]; }
};

/////////////////////////////////////////////////////////////////////////////////////////////////
//        STUFF ENDS HERE
/////////////////////////////////////////////////////////////////////////////////////////////////

int mat[8][8];
int n;

bool check(int p[]) {
    int i, j;
    FOR(i,0,n) FOR(j,i+1,n) {
        if (mat[p[i]][j]==1) return false;
    }
    return true;
}

/*******************************************************************************
 * Calcula o menor número de trocas com o bubblesort e retorna o vetor ordenado
 * em O(nlogn) pelo mergesort.
 */
long long mergecount (vector<int> &a) {
    long long count = 0;
    int i, j, k, n = SI(a);
    if (n <= 1) return 0; 
    vector<int> b(a.begin(), a.begin()+n/2);
    vector<int> c(a.begin()+n/2, a.end());
    count += mergecount(b); count += mergecount(c); 
    for  (i = j = k = 0 ; i < n; ++i)
        if  (k == c.size()) a[i] = b[j++];
        else if  (j == b.size()) a[i] = c[k++];
        else if  (b[j] <= c[k]) a[i] = b[j++];
        else a[i] = c[k++], count += n/2-j;
    return count;
}


int main() {

    int CASES, TEST;
    int perm[8];
    int i, j, k, m, mini;
    char ch;
    
    scanf("%d", &TEST);
    FORE(CASES,1,TEST) {
        printf("Case #%d: ", CASES);
        scanf("%d ", &n);
        FOR(i,0,n) { 
            FOR(j,0,n) { 
                ch = getchar(); mat[i][j] = ch-'0'; 
            }
            getchar();
        }
        FOR(i,0,n) perm[i] = i;
        mini = INF;
        do {
            if (check(perm)) { VI v(perm, perm+n);  m = mergecount(v); mini<?=m; }
        } while (next_permutation(perm, perm+n));
        printf("%d\n", mini);
    }
    return 0;
}
