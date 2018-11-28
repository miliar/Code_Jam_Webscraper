#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
double p[110], op[110], oop[110];
char s[111][111];
char mm[111][111];
int n;
int have1(int w) {
    int ret = 0;
    for (int j = 1; j <= n; ++j) if (mm[w][j] == '1') ++ret;
    return ret;
}

int have(int w) {
    int ret = 0;
    for (int j = 1; j <= n; ++j) if (mm[w][j] != '.') ++ret;
    return ret;
}


int caloop(double f[]) {
    
    
    for (int j = 1; j <= n; ++j) {
        double zi = 0;
        double mu = 0;
        for (int i = 1; i <= n; ++i) if (i != j && (s[j][i] != '.')) {
            mu = mu + 1;
            zi = zi + op[i];
        }
        if (fabs(mu) < 0.0000001) f[j] = 0; else  f[j] = zi / mu;      
    }
    return 0;   
}

int cal(double f[]) {


    for (int j = 1; j <= n; ++j) {
        if (have(j) == 0) f[j] = 0; else    f[j] = have1(j) * 1.00 / have(j);
    }
    return 0;   
}


int calop(double f[]) {

    double tt[110];
    for (int j = 1; j <= n; ++j) {

        for (int k = 0; k < 111; ++k) 
            for (int i = 0; i < 111; ++i) 
                mm[k][i] = s[k][i];
        for (int k = 1; k <= n; ++k) 
            for (int i = 1; i <= n; ++i) 
                if (k == j || i == j) mm[k][i] = '.';
/*for (int a1 = 1; a1 <= n; ++a1) {
    puts("");
    for (int b1 = 1; b1 <= n; ++b1) printf("%c", mm[a1][b1]);
}*/
        double zi = 0, mu = 0;
        cal(tt);
//for (int j = 1; j <= n; ++j) printf("%.2lf ", tt[j]); puts("");
        
        for (int k = 1; k <= n; ++k) if (k != j && s[j][k] != '.')  {
            zi = zi + tt[k];
            mu = mu + 1;
        }
        if (fabs(mu) < 0.0000001) f[j] = 0; else  f[j] = zi / mu;      
    }
    return 0;   
}

int main() {
    freopen("a.txt", "r", stdin);
    freopen("b.txt", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int tcas = 1; tcas <= cas; ++tcas) {
        scanf("%d", &n);
        memset(s, '.', sizeof(s));
        for (int j = 1; j <= n; ++j) scanf("%s", s[j] + 1);
        for (int j = 0; j < 111; ++j) 
            for (int k = 0; k < 111; ++k) 
                mm[j][k] = s[j][k];
        cal(p);        
        calop(op);
        caloop(oop);
//for (int j = 1; j <= n; ++j) printf("%.2lf ", p[j]);puts("");
//for (int j = 1; j <= n; ++j) printf("%.2lf ", op[j]);puts("");
//for (int j = 1; j <= n; ++j) printf("%.2lf ", oop[j]);puts("");        
        printf("Case #%d:\n", tcas);
        for (int j = 1; j <= n; ++j) 
            printf("%lf\n", (p[j]+oop[j])/4.00 + op[j]/2.00);
    }   
    return 0;
}
