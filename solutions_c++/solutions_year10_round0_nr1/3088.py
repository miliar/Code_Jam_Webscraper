#include <iostream>
using namespace std;

int N,x,y,t,ca;

int main(){
    freopen("gcj1.in","r",stdin);
    freopen("gcj1.out","w",stdout);
    scanf("%d",&N);
    int i;
    for(i=1;i<=N;i++){
        scanf("%d%d",&x,&y);
        t=(1<<x)-1;
        if(y<t){
            printf("Case #%d: OFF\n",++ca);
        }
        else{
            if((y-t)%(t+1)==0){
                printf("Case #%d: ON\n",++ca);
            }
            else{
                printf("Case #%d: OFF\n",++ca);
            }
        }
    }
    
    return 0;
}
