#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <list>

using namespace std;

int abs(int x) 
{
   return (x > 0) ? x : -x;
}

int maxi;

int backtrack(vector<int>& candy, vector<int>& sum, int i = 0, int sean = 0, int patrick = 0, int seanRealSum = 0, int snbcandy = 0, int pnbcandy = 0)
{
  if(i >= candy.size())
    if(sean == patrick && snbcandy > 0 && pnbcandy > 0) {
      maxi = max(seanRealSum,maxi);
      return seanRealSum;
    } else {
      return -1;
    }
  if(seanRealSum + sum[i] < maxi) {
    return -1;
  }
  int sres = backtrack(candy, sum, i+1, sean ^ candy[i], patrick, seanRealSum + candy[i], snbcandy+1, pnbcandy);
  int pres = backtrack(candy, sum, i+1, sean, patrick ^candy[i], seanRealSum, snbcandy, pnbcandy+1);
  
  return max(sres,pres);
}

int main() {
  int cases, n;
  cin >> cases;
  
  for(int c = 1; c <= cases; c++) {
    cin >> n;
    
    vector<int> candy(n), sum(n+1);
    for(int i = 0; i < n; i++)
      cin >> candy[i];
    
    sum[n] = 0;
    for(int i = n - 1; i >= 0; i--) {
      sum[i] = sum[i+1] + candy[i];
      //cout << sum[i] << endl;
    }
    maxi = 0;
    int result = backtrack(candy, sum);
    if(result < 0)
      cout << "Case #"<< c << ": NO"<< endl;
    else
      cout << "Case #"<< c << ": " << result << endl;
  }
  
  return 0;
}