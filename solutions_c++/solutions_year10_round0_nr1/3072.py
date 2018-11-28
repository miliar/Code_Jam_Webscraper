#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<vector>
#include<map>
#include<queue>
#include<string>
#include<stdlib.h>
using namespace std;
int Pow(int x,int y){
    int an=1;
    while(y){
        if(y&1)an*=x;
        x*=x;
        y>>=1;
    }
    return an;
}
main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n,k,T,t=0;
    scanf("%d",&T); 
    while(T--){
        t++;
        scanf("%d %d",&n,&k);
        n=Pow(2,n);
        printf("Case #%d: ",t);
        if((k+1)%n==0)puts("ON");
        else puts("OFF");
    }
}
