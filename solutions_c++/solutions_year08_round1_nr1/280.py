/**********************************************************************
Author: cominde
Created Time:  Sat 26 Jul 2008 09:10:41 AM CST
Modified Time: Sat 26 Jul 2008 09:18:09 AM CST
File Name: a.cpp
Description: 
**********************************************************************/
#include <iostream>
using namespace std;
#define out(x) printf("%s: %lld\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}
int main() {
    int n;
    freopen("a.out", "w", stdout);
    long long num0[1000], num1[1000];
    int kase;
    scanf("%d", &kase);
    for (int ii = 1; ii <= kase; ++ii){
        printf("Case #%d: ", ii);
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i){
            scanf("%lld", &num0[i]);
        }
        for (int i = 1; i <= n; ++i){
            scanf("%lld", &num1[i]);
        }
        sort(num0 + 1, num0 + 1 + n);
        sort(num1 + 1, num1 + 1 + n);
        long long sum = 0;
        for (int i = 1; i <= n; ++i){
            sum += num0[i] * num1[n - i + 1];
        }
        printf("%lld\n", sum);
    }
    return 0;
}

