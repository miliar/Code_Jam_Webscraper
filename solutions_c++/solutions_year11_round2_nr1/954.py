//head               
#include <cstdlib>   
#include <cstring>   
#include <memory>    
#include <cstdio>    
#include <fstream>   
#include <iostream>  
#include <cmath>     
#include <string>    
#include <sstream>   
#include <stack>     
#include <queue>     
#include <vector>    
#include <set>       
#include <map>       
#include <algorithm> 
#include <deque>     
#include <list>      
#include <climits>   
                     
using namespace std; 

typedef long long LL;
//typedef __int64 LL;
#define make_pari MP
typedef pair<int, int> PII;

inline int nextInt() { 
    char ch; 
    int val = 0; 
    while (ch = getchar(), ch == ' ' || ch == '\n') ; 
    if (ch == EOF) { 
        exit(0); 
    } 
    int ope = 1;
    if (ch == '-') {
        ope = 0;
    }
    else {
        val = ch - '0'; 
    }
    while (ch = getchar(), ch != ' ' && ch != '\n') { 
        val = val * 10 + ch - '0'; 
    } 
    return ope ? val : -val; 
}

const int MAXN = 128;
struct Node {
    double WP;
    double OWP;
    double OOWP;
    double RPI() {
        return 0.25 * WP + 0.5 * OWP + 0.25 * OOWP;
    }
}que[MAXN];

char ar[MAXN][MAXN];

int main () {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T = nextInt();
    for (int nCase = 1; nCase <= T; ++nCase) {
        int N = nextInt();
        for (int i = 0; i < N; ++i) {
            scanf("%s", ar[i]);
            int cnt = 0, ret = 0;
            for (int j = 0; j < N; ++j) {
                if (ar[i][j] == '.') continue;
                ++ret; 
                if (ar[i][j] == '1') ++cnt;
            }
            if (cnt == 0) que[i].WP = 0.0;
            else que[i].WP = cnt *1.0 / ret;
        }
        for (int i = 0; i < N; ++i) {
            double OWP = 0.0;
            int ret = 0;
            for (int j = 0; j < N; ++j) {
                if (ar[i][j] == '.') continue;
                ++ret; 
                double WP = 0.0;
                int cnt = 0;
                for (int k = 0; k < N; ++k) {
                    if (k != i && ar[j][k] != '.') {
                        ++cnt; WP += ar[j][k] == '1';
                    }
                }
                if (cnt == 0) WP = 0.0;
                else WP = WP / cnt;
                OWP += WP;
            }
            que[i].OWP = OWP *1.0 / ret;
        }
        for (int i = 0; i < N; ++i) {
            double OOWP = 0.0;
            int ret = 0;
            for (int j = 0; j < N; ++j) {
                if (ar[i][j] == '.') continue;
                ++ret; OOWP += que[j].OWP;
            }
            que[i].OOWP = OOWP * 1.0 / ret;
        }
        printf("Case #%d:\n", nCase);
        for (int i = 0; i < N; ++i) 
            printf("%.6lf\n", que[i].RPI());
        
    }
    return 0;
}