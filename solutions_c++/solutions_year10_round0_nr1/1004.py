#include<cstdio>
#include<cstdlib>
#include<cstring>

int main(){
    int t;
    
    scanf("%d",&t);
    for(int c=1;c<=t;c++){
        int n,k;
        scanf("%d %d",&n,&k);
        if( (k+1)%(1<<n)==0)
            printf("Case #%d: ON\n",c);
        else printf("Case #%d: OFF\n",c);
    
    }

    return 0;
}
