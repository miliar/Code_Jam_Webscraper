#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
   //freopen("A-large.in","r",stdin);
   //freopen("out.txt","w",stdout);
   int T , N , K , a;
   bool ison;
   
   scanf("%d",&T);
   for(int c=1;c<=T;c++)
   {
        scanf("%d%d",&N,&K);
        a = 1<<N;
        
        printf("Case #%d: ",c);
        if(K%a == a - 1)puts("ON");
        else            puts("OFF");    
   }
   return 0;
}
