#include "stdio.h"
int g[100],R,k,N;

int solve(){
        int i,sum,hot[1000],count=0,temp[100],h,kk,j;
 while(R--)
 {      sum=0;
       for(i=0;i<N;i++)
         { sum+=g[i];
         if(i==N-1) break;
         if(sum+g[i+1]>k)  break;}
        hot[count++]=sum; j=i;
       
         for(h=0;h<=i;h++)
           temp[h]=g[h];
         for(kk=0;kk<N-i-1;kk++)
            g[kk]=g[++j];
          for(h=0;h<=i;h++)
             g[kk++]=temp[h];
   }
 sum=0;
    for(i=0;i<count;i++)
		sum+=hot[i];
     return sum;
}

int main(){
#ifdef _DEBUG
	freopen("C-small-attempt4.in", "r", stdin);
	freopen("out2.txt", "w", stdout);
#endif
   int T,sum,j=1;
   scanf("%d",&T);
   while(T--){
    sum=0;
   scanf("%d%d%d",&R,&k,&N);
   for(int i=0;i<N;i++)
     scanf("%d",&g[i]);
    sum=solve();
    printf("Case #%d: %d\n",j++,sum);
     }
return 0;
}
