#include<stdio.h>
#include<stdlib.h>
void solve(int test){
    int a,b;
    scanf("%d %d",&a,&b);
    int ans=0;
    for(int i=a;i<b;i++){
        int p;
        for(p=1;p*10<=i;p*=10);
        int l=10;
        int no=i;
        do{
            int k = no%10;
            no=no/10 + p*k;
            if(no>=a&&no<=b&&no>i)ans++;
        }while(no!=i);
    }
    printf("Case #%d: %d\n",test,ans);
}
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)solve(i);
}
