//
//  pa.cpp
//  
//
//  Created by mac on 12/5/26.
//  Copyright (c) 2012年 __MyCompanyName__. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <vector>

using std::vector;

int D;
int d[10010], l[10010], v[10010];

int main() {
    int t, n;
    int cases=0;
    scanf("%d",&t);
    
    while(t--) {
        bool yes = false;
        scanf("%d",&n);
        for(int i=1;i<=n;++i) {
            scanf("%d%d",d+i,l+i);
            v[i] = 0;
        }
        scanf("%d",&D);
        
        int len, pos;
        v[1] = d[1];
        pos = 1;
        for(int i=1;!yes && i<=n;++i) {
            //printf("%d %d\n", d[i], v[i]);
            if(v[i]+d[i] >= D) {
                yes = true;
                break;
            }
            for(int j=i+1;j<=n;++j)
                if( v[i]+d[i] >= d[j] ) {
                    int nextlen = (d[j]-d[i]) < l[j] ? (d[j]-d[i]) : l[j];
                    v[j] = v[j] > nextlen ? v[j] : nextlen;
                }
        }
        
        printf("Case #%d: ", ++cases);
        if( yes )   puts("YES");
        else        puts("NO");
    }
    
    return 0;
}
