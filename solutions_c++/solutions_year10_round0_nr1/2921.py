//snapper chain

#include"cstdio"
#include"cstdlib"

int main(){
    int t,n,k;
    long long sum;
    freopen("A-small.in","r",stdin);
    freopen("A-smal.txt","w",stdout);
    scanf("%d",&t);
    for(int i = 1;i<=t;i++){
        scanf("%d %d",&n,&k);
        sum = 1;
        for(long long j = 0;j<n;j++) sum*=2;
        if((k+1)%sum==0) 
        printf("Case #%d: ON\n",i);
        else printf("Case #%d: OFF\n",i);
    } 
    fclose(stdin);
    fclose(stdout);   
    system("pause");
    return 0;
}    
