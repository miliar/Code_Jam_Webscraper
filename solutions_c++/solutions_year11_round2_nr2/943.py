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

const int MAXN = 256;

struct Node {
    int pos, nums;
}ar[MAXN];

bool operator <(Node a, Node b) {
    return a.pos < b.pos;
}

struct node {
    double st, ed;
    double cost;
    int index;
}vec[MAXN];

int main () {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    int T = nextInt();
    for (int nCase = 1; nCase <= T; ++nCase) {
        int C = nextInt(), D = nextInt();
        for (int i = 0; i < C; ++i) {
            ar[i].pos = nextInt();
            ar[i].nums = nextInt();
        }
        sort(ar, ar + C);
        double low = 0.0, high = INT_MAX;
        while (high - low > 1e-6) {
            double mid = (low + high) / 2.0;
            for (int i = 0; i < C; ++i) {
                if (i == 0) {
                    vec[i].st = ar[i].pos - mid;
                    vec[i].ed = (ar[i].nums - 1) * D + vec[i].st;
                }
                else {
                    if (ar[i].pos - mid > vec[i-1].ed + D) {
                        vec[i].st = ar[i].pos - mid;
                        vec[i].ed = (ar[i].nums - 1) * D + vec[i].st;
                    }
                    else {
                        vec[i].st = vec[i-1].ed + D;
                        vec[i].ed = (ar[i].nums - 1) * D + vec[i].st;
                    }
                }
            }
            bool flag = true;
            for (int i = 0; i < C; ++i) {
                double c1 = fabs(vec[i].st - ar[i].pos);
                double c2 = fabs(vec[i].ed - ar[i].pos);
                double c = max(c1, c2);
                if (c > mid) flag = false;
            }
            if (flag) {
                high = mid;
            }
            else {
                low = mid;
            }
        }
        int ans = (low + high) * 10;
        printf("Case #%d: %.6lf\n", nCase, ans / 20.0);
    }
    return 0;
}