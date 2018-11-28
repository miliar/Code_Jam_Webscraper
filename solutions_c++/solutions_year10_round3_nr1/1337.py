#include<iostream>
#include<stdio.h>
#include<conio.h>
using namespace std;
int main(void)
{   int t;
    
    freopen("A-large.in","r",stdin);
    freopen("A-large0.out","w",stdout);
cin>>t; 
long long cas=0;   
while(t-->0)
    {   long long n=0,ai[1000],bi[1000],i=0,j=0,temp=0;
        cin>>n;
        for(i=0;i<n;i++)
        {   
            cin>>ai[i]>>bi[i];
        }
       
        /*for(i=0;i<n;i++)
        {   
            for(j=0;j<n-i-1;j++)
            {
                
                if(ai[j]>ai[j+1])
                {
                    temp=ai[j+1];
                    ai[j+1]=ai[j];
                    ai[j]=temp;
                }
            }
        }
         for(i=0;i<n;i++)
        {   
            for(j=0;j<n-i-1;j++)
            {
                
                if(bi[j]>bi[j+1])
                {
                    temp=bi[j+1];
                    bi[j+1]=bi[j];
                    bi[j]=temp;
                }
            }
        }
        
        for(i=0;i<n;i++)
        {cout<<ai[i];
         
        }     
        for(i=0;i<n;i++)
        {cout<<bi[i];
         
        } */    
           int count=0;
        for(i=0;i<n;i++)
        {
            for(j=1;j<n;j++)
            {
                if(ai[j]>ai[i]&&bi[j]<bi[i]&&j!=i&&i<j)
                count++;
                else if(bi[j]>bi[i]&&j!=i&&i<j)
                {
                    if(ai[j]<ai[i])
                    count++;
                }
            }
        }
        cas=cas+1;
        cout<<"Case #"<<cas<<":"<<" "<<count<<endl;
        count=0;
      }
getch();
}
