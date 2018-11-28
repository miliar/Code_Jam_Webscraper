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

const LL mod = 1000000007LL;
int main()
{
  int tst;
  cin >> tst;
  int num = 0;
  while(++num <= tst)
  {
    LL cnt = 0;
    LL  n , m, X,Y,Z;
    cin >> n >> m >> X >> Y >> Z;
    vector <LL> A(m);
    for(int i=0;i<m;i++) cin >> A[i];

    vector <LL> T;
    for (LL i = 0; i< n;i++)
    {
      T.push_back( A[i % m]);
      A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z ;
    }

  //  for(int i=0;i<T.size();i++) cout << T[i] << " ";
   // cout << endl;
    vector<LL> W(n,0);
    for(int i= W.size()-1; i >=0;i--)
    {
      for(int j=i+1;j<W.size();j++)
      {
         if(T[i] < T[j] ) W[i] += (1LL + W[j])%mod;
         W[i] %=mod;
      }
    }
    cnt = n;
    for(int i=0;i<n;i++) { cnt+= W[i];  cnt %=mod; }
    cout << "Case #" << num <<": " << cnt%mod <<   endl;

  }

  return 0;
}
