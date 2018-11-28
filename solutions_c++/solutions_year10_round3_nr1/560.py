#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int CCW(int x1, int y1, int x2, int y2, int x3, int y3) {
    int a = x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1;
    if ( a > 0 ) return 1;
    if ( a < 0 )  return -1;
    return 0;
}

bool Intersect( int x1, int y1, int x2, int y2,
                int x3, int y3, int x4, int y4) {

        if (CCW(x1,y1,x2,y2,x3,y3)==-CCW(x1,y1,x2,y2,x4,y4) &&
                    CCW(x3,y3,x4,y4,x1,y1)==-CCW(x3,y3,x4,y4,x2,y2)) return true;
                        return false;
}

int listx1[1010];
int listy1[1010];
int listx2[1010];
int listy2[1010];

int main() {
    int aa, nn;
    int n;
    int cnt,i, j;
    scanf("%d",&nn);
    for ( aa = 1; aa <= nn; ++aa ) {
        scanf("%d",&n);
        for ( i = 0; i < n; i++ ) {
            scanf("%d %d",&listy1[i],&listy2[i]);
            listx1[i] = 0; listx2[i] = 1000;
        }
        cnt = 0;
        for ( i = 0; i < n; i++ ) {
            for ( j = i+1; j < n; j++ ) {
                if ( Intersect(listx1[i],listy1[i],listx2[i],listy2[i],
                        listx1[j],listy1[j],listx2[j],listy2[j]) )
                    cnt++;
            }
        }
        printf("Case #%d: %d\n",aa,cnt);
    }
    return 0;
}

