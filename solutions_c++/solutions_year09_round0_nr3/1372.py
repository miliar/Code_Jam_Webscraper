#include<stdio.h>
#include<string.h>

const char wel[20]="welcome to code jam";

char str[512];
int L, sum[20][600];

int solve()
{
    int i, j, k, ret;
    
    memset(sum, 0, sizeof(sum));
    
    for(i=0; i<19; i++)
        for(j=i; j<L; j++)
            if(wel[i]==str[j]){
                if(i==0) sum[i][j]=1;
                else{
                    for(k=i-1; k<j; k++) sum[i][j]=(sum[i][j]+sum[i-1][k])%10000;
                }
            }
    
/*    for(i=0; i<19; i++){
        for(j=0; j<L; j++) printf("%d ", sum[i][j]);
        printf("\n");
    }
    printf("\n");
*/    
    ret=0;
    for(i=18; i<L; i++) ret=(ret+sum[18][i])%10000;
    
    return ret;
}

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);

    int cc, ct, ans;

//    for(int i=0; i<19; i++) printf("%d: %c\n", i, wel[i]);
//    printf("\n");
    
    scanf("%d", &cc);
    gets(str);
    for(ct=1; ct<=cc; ct++){
//        scanf("%s", &str);
        gets(str);
        L=strlen(str);
        ans=solve();
        printf("Case #%d: %04d\n", ct, ans);
    }
    
    return 0;
}
