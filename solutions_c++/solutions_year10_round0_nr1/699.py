#include<cstdio>

int t,n,k;


int main(){
    scanf("%d",&t);    
    for(int tcase=1;tcase<=t;++tcase){
            scanf("%d %d",&n,&k);        
            bool on = true;
            for(int j=1;j<=n;++j) if(k%(1<<j)!=(1<<j)-1){
                    on = false;
                    break;        
            }
            printf("Case #%d: %s\n", tcase, on ? "ON" : "OFF");
    }
    //while(true){};
}
