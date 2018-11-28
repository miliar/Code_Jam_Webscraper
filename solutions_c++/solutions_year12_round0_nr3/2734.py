#include <cstdio>
#include <cmath>
int T,A,B,carry;
int i,j,x,x1,x2,t,power;

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++){
         carry=0;
         scanf("%d%d",&A,&B);
         
         for(i=A;i<=B;i++){
             x=i;
             power=1;
             for(j=0;j<(int)log10(i);j++)
                power*=10;
                
             do{
                x1=x%10;
                x2=x/10;
                x=x1*power+x2;
                if(i<x && x<=B)carry++;
             }while(x!=i);               
         }
         printf("Case #%d: %d\n",t,carry);  
    }
    return 0;
}
