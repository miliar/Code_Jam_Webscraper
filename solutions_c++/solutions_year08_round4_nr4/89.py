/**********************************************************************
Author: WHU_GCC
Created Time: 2008年08月03日 星期日 01时19分43秒
File Name: gcj_d.cpp
Description: 
**********************************************************************/
#include <iostream>
using namespace std;
#define out(x) (cout << #x << ": " << x << endl)
const int maxint = 0x7FFFFFFF;
template <class T> void get_max(T &a, const T &b) {b > a ? a = b : 1;}
template <class T> void get_min(T &a, const T &b) {b < a ? a = b : 1;}

int k;
char s[1010];
char ss[1010];

int p[10];

int main() {
    int ca;
    int T = 1;
    freopen("gcj_d.out", "w", stdout);
    for (scanf("%d", &ca); ca--;) {
        printf("Case #%d: ", T++);
        scanf("%d", &k);
        scanf("%s", s);
        for (int i = 0; i < k; i++)
            p[i] = i;
        int l = strlen(s);
        int ans = maxint;
        do {
            for (int i = 0; i < l; i++) {
                int a = i / k;
                int b = i % k;
                ss[i] = s[a * k + p[b]];
            }
            ss[l] = 0;
            int tmp = 1;
            for (int i = 1; i < l; i++) {
                if (ss[i] != ss[i - 1])
                    tmp++;
            }
            get_min(ans, tmp);
        } while (next_permutation(p, p + k));
        printf("%d\n", ans);
    }
    return 0;
}

