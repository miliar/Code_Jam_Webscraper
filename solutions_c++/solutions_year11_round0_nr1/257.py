#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define f(i, a, b) for(int i = a; i < b; i++)
#define rep(i, n)  f(i, 0, n)

int p1[201], p2[201], o1[201], o2[201], n1, n2;

int main(){

    int T; scanf("%d", &T); for(int test = 1; test <= T; test++) {

        printf("Case #%d: ", test);

        int n; scanf("%d ", &n);
        n1 = n2 = 0;

        rep(i, n) {

            char c; int p;
            scanf("%c %d ", &c, &p);

            if(c == 'O') {
                p1[n1] = p;
                o1[n1] = i;
                n1++;
            }
            else{
                p2[n2] = p;
                o2[n2] = i;
                n2++;
            }
        }

        o1[n1] = o2[n2] = 1 << 30;

        int res = 0;
        int x1 = 1, x2 = 1;
        int i1 = 0, i2 = 0;

        while(i1 < n1 || i2 < n2) {

            int b1 = (p1[i1] == x1) && (i1 < n1);
            int b2 = (p2[i2] == x2) && (i2 < n2);
            int a1 = 1, a2 = 1;

            if(b1 && b2)
                if(o1[i1] < o2[i2]) {
                    i1++;
                    a1 = 0;
                }
                else {
                    i2++;
                    a2 = 0;
                }
            else if(b1 && o1[i1] < o2[i2]) {
                i1++;
                a1 = 0;
            }
            else if(b2 && o2[i2] < o1[i1]) {
                i2++;
                a2 = 0;
            }

            if(a1) {
                if(x1 < p1[i1]) x1++;
                else if(x1 > p1[i1]) x1--;
            }
            if(a2) {
                if(x2 < p2[i2]) x2++;
                else if(x2 > p2[i2]) x2--;
            }

            res++;
        }

        printf("%d\n", res);

    }
}
