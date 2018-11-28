#include<cstdio>
#include<algorithm>
using namespace std;



int nb,nd;
int save[1002];

int main(){
    
     int t;
    int z=1;
    scanf("%d",&t);
    FILE *p = fopen("c.txt","w");
    int n;
    while(t--)
    {
      memset(save,0,sizeof(save));
      scanf("%d",&n);
      int total=0;
      int maks=0;
      nb=nd=0;
      for(int i=0;i<n;i++)
      {
       scanf("%d",&save[i]);
       total+=save[i]; 
       nb^=save[i]; 
      }
      
      if(!nb)
      {
      
      for(int i=1;i<(1<<n);i++)
      {
       nd=nb=0;
       int nb2=0;
       for(int j=0;j<n;j++)
       {
           if(i&(1<<j))
           {
              nd+=save[j];
              nb^=save[j];  
                
           }   
           else  nb2^=save[j];    
       }    
       if((nb2==nb) &&nb && nb2)
       {
       maks=max(( (total-nd>nd)?total-nd:nd ),maks);       
       } 
           
      }       
             
      }
     
     
      
      if(maks)fprintf(p,"Case #%d: %d\n",z++,maks);
      else fprintf(p,"Case #%d: NO\n",z++);
              
    }
    
    return 0;
    }
