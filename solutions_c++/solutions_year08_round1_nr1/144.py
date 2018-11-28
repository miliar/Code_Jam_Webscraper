/**********************************************************************
Author: chaeyeon
Created Time:  Sat 26 Jul 2008 09:05:40 AM CST
Modified Time: Sat 26 Jul 2008 09:09:59 AM CST
File Name: a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(x) printf("%s: %lld\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}
int a[1000], b[1000];
int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d", a + i);
        }
        for (int i = 0; i < n; ++i) {
            scanf("%d", b + i);
        }
        sort(a, a + n);
        sort(b, b + n);
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += a[i] * b[n - i - 1];
        }
        printf("%lld\n", ans);
    }
    return 0;
}

