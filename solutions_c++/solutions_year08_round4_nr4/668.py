#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<cmath>
#include<cstdio>
#include<sstream>
#include<algorithm>
using namespace std;

string s; vector<int> p;

int main ()
{
    int tc ; 
    cin>>tc;
    for( int cse = 1; cse <= tc; cse ++)
    {
         int k ; 
         cin>>k>>s;
         p.clear();
         for( int i = 0; i<k; i++) p.push_back( i );
         int ret = s.size();
         sort( p.begin(), p.end());

         do
         {
//          for(int i =0  ; i<p.size(); i++) cout<<p[i]; cout<<endl;
          string x(s.size(), '.');
          for( int i=0 ; i<s.size(); i++)
          {
               int block = i/k;     
               int st = block * k;
               x[i] = s[st + p[i-st]];    
          }   
          
          for( int i =0 ; ((int)x.size()) > 1 && i<((int)x.size()); i++)
          {
               if( x[i] == x[i+1] ) x.erase(x.begin() + i--); 
          }
          ret = min( ret, (int)x.size());
         }while( next_permutation( p.begin(),p.end()) );
         cout<<"Case #"<<cse<<": "<<ret<<endl;
    }
return 0;    
}
