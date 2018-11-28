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
#define pb push_back
#define sz(a) (int) a.size()

using namespace std;

int main()
{
    long long  int i,j,N,P,K,L,frec[2000];
    
   cin>>N;
   
  for(i=0;i<N;i++)
 {
    cin>>P>>K>>L; 
    
    for(j=0;j<L;j++)
     cin>>frec[j];             
                  
   sort(frec,frec+L);
   
   reverse(frec,frec+L);
   
   long long int suma=0;
   
    long long int aux=K,vez=1;


   
   for(j=0;j<L;j++)
   {
    if(aux==0) 
     {aux=K;
      vez++;
      } 
                   
                 
    suma= suma+   (long long int) ( (long long int) frec[j]*  (long long int) vez )  ;            
    
     aux--;              
                   
   } 

  cout<<"Case #"<<i+1<<": "<<suma<<endl;                
                  
 }   
 
    
return 0;
}
