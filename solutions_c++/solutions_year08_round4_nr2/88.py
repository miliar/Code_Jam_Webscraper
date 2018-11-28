/**********************************************************************
Author: WHU_GCC
Created Time: 2008年08月03日 星期日 00时57分21秒
File Name: gcj_b.cpp
Description: 
**********************************************************************/
#include <iostream>
using namespace std;
#define out(x) (cout << #x << ": " << x << endl)
const int maxint = 0x7FFFFFFF;
template <class T> void get_max(T &a, const T &b) {b > a ? a = b : 1;}
template <class T> void get_min(T &a, const T &b) {b < a ? a = b : 1;}
int main() {
    int ca;
    int n, m, a;
    int T = 1;
    freopen("gcj_b.out", "w", stdout);
    for (scanf("%d", &ca); ca--;) {
        printf("Case #%d: ", T++);
        scanf("%d%d%d", &n, &m, &a);
        for (int x1 = 0; x1 <= n; x1++)
            for (int y1 = 0; y1 <= m; y1++)
                for (int x2 = 0; x2 <= n; x2++) {
/*                    if (x1 != 0) {
                        int t = a + x2 * y1;
                        if (t % x1 == 0) {
                            if (t / x1 <= m) {
                                printf("%d %d %d %d %d %d\n", 0, 0, x1, y1, x2, t / x1);
                                goto end;
                            }   
                        }
                    }
*/
                    for (int y2 = 0; y2 <= m; y2++) {
                        if (abs(x1 * y2 - x2 * y1) == a) {
                                printf("%d %d %d %d %d %d\n", 0, 0, x1, y1, x2, y2);
                                goto end;
                        }
                    }
                }
        printf("IMPOSSIBLE\n");
        end:;
    }
    return 0;
}

