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


int main()
{
     int N;
     scanf("%d", &N);
     
     for(int c=0;c<N;c++)
     { 
             int p,k,l;
        scanf("%d %d %d",&p,&k,&l);

        vector<long long> keys[k];
        vector<long long> freq;
        
        string temp;
        getline(cin,temp);
        getline(cin,temp);
        stringstream ss(temp);
        long long a;
        while(ss>>a)
        {
           freq.push_back(a);
         }
         
        sort(freq.rbegin(),freq.rend());
       int j=0;   
       for(int i=0;i<l;i++)
       {   if(j>=k)
           j=0;
           
           if(keys[j].size()>=p)
           j++;
           
           if(j>=k)
           j=0;
           
           keys[j].push_back(freq[i]);
           j++;
           
       }   
       
       long long count=0;
       for(int i=0;i<k;i++)
       for(int k=0;k<keys[i].size();k++)
       count+=(keys[i][k]*(k+1));
       
      // cout<<count<<endl;
       
      /*  for(int i=0;i<k;i++)
       {  
         for(int k=0;k<keys[i].size();k++)
          cout<<keys[i][k]<<"  ";
          
          cout<<endl;
          }  
                     
        */
       cout<<"Case #"<<c+1<<": "<<count<<endl;
        
        
      }
      
  return 0;   
}        
