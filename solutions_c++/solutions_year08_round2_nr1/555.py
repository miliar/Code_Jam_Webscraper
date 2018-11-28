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
    vector < pair<LL,LL> > T;
    long long n,A,B,C,D,x0,y0,M;
    cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    long long X = x0, Y = y0;
    T.push_back(make_pair(X, Y));
 //   cout << X << " " << Y << endl;
    for (int i = 1; i<= n-1;i++)
    {
      X = (A * X + B) % M;
      Y = (C * Y + D) % M;
      T.push_back(make_pair(X, Y));
//      cout << X << " " << Y << endl;
    }

    long long cnt = 0LL;
    for(int i=0;i<T.size();i++)
    for(int j=i+1;j<T.size();j++)
    for(int t=j+1;t<T.size();t++)
    {
      if( (((T[i].first + T[j].first + T[t].first )% 3LL) == 0LL ) && (((T[i].second + T[j].second + T[t].second )% 3LL) == 0LL ) )
      {
          cnt++;
        
      }

    }

    cout << "Case #" << num <<": " << cnt <<   endl;
  }

  return 0;
}
