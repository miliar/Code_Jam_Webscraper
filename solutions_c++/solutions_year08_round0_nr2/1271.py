/**********************************************************************
Author: WHU_GCC
Created Time: 2008年07月17日 星期四 22时27分05秒
File Name: gcj_b.cpp
Description: 
**********************************************************************/
#include <iostream>
using namespace std;
#define out(x) (cout << #x << ": " << x << endl)
const int maxint = 0x7FFFFFFF;
template <class T> void get_max(T &a, const T &b) {b > a ? a = b : 1;}
template <class T> void get_min(T &a, const T &b) {b < a ? a = b : 1;}

int na, nb, t;
int sa[110], ea[110], sb[110], eb[110];

int at_a[24 * 60 + 10], at_b[24 * 60 + 10];

int main() {
    int ca, c = 1;
    for (scanf("%d", &ca); ca--;) {
        printf("Case #%d: ", c++);

        scanf("%d", &t);
        scanf("%d%d", &na, &nb);
        for (int i = 0; i < na; i++) {
            int t1, t2, t3, t4;
            scanf("%d:%d%d:%d", &t1, &t2, &t3, &t4);
            sa[i] = t1 * 60 + t2;
            ea[i] = t3 * 60 + t4;
        }
        for (int i = 0; i < nb; i++) {
            int t1, t2, t3, t4;
            scanf("%d:%d%d:%d", &t1, &t2, &t3, &t4);
            sb[i] = t1 * 60 + t2;
            eb[i] = t3 * 60 + t4;
        }
        
        memset(at_a, 0, sizeof(at_a));
        memset(at_b, 0, sizeof(at_b));
        
        int cnt_a = 0, cnt_b = 0;
        for (int i = 0; i < 24 * 60; i++) {
            for (int j = 0; j < na; j++)
                if (sa[j] == i) {
                    if (at_a[i] > 0) {
                        at_b[ea[j] + t]++;
                        at_a[i]--;
                    }
                    else {
                        at_b[ea[j] + t]++;
                        cnt_a++;
                    }
                }
            for (int j = 0; j < nb; j++)
                if (sb[j] == i) {
                    if (at_b[i] > 0) {
                        at_a[eb[j] + t]++;
                        at_b[i]--;
                    }
                    else {
                        at_a[eb[j] + t]++;
                        cnt_b++;
                    }
                }
            if (at_a[i] > 0)
                at_a[i + 1] += at_a[i];
            if (at_b[i] > 0)
                at_b[i + 1] += at_b[i];
        }
        printf("%d %d\n", cnt_a, cnt_b);
    }
    return 0;
}

