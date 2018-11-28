//XOR 
//2^N ways of choosing numbers.

#include<vector>
#include<iostream>
using namespace std;
typedef vector<int> Intvec;

int main()
{
   int T;
   cin >> T;  
   for(int n=0; n<T; ++n)
   {
       int k;
       cin>>k;
       int exor =0, sum = 0, min=INT_MAX;
       for(int i=0; i< k; ++i)
       {
          int temp;  
          cin>>temp;   
          exor^= temp;
          sum += temp;
          if(min > temp) min = temp;     
       }
       if(exor != 0)
       {
           cout << "Case #"<<n+1<<": NO\n";    
       } 
       else
       {
           cout << "Case #"<<n+1<<": "<<sum-min<<"\n"; 
       }
   }    
}
