#include <cstdio>
int T,N,L,chance,carry;
int i,x,t;


int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++){
         carry=0;
         scanf("%d",&N);
         scanf("%d",&chance);
         scanf("%d",&L);
         for(i=0;i<N;i++){
             scanf("%d",&x);
             if((x+2)/3>=L)
                carry++;
             else {
                  if(x/3!=0 && x>=3*L-4 && chance!=0){
                     chance--;
                     carry++;            
                  }
             }                 
         }
         printf("Case #%d: %d\n",t,carry);  
    }
    return 0;
}
