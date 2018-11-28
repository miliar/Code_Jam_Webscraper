#include<iostream>
using namespace std;
int main()
{
     int t,tempt,kvalues[31],m=2;
     scanf("%d",&t);
     kvalues[0]=1;
     for(int i=1;i<31;i++)
     {
         kvalues[i]=m;
         m=2*m;
    }
     tempt=t;
     while(t--){
     int n,k,p,modulo;
     scanf("%d %d",&n,&k);
     //printf("%d %d\n",k,kvalues[n]);
     modulo=k%kvalues[n];
     if(modulo+1==kvalues[n])
     printf("Case #%d: ON\n",tempt-t);
     else
     printf("Case #%d: OFF\n",tempt-t);
     }
     return 0;
}
