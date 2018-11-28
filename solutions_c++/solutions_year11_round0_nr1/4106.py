#include<iostream>
using namespace std;
int main(){
    int T,N,kase,i,k;
    char str[5];
    freopen("Alarge.in","r",stdin);
    freopen("Alarge.out","w",stdout);
    scanf("%d",&T);
    for(kase=1;kase<=T;kase++){
        scanf("%d",&N);
        int prevO=1,prevB=1,tO=0,tB=0,tmp,curr=0;
        while(N--){
                scanf("%1s%d",str,&tmp);
                if(str[0]=='O'){
                   if((curr-tO) >= abs(tmp-prevO)){                                
                                tO = curr+1;                               
                   }
                   else{
                        tO = curr+1 + abs(tmp-prevO) - (curr-tO);
                   }
                   prevO = tmp;
                   curr = tO;
                }
                else{
                   if((curr-tB) >= abs(tmp-prevB)){                                
                                tB = curr+1;                               
                   }
                   else{
                        tB = curr+1 + abs(tmp-prevB) - (curr-tB);
                   }
                   prevB = tmp;
                   curr = tB; 
                }
                //cout<<prevO<<","<<prevB<<","<<tO<<","<<tB<<","<<curr<<endl;
        }
        printf("Case #%d: %d\n",kase,curr);
    }
    return 0;
}
                        

        
