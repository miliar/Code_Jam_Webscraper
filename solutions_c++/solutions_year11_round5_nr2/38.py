#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
#include <iostream>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

int c[100000];
int g[100000][2];

int main() {
    int TT,tt,n,i,r,j,md,mj;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%d",&n);
        if(n==0) {
            printf("Case #%d: %d\n",tt+1,0);
            continue;
        }
        for( i=0; i<n; i++ ) {
            scanf("%d",&c[i]);
        }
        sort(c,c+n);
        r = 0;
        for( i=0; i<n; i++ ) {
            md = 10000000;
            mj = -1;
            for( j=0; j<r; j++ ) {
                if(g[j][0]==c[i]-1) {
                    if(g[j][1]<md) {
                        md = g[j][1];
                        mj = j;
                    }
                }
            }
            if(mj==-1) {
                g[r][0] = c[i];
                g[r][1] = 1;
                r++;
            }else {
                g[mj][0] = c[i];
                g[mj][1]++;
            }
        }
        md = 100000000;
        for( i=0; i<r; i++ ) {
            if(g[i][1]<md) md = g[i][1];
        }
        printf("Case #%d: %d\n",tt+1,md);
    }
    return 0;
}
