#include<iostream>
#include<cstdio>
using namespace std;

      
  int main()
    {
         freopen("input.txt","r",stdin);
         freopen("output.txt","w",stdout);
         
         int t,tc=1,n,h,l,freq[101];

         for(scanf("%d",&t);tc<=t;tc++)
          {
              printf("Case #%d: ",tc);
            scanf("%d %d %d\n",&n,&l,&h);
                    for(int nop=1;nop<=n;nop++)
                    {
                        scanf("%d ",&freq[nop]);
                    }    
                    
             int found;       
             for(int f=l;f<=h;f++)
             { 
                 found=1;      
              for(int nop=1;nop<=n;nop++)
                    {
                        if((freq[nop]%f!=0)&&(f%freq[nop]!=0))
                          {
                            found=0; 
                            break;
                        }     
                    }
                  if(found==1)
                   {
                       printf("%d\n",f);
                       break;
                   }            
              }   
              
                 if(found==0)
                   printf("NO\n");   

          }        
                
                //system("PAUSE");
                return 0;
    }    

    
