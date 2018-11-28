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
#define MP make_pair
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
//最大公约数
template<typename type>
type gcd(type a, type b) {
    return b ? gcd(b, a % b) : a;
}

//最小公倍数
template<typename type>
type lcm(type a, type b) {
    return a / gcd(a, b) * b;
}
const int N = 10086;
int ar[N];

void slove() {
    //printf("%d %d\n", lcm(20, 10), gcd(20, 10));
    int n, l, h;
    scanf("%d %d %d", &n, &l, &h);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &ar[i]);
    }
    bool can = false;
    for (int i = l; i <= h; ++i) {
        int j = 0;
        for (j = 0; j < n; ++j) {
            if (!(i % ar[j] == 0 || ar[j] % i == 0)) break;
        }
        if (j == n) {
            can = true;
            printf(" %d\n", i);
            break;
        }
    }
    if(!can) puts(" NO");
}

int main () {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T = nextInt();
    for (int nCase = 1; nCase <= T; ++nCase) {
        printf("Case #%d:", nCase);
        slove();
    }
    return 0;
}