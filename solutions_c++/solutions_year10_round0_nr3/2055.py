#include<cstdio>
#include<iostream>
using namespace std;
int arr[1000],pas[1000];
int vl,a,b,i,j,x,cos;
int ai,cap,ban,est;
long long cun[1000],con,ll;

int main(){
 
scanf("%d",&b);

for(a=0;a<b;a++){
scanf("%d %d %d",&vl,&cap,&j);

for(i=0;i<j;i++)
scanf("%d",&arr[i]);
                 
for(i=0;i<j;i++){
 ban=0;    
 ll=0;   
 est=i;
 ai=0;
          
 while(ban==0 && ai<j){
 if(est>=j){ est=0; }
 
 if(ll+arr[est]<=cap){              
    ll+=arr[est];
    ai++;  
                     }
                     
 else{
  ban=1;
      }
      
 est++; 
 }
 
 est--;
 pas[i]=est;
 cun[i]=ll;                    
 
}                 
 est=0;
 con=0;
 
 for(x=0;x<vl;x++){
  con+=cun[est];
  est=pas[est];                   
 }
 
 printf("Case #%d: ",a+1);
 cout<<con<<"\n";
 //printf("%lld\n",con);

} 
    

return 0;
}
