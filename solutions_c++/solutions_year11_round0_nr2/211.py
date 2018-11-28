#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;
#define N 111
#define M 300
char str[N];
bool opposite[M][M];
char combine[M][M];
char stk[N];
int vis[M],top;
int main(){
    int i,j,k;
    int cas;
    int C,D,n;
    char c1,c2,c3;
    //freopen("B.in","r",stdin);
    //freopen("B.out","w",stdout);
    scanf("%d",&cas);
    for(k = 1; k <= cas; k++){
        scanf("%d",&C);
        memset(combine,' ',sizeof(combine));
        memset(opposite,false,sizeof(opposite));
        for(i = 1; i <= C; i++){
            scanf(" %c %c %c",&c1,&c2,&c3);
            combine[(int)c1][(int)c2] = combine[(int)c2][(int)c1] = c3;
        }
        scanf("%d",&D);
        for(i = 1; i <= D; i++){
            scanf(" %c %c",&c1,&c2);
            opposite[(int)c1][(int)c2] = opposite[(int)c2][(int)c1] = true;
        }
        scanf("%d",&n);
        scanf("%s",str+1);
        for(i = 1, top = 0; i <= n; i++){
            if(top == 0){
                stk[++top] = str[i];
                continue;
            }
            char tmp = str[i];
            while(top > 0 && combine[(int)stk[top]][(int)tmp] != ' '){
                tmp = combine[(int)stk[top]][(int)tmp];
                top--;
            }

            for(j = 1; j <= top; j++)
                if(opposite[(int)stk[j]][(int)tmp]) break;
            if(j <= top) top = 0;
            else stk[++top] = tmp;
        }
        printf("Case #%d: [",k);
        for(i = 1; i < top; i++)
            printf("%c, ",stk[i]);
        if(top != 0) printf("%c",stk[top]);
        printf("]\n");
    }
    return 0;
}
