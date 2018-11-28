#include<stdio.h>
#include<string.h>

int l , d , n , flg[20][30];
char dic[5003][18] , tok[505];

int main(){
    freopen("A-large.in" , "r" , stdin);
    freopen("A-large.out" , "w" , stdout);
    int i , j  , k;
    while(scanf("%d%d%d" , &l , &d , &n) == 3){
        for(i = 0;i<d;i++) scanf(" %s" , dic[i]);
        int kase = 1 , ret , m;
        gets(tok);
        for(i = 0;i<n;i++){
            gets(tok);
            ret = 0;
            memset(flg , 0 , sizeof(flg));
            m = strlen(tok);
            for(j = 0 , k = 0;j<m;j++ , k++){
                if(tok[j] == '('){
                    j++;
                    while(tok[j] != ')'){
                        flg[k][tok[j]-'a'] = 1;
                        j++;
                    }
                }
                else
                    flg[k][tok[j]-'a'] = 1;
            }

            for(j = 0;j<d;j++){
                for(k = 0;k<l;k++)
                    if(flg[k][dic[j][k] - 'a'] == 0) break;
                if(k == l) ret++;
            }
            printf("Case #%d: %d\n" , kase++ , ret);
        }
    }
    return 0;
}
