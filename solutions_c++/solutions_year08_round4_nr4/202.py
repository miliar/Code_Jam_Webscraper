/**********************************************************************
Author: momodi
Created Time:  2008-8-3 0:31:44
Modified Time: 2008-8-3 0:57:20
File Name: d.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define out(x) printf("%s: %I64d\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}

char buf[1010];
char des[1010];
int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        int k;
        scanf("%d\n", &k);
        gets(buf);
        int a[10];
        for (int i = 0; i < k; ++i) {
            a[i] = i;
        }
        int len = strlen(buf);
        int ans = maxint;
        do {
            for (int i = 0; i < len; i += k) {
                for (int j = 0; j < k; ++j) {
                    des[i + j] = buf[i + a[j]];
                }
            }
            int cnt = 1;
            for (int i = 1; i < len; ++i) {
                if (des[i] != des[i - 1]) {
                    ++cnt;
                }
            }
            get_min(ans, cnt);
        } while (next_permutation(a, a + k));
        printf("%d\n", ans);
    }
    return 0;
}

