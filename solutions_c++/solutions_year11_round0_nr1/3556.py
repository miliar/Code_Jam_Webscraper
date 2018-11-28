/* 
 * File:   main.cpp
 * Author: gaia
 *
 * Created on May 7, 2011, 10:09 AM
 */

#include <cstdlib>
#include <stdio.h>
#include <algorithm>
using namespace std;

/*
 * 
 */
int p1, p2, t1, t2, c2;
char c1[3];

int main(int argc, char** argv) {

    int test, n, cas(1);
    freopen("/home/gaia/Downloads/A-large.in","r",stdin);
    freopen("/home/gaia/Downloads/out","w",stdout);
    scanf("%d", &test);
    while (test--) {
        scanf("%d", &n);
        //printf("n---> %d\n",n);
        p1 = p2 = 1;
        t1 = t2 = 0;
        //printf("%d  %d  %d   %d\n",p1,p2, t1, t2);
        for (int i = 0; i < n; ++i) {
            scanf("%s%d", c1,   &c2);
            int tp = c2;
           // printf("%s   %d\n",c1,c2);
            if(c1[0] == 'O'){
                int t = abs(tp-p1);
                t1 += t + 1;
                p1 = tp;
                if(t1 <= t2)     t1 = t2 + 1;
            }else{
                int t = abs(tp-p2);
                t2 += t + 1;
                p2 = tp;
                if(t2 <= t1)     t2 = t1 + 1;
            }
            //printf("%d   %d   %d   %d\n",p1,p2,t1,t2);
        }
        printf("Case #%d: %d\n",cas++,max(t1,t2));
    }
    return 0;
}

