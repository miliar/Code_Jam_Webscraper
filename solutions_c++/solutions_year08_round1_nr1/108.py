/**********************************************************************
Author: WHU_GCC
Created Time: 2008年07月26日 星期六 09时05分36秒
File Name: gcj_a.cpp
Description: 
**********************************************************************/
#include <iostream>
using namespace std;
#define out(x) (cout << #x << ": " << x << endl)
const int maxint = 0x7FFFFFFF;
template <class T> void get_max(T &a, const T &b) {b > a ? a = b : 1;}
template <class T> void get_min(T &a, const T &b) {b < a ? a = b : 1;}

const int maxn = 1000;

int a[maxn], b[maxn];
int n;

int main() {
    freopen("gcj_a.out", "w", stdout);
    int T;
    int c = 1;
    for (scanf("%d", &T); T--;) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        for (int i = 0; i < n; i++)
            scanf("%d", &b[i]);
        sort(a, a + n);
        sort(b, b + n);
        long long ans = 0;
        for (int i = 0; i < n; i++)
            ans += (long long)a[i] * b[n - i - 1];
        cout << "Case #" << c++ << ": ";
        cout << ans << endl;
        
    }
    return 0;
}

