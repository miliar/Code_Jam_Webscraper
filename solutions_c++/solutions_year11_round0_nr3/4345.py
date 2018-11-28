#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int tot,res,cad[20],i,j,a,b;
int vis[20];

void rec(int pos, int sum){

int m,sum1,sum2;
int con1,con2;

if(pos > j) return ;

con1=con2=sum1=sum2=0;

for(m=0; m<j; m++){
   if(vis[m] == 0){
      sum1=sum1^cad[m];        
      con1++;
     }
   else {
      sum2=sum2^cad[m];
      con2++;   
   }           
}

if(con1 > 0 && con2 > 0 ){
if(sum1 == sum2) {
  if(sum > res)
    res=sum;
  if((tot-sum) > res)
    res=(tot-sum);             
}
}

vis[pos]=1;
rec(pos+1,sum+cad[pos]);
vis[pos]=0;
rec(pos+1,sum);

     
return;     
}


int main(){

scanf("%d",&b);

for(a=0; a<b; a++){

tot=0;         
scanf("%d",&j);         
for(i=0; i<j; i++) {
   scanf("%d",&cad[i]);
   tot+=cad[i];
   }

res=0 ;
vis[0]=1;   
rec(1,cad[0]);
vis[0]=0;
rec(1,0);         
         
if(res == 0)
   printf("Case #%d: NO\n",a+1);         
else
   printf("Case #%d: %d\n",a+1,res);

memset(vis,0,sizeof(vis));
memset(cad,0,sizeof(vis));

}
      
return 0;    
}
