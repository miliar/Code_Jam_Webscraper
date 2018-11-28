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

const int N = 128;
char str[N][N];
int n, m;

bool is_ok(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m && str[x][y] == '#';
}

void slove() {
    n = nextInt(), m = nextInt();
    for (int i = 0; i < n; ++i) {
        scanf("%s", str[i]);
    }
    bool flag = true;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (str[i][j] == '#') {
                if (is_ok(i + 1, j) && is_ok(i, j + 1) && is_ok(i + 1, j + 1)) {
                    str[i][j] = '/'; str[i][j+1] = '\\';
                    str[i+1][j] = '\\'; str[i+1][j+1] = '/';
                }
                else flag = false;          
            }
        }
    }
    puts("");
    if (!flag) puts("Impossible");
    else {
        for (int i = 0; i < n; ++i) {
            puts(str[i]);
        }
    }
}

int main () {
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T = nextInt();
    for (int nCase = 1; nCase <= T; ++nCase) {
        printf("Case #%d:", nCase);
        slove();
    }
    return 0;
}