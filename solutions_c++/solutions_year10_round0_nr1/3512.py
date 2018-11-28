#include <cstdio>

using namespace std;

int main(){
    int test;
    scanf("%d",&test);
    for(int t=0;t<test;t++){
        int n,k;
        scanf("%d %d",&n,&k);
        printf("Case #%d: ",t+1);
        if(k%(1<<n)==((1<<n)-1))
            printf("ON");
        else
            printf("OFF");
        printf("\n");
    }

    return 0;
}
