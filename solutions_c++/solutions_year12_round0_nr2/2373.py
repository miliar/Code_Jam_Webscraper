/* 
 * File:   dance.cc
 * Author: vivek
 *
 * Created on April 14, 2012, 9:31 PM
 */

#include <cstdlib>
#include <cstdio>
using namespace std;
#define MAX_SIZE 101

/*
 * 
 */
int main(int argc, char** argv) {
    int t, i = 0, p, s, ans, n, stable, rem, done = 0, special = 0;
    int score = 0, j, k1, k2, k3, diff1, diff2, diff3;
    scanf("%d", &t);
    while (t--) {
        ++i;
        ans = 0;
        scanf("%d", &n);
        scanf("%d", &s);
        scanf("%d", &p);
        for (j = 0; j < n; j++) {
            scanf("%d", &score);
            rem = score / 3;
            done = 0;
            special = 0;
            for (k1 = rem - 2; k1 <= rem + 2; k1++) {
                if (k1 < 0)
                    continue;
                for (k2 = rem - 2; k2 <= rem + 2; k2++) {
                    if (k2 < 0)
                        continue;
                    diff1 = abs(k1 - k2);
                    if (diff1 > 2) {
                        continue;
                    }
                    for (k3 = rem - 2; k3 <= rem + 2; k3++) {
                        if (k3 < 0)
                            continue;
                        diff2 = abs(k2 - k3);
                        diff3 = abs(k1 - k3);
                        if (diff2 > 2) {
                            continue;
                        }
                        if (diff3 > 2) {
                            continue;
                        }
                        if ((k1 + k2 + k3) == score) {
                            if ((diff3 < 2) && (diff2 < 2) && (diff1 < 2)) {
                                if (k1 >= p || k2 >= p || k3 >= p) {
                                    //printf("%d %d %d = %d %d %d %d\n",k1,k2,k3,score,diff1,diff2,diff3);
                                    done = 1;
                                    ans++;
                                    goto endk1;
                                }
                            } else {
                                if (k1 >= p || k2 >= p || k3 >= p) {
                                    special = 1;
                                }
                            }
                        }
                    }
                }

            }
            if (done == 0 && special && s > 0) {
                ans++;
                s--;
            }
endk1:
            ;
        }
        printf("Case #%d: %d\n", i, ans);
    }
    return 0;
}

