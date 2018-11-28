#include <stdio.h>
#include <string.h>

char str[10000];
char map[26][26];
char opp[26][26];
char stk[10000];
int in[26];

int main() {
    int tt,TT,C,D,N,top,i,j;
    char x;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%d",&C);
        memset(map,-1,sizeof(map));
        memset(opp,0,sizeof(opp));
        for( i=0; i<C; i++ ) {
            scanf("%s",str);
            map[str[0]-'A'][str[1]-'A'] = str[2]-'A';
            map[str[1]-'A'][str[0]-'A'] = str[2]-'A';
        }
        scanf("%d",&D);
        for( i=0; i<D; i++ ) {
            scanf("%s",str);
            opp[str[0]-'A'][str[1]-'A'] = 1;
            opp[str[1]-'A'][str[0]-'A'] = 1;
        }
        scanf("%d",&N);
        scanf("%s",str);
        top = -1;
        memset(in,0,sizeof(in));
        for( i=0; i<N; i++ ) {
            x = str[i]-'A';
            while(1) {
                if(top==-1) {
                    stk[++top] = x;
                    in[x]++;
                    break;
                }else {
                    if(map[x][stk[top]]!=-1) {
                        x = map[x][stk[top]];
                        in[stk[top]]--;
                        top--;
                    }else {
                        in[x]++;
                        for( j=0; j<26; j++ ) {
                            if(in[j] && opp[x][j]) {
                                break;
                            }
                        }
                        if(j==26) {
                            stk[++top] = x;
                        }else {
                            memset(in,0,sizeof(in));
                            top = -1;
                        }
                        break;
                    }
                }
            }
        }
        if(top==-1) {
            printf("Case #%d: []\n",tt+1);
        }else {
            printf("Case #%d: [%c",tt+1,stk[0]+'A');
            for( i=1; i<=top; i++ ) {
                printf(", %c",stk[i]+'A');
            }
            printf("]\n");
        }
    }
    return 0;
}
