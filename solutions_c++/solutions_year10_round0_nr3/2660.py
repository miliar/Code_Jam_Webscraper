#include <iostream>
#include <stdio.h>

#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for (int i = a; i < b; i++)

using namespace std;

long long int gsum[1000], lsum[1000];
int gend[1000], g[1000], ls[1000];
bool lactive[1000];

int main() {
    int t, n, sum, pos;
    long long int ans;
    long int r, k, l, prod;
    bool flag;

    scanf ("%d", &t);

    REP(z,t) {
        scanf ("%ld %ld %d", &r, &k, &n);
        REP(i,n) scanf("%d", &g[i]);

        REP(i,n) {
            lsum[i] = 0;
            lactive[i] = 0;
            ls[i] = 0;
            gsum[i] = 0;
            sum = 0;
            flag = 1;

            FOR(j,i,n) {
                if (sum + g[j] < k) {
                    sum += g[j];
                    gsum[i] = sum;
                    gend[i] = j;
                }
                else if (sum + g[j] == k) {
                    sum += g[j];
                    gsum[i] = sum;
                    gend[i] = j;
                    flag = 0;
                    break;
                }
                else if (sum + g[j] > k) {
                    flag = 0;
                    break;
                }
            }

            if(flag)
            FOR(j,0,i) {
                if (sum + g[j] < k) {
                    sum += g[j];
                    gsum[i] = sum;
                    gend[i] = j;
                }
                else if (sum + g[j] == k) {
                    sum += g[j];
                    gsum[i] = sum;
                    gend[i] = j;
                    break;
                }
                else if (sum + g[j] > k) {
                    break;
                }
            }
        }

        pos = 0; ans = 0;
        for (l = 1; l <= r; l++) {
//            cout << "Loop: " << l << endl;
            if (lactive[pos] == 0) {
                lactive[pos] = 1;
            }
            else {
 //               cout << "Debug " << pos << "   " << lsum[pos] << "   " << ans << endl;
                prod = (r - l + 1)/ls[pos];
                ans += prod * lsum[pos];

                prod = (r - l + 1)%ls[pos];
                REP(i,prod) {
                    ans += gsum[pos];
                    pos = (gend[pos] < n-1)? gend[pos]+1: 0;
                }
                break;
            }

            REP(i,n) if (lactive[i]) {
                        lsum[i] += gsum[pos];
                        ls[i]++;
            }

            ans += gsum[pos];
            pos = (gend[pos] < n-1)? gend[pos]+1: 0;
        }

        printf ("Case #%d: %lld\n", z+1, ans);
    }

    return 0;
}
