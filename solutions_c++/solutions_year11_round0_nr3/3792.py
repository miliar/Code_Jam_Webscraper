#include<iostream>
using namespace std;
int main(){
    int T,kase,N,i,num, minN, sor,sum;
    freopen("Clarge.in","r",stdin);
    freopen("Clarge.out","w",stdout);
    scanf("%d",&T);
    
    for(kase=1;kase<=T;kase++){
        scanf("%d",&N);
        for(i=0,minN=10000001,sum=0,sor=0;i<N;i++){
            scanf("%d",&num);
            sum += num;
            sor ^= num;
            if(num < minN)
                   minN=num;
        }
        if(sor != 0)
               printf("Case #%d: NO\n",kase);
        else
               printf("Case #%d: %d\n",kase,sum-minN);
    }
    return 0;
}
                                   
