#include<iostream>
#include<cstdlib>

int a,b,i,v,n,k;

int main(){

scanf("%d",&b);

for(a=0;a<b;a++){
                 
scanf("%d %d",&n,&k);
v=1;

for(i=0;i<n;i++){
   v*=2;  
   
                    
}
v--;

while(k>v)
k-=(v+1);

if(v==k)
printf("Case z#%d: ON\n",a+1);

else
printf("Case #%d: OFF\n",a+1);     

}

return 0;    

}
