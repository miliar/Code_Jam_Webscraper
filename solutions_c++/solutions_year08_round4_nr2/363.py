#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<vector>
#include<string>
#include<set>
using namespace std;

int T, a, x, y;

int main() {
    scanf("%d",&T);
    for(int z=0;z<T;z++) {
        bool ok = 0;
        scanf("%d %d %d",&x,&y,&a);
        for(int i=0;i<=x;i++) for(int j=0;j<=y;j++) for(int i2=0;i2<=x;i2++) for(int j2=0;j2<=y;j2++) {
            if(i*j2-j*i2 == a) {
                ok = 1;
                printf("Case #%d: %d %d %d %d %d %d\n",z+1,0,0,i,j,i2,j2);
                goto end;
            }
        }
        end:
        if(!ok) printf("Case #%d: IMPOSSIBLE\n",z+1);
    }
    return 0;
}

              
        
