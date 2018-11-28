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
         int n;
         cin>>n;
         string temp;
          getline(cin,temp);
           vector<int> x;
           vector<int> y;
         for(int i=0;i<2;i++)
         {  
            string t;
            getline(cin,t);
            stringstream ss(t);
            int a;
            while(ss>>a)
            { if(i==0)
              x.push_back(a);
              else
              y.push_back(a);
            }
         }   
      
     long long sum=0;
      sort(x.begin(),x.end());
      sort(y.begin(),y.end());
       for(int i=0,j=n-1;i<n,j>=0;i++,j--)
       
          sum+=x[i]*y[j];
      
       cout<<"Case #"<<c+1<<": "<<sum<<endl;
        
      //  for(int i=0;i<n;i++)
        //cout<<y[i]<<endl;
         
     
      }
      
  return 0;   
}        
