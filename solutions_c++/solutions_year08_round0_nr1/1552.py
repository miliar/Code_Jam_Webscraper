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

void display(vector<string> s)
{
      for(int i=0;i<s.size();i++)
      cout<<s[i]<<endl;
} 

int main()
{
     int N;
     scanf("%d", &N);
     
     for(int c=0;c<N;c++)
     {
         int n;
         cin>>n;
         
         vector <string> s;
         vector <string> q;
         string x;
         getline(cin , x );
         for(int i=0;i<n;i++)
         {
            string temp;
            getline(cin,temp);
           
            s.push_back(temp);
         }

         int m;
         cin>>m;
         getline(cin,x);
         
         
         for(int j=0;j<m;j++)
         {
           string temp;
           getline(cin,temp);
           
            q.push_back(temp);
            
         }
         
        
        
        
        int count=-1;
        
       while(q.size()>0)
      {  
            vector <int> f(s.size(),-1);
            int max=-1,pos=-1;
            
            for(int i=0;i<q.size();i++)
            {
                for(int j=0;j<s.size();j++)
                {
                     if(q[i]==s[j] && f[j]==-1 )
                      {              
                         f[j] = i;  
                         if(i>max)
                         {
                            max=i;
                            pos=j;
                         }
                       
                       }     
                                  
                }
               
             }
             
            
            
            for(int k=0;k<f.size();k++)
             if(f[k]==-1)
               { max=q.size();
                 pos=k;
               }
          
            
        
             q.erase(q.begin(),q.begin()+max);
          
          
            
            count++;
            
            
            
      
      }    // end of while         
        
        if(m==0)
        count=0;
        cout<<"Case #"<<c+1<<": "<<count<<endl;
        
        
         
     
      }
      
  return 0;   
}        
