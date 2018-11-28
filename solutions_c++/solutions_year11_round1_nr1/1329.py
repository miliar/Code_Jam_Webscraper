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

int main () {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T = nextInt();
    for (int nCase = 1; nCase <= T; ++nCase) {
        LL N, PD, PG;
        scanf("%lld%lld%lld", &N, &PD, &PG);
        if (PG == 0 && PD == 0) {
            printf("Case #%d: %s\n", nCase, "Possible");
            continue;
        }
        else if (PG == 0) {
            printf("Case #%d: %s\n", nCase, "Broken");
            continue;
        }
        LL D = 1;
        bool flag = false;
        while (D <= N) {
            if (D * PD % 100 != 0) {
                ++D;
                continue;
            }
            LL P = D * PD;
            LL G = P / PG;
            while (G < D) ++G;
            while (G < INT_MAX && G * PG % 100 != 0) 
                ++G;
            if (G * PG % 100 == 0 && G * PG >= P && (G * (100 - PG) >= (D * 100 - P))) {
                flag = true;
                break;
            }
            ++D;
        }
        printf("Case #%d: %s\n", nCase, flag ? "Possible" : "Broken");
    }
    return 0;
}