/* 
 * File:   main.cpp
 * Author: xhSong
 *
 * Created on 2011年5月21日, 下午9:16
 */

#include <cstdlib>
#include <cstdio>
#include <algorithm>
#define eps 1e-8

using namespace std;

struct region {
    int mid, m;
    double left, right, time;
    bool operator <(const region &a)const {
        return mid;
    }
}a[200];

bool check(int n, double time) {
    double right = -1e30;
    for(int i = 0; i < n; ++i) {
        if(time < a[i].time) {
            return false;
        }
        if(right < a[i].left) {
            double moveleft = min(time - a[i].time, a[i].left - right);
            right = a[i].right - moveleft;
        } else {
            double moveright = right - a[i].left;
            if(time - a[i].time < moveright) {
                return false;
            }
            right = a[i].right + moveright;
        }
    }
    return true;
}

int main(int argc, char** argv) {
    int T;
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("b.out", "w", stdout);
    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        int n, d;
        scanf("%d%d", &n, &d);
        for(int i = 0; i < n; ++i) {
            scanf("%d%d", &a[i].mid, &a[i].m);
            a[i].time = (a[i].m - 1) * d * 0.5;
            a[i].left = a[i].mid - a[i].time - d * 0.5;
            a[i].right = a[i].mid + a[i].time + d * 0.5;
           // printf("\n%lf %lf %lf\n", a[i].left, a[i].right, a[i].time);
        }
//        sort(a, a + n);
        
        double left = 0, right = 1e20, mid;
        while(right - left > eps) {
            mid = (left + right) / 2;
            if(check(n, mid)) {
                right = mid;
            } else {
                left = mid;
            }
        }
        printf("Case #%d: %.8lf\n", t, mid);
    }
    return 0;
}


