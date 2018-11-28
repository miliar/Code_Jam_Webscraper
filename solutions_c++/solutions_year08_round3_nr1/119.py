#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <utility>
#include <queue>
using namespace std;
 
#define all(c)         (c).begin(),(c).end()
#define fori(c,i)     for(typeof(c).begin() i = (c).begin(); i != (c).end(); i++)
 
typedef long long     LL;
typedef vector<int>   vi; 
typedef vector< vi >   vvi; 

int main()
{
  int tst;
  cin >> tst;
  int num = 0;
  while(++num <= tst)
  {
    int P,K,L;
    cin >> P >> K >> L;                  // p - liter, k - klawiszy
    
   // cout << "====" << L << endl;
    vector <int> T(L);
    for(int i=0;i<L;i++) cin >> T[i];
    sort(all(T));
    reverse(all(T));
    LL cnt = 0LL;

  //  for(int i=0;i<L;i++) cout <<  T[i]  << " ";
    
    vector <int> Z(P,K);
    int c = 0;
    for(int i=0;i<P;i++)
    {
       while( c < L && Z[i])
       {
         cnt+= (LL)(i+1)*(LL)T[c];
         Z[i]--;
         c++;
       }
    }
    if( c == L)
    {
      cout << "Case #" << num <<": " << cnt <<   endl;
    }
    else cout << "Case #" << num <<": Impossible"  <<   endl;
  }

  return 0;
}
