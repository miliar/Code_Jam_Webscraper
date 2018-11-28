#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int gettime(string s )
{
   stringstream ss(s);
   int a=0,b=5;char c;
   ss>>a>>c>>b;
   return (a*60)+b;
}  


int main()
{
     int N;
     scanf("%d", &N);
    
     for(int c=0;c<N;c++)
     {
         int T;
         cin>>T;
        
         int na,nb;
         scanf("%d %d",&na,&nb);
        
     
        vector <int> reqA;
        vector <int> reqB;
        vector <int> availA;
        vector <int> availB; 
    
       for(int i=0;i<na;i++)
       {
          string temp;
          getline(cin,temp,' ');
        
          reqA.push_back(gettime(temp));
          getline(cin,temp);   
          availB.push_back(gettime(temp)+ T);
            
     
       }
     
       
      
        for(int i=0;i<nb;i++)
       {
          string temp;
          getline(cin,temp,' ');
         
          reqB.push_back(gettime(temp));
          getline(cin,temp);   
          availA.push_back(gettime(temp)+ T);
           
     
       }
     
     
      
        
     
     
       sort(reqA.begin(),reqA.end());
       sort(reqB.begin(),reqB.end());
       sort(availA.begin(),availA.end());
       sort(availB.begin(),availB.end());
       
       
      
     
       for(int i=0;i<reqA.size();i++)
        if(availA.size()>0)
        {
           if(reqA[i]>=availA[0])
            {
               reqA.erase(reqA.begin()+i);
               availA.erase(availA.begin());
               i--;
               if(reqA.size()==0 || availA.size()==0)
               break;
            } 
            
            
        }
            else
            break;
            
                
        
        
        
        
        
        
        for(int i=0;i<reqB.size();i++)
         if(availB.size()>0)
         {
           if(reqB[i]>=availB[0])
            {  
               reqB.erase(reqB.begin()+i);
               availB.erase(availB.begin());
               i--;
              if(reqB.size()==0 || availB.size()==0)
               break; 
            } 
            
         }
    
         else break;            
     
                   
     
     cout<<"Case #"<<c+1<<": "<<reqA.size()<<" "<<reqB.size()<<endl;
     
     
     
      }
      
    
     
  return 0;   
}        
