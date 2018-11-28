#include <stdio.h>
#include <stdlib.h>

int abs(int x)
{
   if(x<0) x=-1*x;
   
   return x;
}
int main()
{
    int t;
    scanf("%d",&t);
    
    for(int w=1;w<=t;w++)
    {
       int n;
       scanf("%d",&n);
       
       int resp=0;
       int cur[2];
       cur[0]=1;
       cur[1]=1;
       
       int ant;
       int aux;
       scanf(" %c %d",&ant,&aux);
       
       resp+=aux;
       if(ant=='O') cur[0]=aux;
       if(ant=='B') cur[1]=aux;
       
       for(int i=2;i<=n;i++)
       {
          char r; 
          int b;
          scanf(" %c %d",&r,&b); 
          
          int v;
          if(r=='O') v=0;
          if(r=='B') v=1;
           
          if(r==ant)
          {
            int tam=abs(b-cur[v]);
            
            resp+=tam+1;      
            aux+=tam+1;
            
            cur[v]=b;
          } 
          else
          {
             int tam=abs(b-cur[v]);
             
             if(aux>=tam)
             {
               resp+=1;
               aux=1;     
             }
             else
             {
                tam-=aux;
                
                resp+=tam+1;
                aux=tam+1;      
             }
          
             cur[v]=b; 
          }
       
          ant=r;
       }
    
       printf("Case #%d: %d\n",w,resp);
    }
    
  return 0;   
}
