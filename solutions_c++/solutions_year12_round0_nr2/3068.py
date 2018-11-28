#include<iostream>
#include<cstdio>
#include<string.h>
using namespace std;

  int main()
    {
         freopen("input.txt","r",stdin);
         freopen("output.txt","w",stdout);

         int tc=1,t,n,s,p,score,ming,mins,count;
         cin>>t;
         for(;tc<=t;tc++)
          {
              count = 0;
              cin>>n>>s>>p;
              switch(p)
              {
                  case 0:
                      ming = 0;
                      mins = 0;
                      break;
                  case 1:
                      ming = 1;
                      mins = 1;
                      break;
                  default: 
                      ming = 3*p-2;
                      mins = 3*p-4;
              }    
              
              for(int i = 0;i<n;i++)
               {
                   cin>>score;
                   if(score>=ming)
                      {count++;
                      continue;
                      } 
                   if((score>=mins)&&(s>0))   
                   {
                       count++;
                       s--;
                   }        
               }       
              cout<<"Case #"<<tc<<": "<<count<<"\n";              
          }   
                //system("PAUSE");
                return 0;
    }    

    
