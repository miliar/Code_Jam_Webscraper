#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int main()
{
    int t,n,m,i,j,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
         cin>>n>>m;
         int count=0;
         char a[4],a1[4],a2[4],a3[4];
        if(n>=100 && n<=999)
        { 
  for(i=n;i<=m;i++)
  {
                   itoa(i,a,10);
                   a1[0]=a[2];a1[1]=a[0];a1[2]=a[1];a1[3]='\0';
                   a2[0]=a[1];a2[1]=a[2];a2[2]=a[0];a2[3]='\0';
      for(j=i+1;j<=m;j++)
      {       
              itoa(j,a3,10);
              if((strcmp(a1,a3)==0) || strcmp(a2,a3)==0)
              {
                                    count++;
                                    }      
                   }
                   }
                   }
             if(n>=10 && n<=99)
             {
                 for(i=n;i<=m;i++)
                 {
                      itoa(i,a,10);
                       strrev(a);
                     for(j=i+1;j<=m;j++)
                     {
                                        itoa(j,a3,10);
                                        if(strcmp(a,a3)==0)
                                        {
                                                           count++;
                                                           }
                                                           }
                                                           } 
                                                           }
                                       printf("Case #");
                                       cout<<k;
                                       printf(": ");                                          
                   cout<<count<<endl;
                   }
                   return 0;
                   }                                             
                        
                                                  
              
