#include<iostream>
#include<string>
#include<cstdio>
#include<algorithm>
using namespace std;

int main()
{
    int t,l=0;
    cin>>t;
    while(t--)
    {
              int i,j,k,n,s,p,val,arr[110],scr=0;
              cin>>n>>s>>p;
              for(i=0;i<n;i++)
              {
                              cin>>val;
                              arr[i]=val;
                              j=val/3;
                              k=val%3;
                              
                              if(j>0)
                              {
                              if(j>=p)
                                  scr++;
                              else    
                              if(j+1>=p&k>0)
                              
                                 {       //if(k>0)
                                              scr++;
                                 
                                 }
                               else  
                              if(s>0)
                               if((j+2>=p&k==2)|j+1==p)
                                    {
                                               scr++;
                                               s--;
                                      }
                                //else if(j+1>=p)
                                
                                   
                               }
                               else
                               {
                                    if(p==2&k==2&s>0)
                                    {
                                                s--;
                                                scr++;
                                                }
                                    else if(p==1&k>0)
                                                    scr++;
                                    else if(p==0)
                                       scr++;
                               }                 
                                                      
              }
             cout<<"Case #"<<++l<<": "<<scr<<endl;
    }
    return 0;
}         
