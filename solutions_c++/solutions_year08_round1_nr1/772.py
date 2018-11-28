#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<list>
#include<map>
#include<bitset>
#include<sstream>
#include<utility>
#include<algorithm>
#include<queue>
#include<stack>
#define INF 1<<30
#define pb push_back()
#define sz(a) (int) a.size()

using namespace std;

int main()
{
    int T,i,j,x,n;
    cin>>T;
    
  for(i=0;i<T;i++)
  {
     vector<int> A,B;
     cin>>n;
             
     for(j=0;j<n;j++)
      {cin>>x;
      A.push_back(x);             
      }
      for(j=0;j<n;j++)
      {cin>>x;
      B.push_back(x);             
      }  
      
   sort(A.begin(),A.end()); 
   sort(B.begin(),B.end());
   reverse(B.begin(),B.end());
   
   long long int suma=0;
   
   for(j=0;j<n;j++)
   suma+=(long long int) (A[j]*B[j]); 
   cout<<"Case #"<<i+1<<": "<<suma<<endl; 
                   
  }  
    
    
    
    
return 0;
}
