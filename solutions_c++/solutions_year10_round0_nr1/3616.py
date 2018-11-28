#include<iostream>
#include<cmath>
   using namespace std;

   int main()
   {
          freopen("A.in","r",stdin);
              freopen("A.out","w",stdout);

             int M,N,K,a,test,i,j,kase=1,b,c;
             int ar[100];


             scanf("%d",&M);

             while(M--)
             {                scanf("%d%d",&N,&K);

                              a=(1<<N)-1;

                              b=K%(1<<N);
                              if(a==b)
                                     printf("Case #%d: ON\n",kase);
                              else printf("Case #%d: OFF\n",kase);
                              kase++;

             }
                    return 0;
   }
