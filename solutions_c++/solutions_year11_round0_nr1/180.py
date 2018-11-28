#include <stdio.h>

int O[100][2];
int B[100][2];

int main() {
    int tt,TT,n,i,j,x,y,p,q,f,s;
    char cmd[10];
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%d",&n);
        p = 0;
        q = 0;
        for( i=0; i<n; i++ ) {
            scanf("%s %d",cmd,&x);
            if(cmd[0]=='O') {
                O[p][0] = x;
                O[p++][1] = i;
            }else {
                B[q][0] = x;
                B[q++][1] = i;
            }
        }
        O[p][1] = 1000000;
        B[q][1] = 1000000;
        s = 0;
        for( i=0,j=0,x=1,y=1; i<p || j<q; ) {
            if(O[i][1]<B[j][1]) {
                while(x!=O[i][0]) {
                    if(x<O[i][0]) {
                        x++;
                    }else {
                        x--;
                    }
                    if(y<B[j][0]) {
                        y++;
                    }else if(y>B[j][0]) {
                        y--;
                    }
                    s++;
                }
                if(y<B[j][0]) {
                    y++;
                }else if(y>B[j][0]) {
                    y--;
                }
                s++;
                i++;
            }else {
                while(y!=B[j][0]) {
                    if(y<B[j][0]) {
                        y++;
                    }else {
                        y--;
                    }
                    if(x<O[i][0]) {
                        x++;
                    }else if(x>O[i][0]) {
                        x--;
                    }
                    s++;
                }
                if(x<O[i][0]) {
                    x++;
                }else if(x>O[i][0]) {
                    x--;
                }
                s++;
                j++;
            }
        }
        printf("Case #%d: %d\n",tt+1,s);
    }
    return 0;
}
