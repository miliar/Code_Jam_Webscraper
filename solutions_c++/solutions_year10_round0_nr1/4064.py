#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
   long test,n,k,i,j;
   scanf("%ld",&test);
   for(i=1;i<=test;i++)
   {
       scanf("%ld%ld",&n,&k);
       k++;
       long p= (1<<n);
       
       printf("Case #%ld: ",i);
       
       if(!(k%p))printf("ON\n");
       else printf("OFF\n");
   } 
   //int dum; scanf("%d",&dum); 
   return 0;  
}
