#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <algorithm>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <string>

using namespace std;






int main()
{

  int i,j,k,n,T,z;

  cin >>T;

  vector<int> x;
  vector<int> y;




  for(i=0; i<T; ++i) {

    cin >>n;

    x = vector<int>(n);
    y = vector<int>(n);

    for(j=0; j<n; ++j)
      cin >> x[j];
    for(j=0; j<n; ++j)
      cin >> y[j];

    sort( x.begin(), x.end() );
    sort( y.begin(), y.end() );

    z = 0;
    for(j=0; j<n; ++j) {
      
      z+= x[j]*y[n-j-1];

    }

    cout << "Case #" << i+1 << ": " <<z ;

    cout <<endl;

    x.clear();
    y.clear();
  }


}
