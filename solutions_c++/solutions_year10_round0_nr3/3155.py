#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

long long t,r,k,n,of,suma=0;
long long   wynik=0;
vector<long long> V;
int main()
{

 cin >> t;
 for (int i=0;i<t;i++)
  {     
   V.clear();       
   suma=0;
   wynik=0;       
   cin >> r >>k>>n;   
   
   for (int j=0;j<n;j++)
   {
    cin>> of;
    suma+=of;
    V.push_back(suma);
   }
   for (int j=0;j<r;j++)
   {
    long long dzi=upper_bound(V.begin(),V.end(),k)-V.begin();
    if (dzi==n)
    {
     wynik=wynik+V[dzi-1];
     continue;
    }
    if(dzi!=0)
    {
     wynik=V[dzi-1]+wynik;         
     for (int t=dzi;t<V.size();t++)
      V[t]-=V[dzi-1];
     int change = V[V.size()-1]; 
     V.insert(V.end(),dzi,0);
     replace_copy(V.begin(),V.begin()+dzi,V.end()-dzi,0,0);
     V.erase(V.begin(),V.begin()+dzi);
     for (int t=n-dzi;t<V.size();t++)
       V[t]+=change ;
     }
   }
   cout<<"Case #"<<i+1<<": "<<wynik<<endl;
  }
//system ("pause");  
return 0;    
}
