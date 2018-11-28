#include <stdio.h>

unsigned long long k;
int arr[32];

void set(){
     int i;
     arr[1] = 1;
     for (i=2;i<=30;i++){
         arr[i] = (arr[i-1] * 2) + 1;
     }
}

int main (){
    int n,i,t,z;
    z=0;
    set();
    scanf("%d",&t);
    for (i=0;i<t;i++){
        z = 0;
        scanf("%d %u",&n,&k);
        if (k - arr[n] >= 0){
           if ( ((k-arr[n])%(arr[n]+1)) == 0 )z = 1;
        }
        if (z == 0)printf("Case #%d: OFF\n",i+1);
        if (z == 1)printf("Case #%d: ON\n",i+1);
    }
    while (getchar()!=EOF);
    return 0;
}
