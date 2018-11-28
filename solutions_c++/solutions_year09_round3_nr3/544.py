#include <cstdlib>
#include <iostream>

using namespace std;
int t,n,k;
int WI[20];
int czy[200];
int main(int argc, char *argv[])
{
    
    
    
    
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
           
     scanf("%d%d",&n,&k);
    
     for(int i=0;i<k;i++)
      scanf("%d",&WI[i]);
      int res=0,resmin=1000000000;
      sort(WI,WI+k);
      do
      {
   //   for(int i=0;i<k;i++)cout<<WI[i]<<" "; cout<<endl;
      for(int i=1;i<=n;i++)czy[i]=1;  
       res=0;                          
      for(int i=0;i<k;i++) 
              {
             
              czy[WI[i]]=0;
              int start=WI[i]-1;
              while(start>=1 && czy[start]){start--;res++;} 
              start=WI[i]+1;   
              while(start<=n && czy[start]){start++;res++;}          
           //   cout<<"RES:"<<res<<endl;;       
                     
               } 
               if(res<resmin)resmin=res;    
      }     
      while(next_permutation(WI,WI+k))  ;                 
                                  
                                     
      
      
            
    printf("Case #%d: %d\n",i,resmin);        
    }
    
  //  system("PAUSE");
    
    
    
    
    return 0;
}
