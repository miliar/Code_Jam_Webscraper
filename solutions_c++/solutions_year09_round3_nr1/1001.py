#include<iostream>
#include<conio.h>
#include<string.h>
#include<math.h>
using namespace std;
int main()
{
int i,j,k,l,m,n,flag,T,count=0,counter=0,maincounter=0,subcounter=0,pow,result;
i=j=k=l=m=n=flag=0;
char ar[61];
int ar1[61];
cin>>T;
for(i=0;i<61;i++)
ar1[i]=-1;
for(j=0;j<T;j++)
{   count=0;
counter=1;
for(i=0;i<61;i++)
ar1[i]=-1;
maincounter=0;
subcounter=0;
    cin>>ar;
    count=strlen(ar);
    
    for(i=0;i<count;i++)
    {
         if(ar1[i]!=-1)
         continue;               
          if(counter==1)
              {
                        subcounter++;
                            ar1[i]=counter;
                            maincounter++;
                            for(k=i+1;k<count;k++)
                            {
                             if(ar[k]==ar[i])
                             {ar1[k]=counter;   
                              maincounter++;
                             }                
                            }
                            counter=0;
              }                       
              else if(counter==0)
              {
                    subcounter++;
                            ar1[i]=counter;
                             maincounter++;
                              for(k=i+1;k<count;k++)
                            {
                             if(ar[k]==ar[i])
                              {ar1[k]=counter;   
                              maincounter++;
                             }                           
                            }
                            counter=2;              
              }            
              else
              {
                   subcounter++;
                           ar1[i]=counter;
                            maincounter++;
                             for(k=i+1;k<count;k++)
                            {
                             if(ar[k]==ar[i])
                              {ar1[k]=counter;   
                              maincounter++;
                             }                          
                            }
                           counter++;    
              }
              
        if(maincounter==count)
        break;      
                             
    } 
    result=0;
      pow=1;
     if(subcounter==1)
     subcounter=2;
    for(i=0;i<count;i++)
    {    pow=1;
        for(k=count-1-i;k>0;k--)
        pow=pow*subcounter;
               
        result+= ar1[i]*pow;         

    }
    cout<<"Case #"<<j+1<<": "<<result<<endl;
}
cin>>i;
return 0;    
}
