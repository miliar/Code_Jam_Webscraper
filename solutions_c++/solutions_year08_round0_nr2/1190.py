/*
Author: Ahyangyi
Using Dev-Cpp with MinGW
*/

#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

struct node {
    int l, a;
    } data[400];
char x[1000], y[1000];
int tt;

bool operator < (const node& a, const node& b) {
    return a.l < b.l;
    }

int convert (char* s) {
    return (s[0]-'0')*600+(s[1]-'0')*60+(s[3]-'0')*10+(s[4]-'0');
    }

int main () {
    int t, n, ct, i, na, nb, a, b, sa, sb;
    
    ct = 0;
    for (scanf("%d", &t); t > 0; t --) {
        scanf("%d", &tt);
        
        scanf("%d%d", &na, &nb);
        n = (na + nb) * 2;
        
        for (i = 0; i < na + nb; i ++) {
            scanf("%s%s", x, y);
            
            data[i].l = convert(x) * 2;
            data[i].a = i < na;
            data[i + na + nb].l = (convert(y) + tt) * 2 - 1;
            data[i + na + nb].a = 2 + (i < na);
            }
        
        sort(data, data + n);
        sa = 0;
        sb = 0;
        a = b = 0;
        for (i = 0; i < n; i ++) {
            if (data[i].a >= 2) {
                if (data[i].a & 1)
                    sb ++;
                else
                    sa ++;
                }
            else {
                if (data[i].a & 1) {
                    if (sa == 0)
                        a ++;
                    else
                        sa --;
                    }
                else {
                    if (sb == 0)
                        b ++;
                    else
                        sb --;
                    }
                }
            }
        
        printf("Case #%d: %d %d\n", ++ct, a, b);
        }
    
    return 0;
    }
