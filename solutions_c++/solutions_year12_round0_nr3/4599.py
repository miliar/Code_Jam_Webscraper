#include<stdio.h>
#include<math.h>
#include<conio.h>

int main()
{
  long int T,i,j,n,k;
  long int A,B,dig,rec[1000],check,temp,r,va;
    
    scanf("%d",&T);  
    for (i=0;i<T;i++)
    {
        
     rec[i]=0;
                     scanf("%d %d",&A,&B);
                     for(j=A;j<=B;j++)
                     {
                                    
                                      check=j;
                                      dig=0;
                                      while(check!=0){
                                              check=check/10;
                                              dig++;
                                              }
                                              
                                              dig--;
                                      temp=j;
                                      do
                                      {
                                            
                                      r=temp%10;
                                      temp=temp/10;
                                      va=ceil(pow(10.0,dig));
                                      temp=temp+r*va;                 
                                  
                                     if(temp>j && temp<=B)
                                     { 
                                      rec[i]++;
                                      }
                                      
                                      }while(temp!=j);
                                      
                                                
                     }
   }
   
   
     for(i=0;i<T;i++)
     printf("Case #%d: %d\n",i+1,rec[i]);
   
}
