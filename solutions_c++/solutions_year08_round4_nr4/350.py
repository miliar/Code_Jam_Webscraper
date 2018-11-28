#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;

#define FR(i, n) for (int i=0; i<n; i++)
#define FOR(i,a,b) for (int i=a; i<=b; i++)
#define FI first
#define SE second
#define tmax(x, y) (((x)>(y))? (x):(y))
#define tmin(x, y) (((x)<(y))? (x):(y))
#define myabs(x) (((x)>0)? (x):(-(x)))
#define INF 1000000000

string i2s(int x) { ostringstream o; o<<x; return o.str(); }
int s2i(string s) { int x; istringstream i(s); i>>x; return x; }

typedef pair<int, int> II;
typedef vector<int> VI;
typedef long long LL;

int res;
int ntest, test;
int k;
string st;
int p[10];

void read_in() {
     cin >> k;getline(cin, st);
     getline(cin, st);     
     //cout << st << endl;         
}

int tinh() {
    int ret = 0;
    string s2 = string(st);
    int n = s2.size();
    FR(i, n/k) {
      FR(j, k) s2[i*k + j] = st[i*k + p[j]];
    }
    
    FOR(i,1,n) if (s2[i] != s2[i-1]) ret++;   
    
    return ret;
}

void process() {
     FR(i, k) p[i] = i;
     res = INF;
     do {
         res <?= tinh();
     }
     while ( next_permutation (p,p+k) );
}

int main() {
    freopen("D-small-attempt0.in", "rt", stdin);
    freopen("d.out", "wt", stdout);
    
    scanf("%d", &ntest);
    FR(test, ntest) {
        read_in();
        cout << "Case #" << test+1<<": ";
        process();        
        cout << res<<endl;
    }
    
    return 0;
}
