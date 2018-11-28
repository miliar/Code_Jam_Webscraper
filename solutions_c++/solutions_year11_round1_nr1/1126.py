#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string.h>
#include<list>
using namespace std;
int main(){
long long int T,Pd,Pg;
long long int N,i;
long long int cons=100,yash,temp;
int flag=0;
scanf("%lld",&T);
for(yash=1;yash<=T;yash++){
scanf("%lld%lld%lld",&N,&Pd,&Pg);
if(Pd<100&&Pg==100){
printf("Case #%lld: Broken\n",yash);
continue;
}
else if(Pd>0&&Pg==0){
printf("Case #%lld: Broken\n",yash);
continue;
}
else{
flag=0;
for(i=N;i>=1;i--){
cons=100;
temp=Pd;
temp/=__gcd(temp,cons);
cons/=__gcd(temp,cons);
i=i/__gcd(i,cons);
cons/=__gcd(i,cons);
if((temp*i)%100==0){
flag=1;
printf("Case #%lld: Possible\n",yash);
break;
}
}
if(flag==0)
printf("Case #%lld: Broken\n",yash);
}
}
return 0;
}
