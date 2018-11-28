/*
 * =====================================================================================
 *
 *       Filename:  B.cpp
 *
 *    Description:  B
 *
 *        Version:  0.0
 *        Created:  05/08/2010 09:45:11 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Jianfei Wang (thinXer), me@thinxer.com
 *        Company:  Tsinghua University
 *
 * =====================================================================================
 */

#include	<iostream>
using namespace std;

#define MAXN 1000
typedef long long int64;

int r,k,n;
int d[MAXN];
int64 sum[MAXN];
int next[MAXN];

int64 solve() {
    int64 ret = 0;
    cin >> r >> k >> n;
    
    int64 s = 0;
    for (int i=0; i<n; i++) {
        cin >> d[i];
        s += d[i];
    }

    if (s <= k) {
        ret = r * s;
    } else {
        int i = 0, j = 0;
        for (i=0; i<n; i++) {
            sum[i] = 0;
            j = i;
            while (sum[i] + d[j] <= k) {
                sum[i] += d[j];
                j = (j+1) % n;
            }
            next[i] = j;
        }
        int a = 0;
        while (r-->=1) {
            ret += sum[a];
            a = next[a];
        }
    }
    return ret;

}

int main() {
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        cout << "Case #" << (i+1) << ": " << solve() << endl;
    }
    return 0;
}
