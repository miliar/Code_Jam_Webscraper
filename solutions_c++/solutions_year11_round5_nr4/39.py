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

char str[100];

long long dfs(int d,long long s) {
    long long g;
    if(!str[d]) {
        g = (long long)(sqrt(s)+0.1);
        if(g*g==s) return s;
        return -1;
    }else if(str[d]=='?') {
        s<<=1;
        g = dfs(d+1,s);
        if(g!=-1) return g;
        return dfs(d+1,s+1);
    }else if(str[d]=='0') {
        return dfs(d+1,s<<1);
    }else {
        return dfs(d+1,(s<<1)+1);
    }
}

int main() {
    int tt,TT,f,i;
    long long x;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%s",str);
        x = dfs(0,0);
        printf("Case #%d: ",tt+1);
        f = 0;
        for( i=62; i>=0; i-- ) {
            if(x&(1LL<<i)) {
                f = 1;
                printf("1");
            }else {
                if(f) {
                    printf("0");
                }
            }
        }
        puts("");
    }
    return 0;
}
