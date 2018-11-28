#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

int ca, A, B, ans, len, base;
set<int> st;

int calc(int x, int l, int r) {
    int num = x;
    st.clear();
    for(int i = 0; i < len - 1; i++) {
        int t = num % 10;
        num = num / 10 + t * base;
        if(num > x && l <= num && num <= r) {
            st.insert(num);
        }
    }
    return st.size();
}

int get_len(int x) {
    int ret = 0;
    while(x) {
        ret++;
        x /= 10;
    }
    return ret;
}

int main() {
    freopen("gcj_C.out", "w", stdout);
    scanf("%d", &ca);
    for(int t = 1; t <= ca; t++) {
        scanf("%d%d", &A, &B);
        len = get_len(A);
        base = 1;
        for(int i = 1; i < len; i++) base *= 10;
        ans = 0;
        for(int i = A; i <= B; i++) {
            ans += calc(i, A, B);
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}

