#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <memory>
#include <cctype>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define FOR( i , n ) for (int i = 0; i < n ; i++ )
#define debug(x) cout << #x" = " << x << "\n"
#define FORIT( i , c ) for ( __typeof((c).begin())  i  = (c).begin() ; (i) != (c).end() ; (i)++ )

vector<int> v;

int main() {
  int ca;
  cin>>ca;
  string c1;
  FOR(cas, ca)
    {
      string N;
      cin >> N;
      long long u=0;
      v.clear();
      cout<<"Case #"<<cas+1<<": ";
      
      FOR(i,N.size())
        v.push_back(N[i]-'0');
      
      if(next_permutation(v.begin(),v.end()))
        {
       FOR(i,v.size()) 
          {
          cout<<((char)('0'+v[i]));
          }

        }
      else
       {
        
        sort(v.begin(),v.end());
        int k = 0;
        while(v[k]==0)k++;
        int b = v[k];
        cout<<((char)(v[k]+'0'))<<"0";
        FOR(i,v.size()) 
        if(i!=k)
       {
        cout<<((char)(v[i]+'0'));
       }

      }
      cout<<endl;      
}
 return 0;
}
