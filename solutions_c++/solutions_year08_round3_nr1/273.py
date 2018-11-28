#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main ()
{
    int tc ; 
    cin>>tc;
    for( int cse = 1; cse <= tc; cse ++)
    {
         int perkey, nokey, noletter;
         cin>>perkey>>nokey>>noletter;     
         vector<unsigned long long> freq(noletter, 0);
         for( int i =0 ;i<noletter; i++) cin>>freq[i];
         sort( freq.begin(), freq.end());
         reverse( freq.begin(), freq.end());
         int keyno = 0; unsigned long long result =0, weight = 1;
         for( int i =0 ; i< noletter; i++)
         {
              result += weight * freq[i];
              keyno ++;
              if( keyno == nokey ) { keyno = 0; weight++ ; }
         }
         cout<<"Case #"<<cse<<": "<<result<<endl;
         
    }
return 0;    
}
