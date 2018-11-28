#include<stdio.h>

int state[100], pow[100];

void disp()
{
     int i;
     printf("--------------------\n");
     for(i=0;i<10;i++){
        printf("%3d",state[i]);
     }
     printf("\n");
     for(i=0;i<10;i++){
        printf("%3d",pow[i]);
     }
     printf("\n");
}
int main()
{
    int T, Case,i,n,k;
    scanf("%d",&T);
    for(Case=1;Case<=T;Case++)
    {
      scanf("%d%d",&n,&k);
      for(i=0;i<n;i++){
          state[i]=0;
          pow[i]=0;
      }
      pow[0]=1;
      while(k--){
            i=0;
            while(pow[i]){
                if(state[i]) 
                     state[i]=0;
                else 
                     state[i]=1;
                i++;
                if(i==n)
                        break;
            }
            i=0;
            while(i<n){
                 pow[i+1]=pow[i]&&state[i];
                 i++;
            }
//            disp();
      }
      printf("Case #%d: ",Case);
      if(state[n-1]&&pow[n-1]) 
           printf("ON");
      else
          printf("OFF");
      if(Case!=T) printf("\n");
    }
   return 0;
}
