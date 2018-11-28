#include <iostream>

using namespace std;
int ntest;
int n,k;
int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    for(int t=0; t<ntest; t++){        
        printf("Case #%d: ",t+1);
        scanf("%d %d",&n,&k);
        if(k==0) printf("OFF\n");
        else if( k % (1<<n) == ((1<<n)-1) )
            printf("ON\n");
        else 
            printf("OFF\n");
    }
    return 0;
}

