#include <stdio.h>
#include <stdlib.h>

int n;
int val[15];

int main()
{
   int t; 
   scanf("%d",&t);
    
   for(int w=1;w<=t;w++) 
   { 
      scanf("%d",&n);
      int soma=0;
      for(int i=0;i<n;i++)
      {
         scanf("%d",&val[i]);
         soma+=val[i];
      } 
    
      int aux=1<<n;
      aux--;
      
      int pat=0;
      int sea=0;
      
      int maior=0;
      
      for(int i=0;i<=aux;i++)
      {
         pat=0;   
         sea=0;
         int cur=0;   
         for(int j=0;j<n;j++) 
         {
            int p=1<<j;
            
            if(i&p) 
            {
               pat=(pat^val[j]);
            }
            else 
            {
               sea=(sea^val[j]); 
               cur+=val[j];
            }    
         }
         
         if(pat==sea && cur>maior && cur!=soma) maior=cur;  
      }
      
      if(maior==0) printf("Case #%d: NO\n",w);
      else printf("Case #%d: %d\n",w,maior); 
      
   } 
  return 0;   
}
