#include<stdio.h>
#include<memory.h>
#define mod 100003

long long  f[502][502],c[502][502];
long long  s[502];
int  n;

void getc(){
     c[0][0] =  1;
     for(int i=1;i<=500;i++){
         for(int j=0;j<=i;j++){
             if(j==0)  c[i][j] = 1;
             else{
                c[i][j] = (c[i-1][j] + c[i-1][j-1])%mod;
             }
         }
     }
}
void init(){
     getc();
     f[2][1] = 1;
     f[1][0] = 1;
     for(int i=3;i<=500;i++){
         for(int j=1;j<=i-1;j++){
             for(int k=0;k<=j-1;k++)
                f[i][j] =  (f[i][j] +  f[j][k]*c[i-j-1][j-k-1])%mod;
         }
     }
     //printf("f[3][1]: %d\n",f[3][1]);
     for(int i=2;i<=500;i++){
         for(int j=1;j<=i-1;j++){
            s[i] = (s[i] + f[i][j])%mod;

         }
     }
}
int main(){
    init();
    freopen("C-large.in","r",stdin);
    freopen("ccout.txt","w",stdout);
    int t,ccount = 0;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        printf("Case #%d: %I64d\n",++ccount,s[n]);
    }
    return 0;
}
