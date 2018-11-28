#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve( vector<int>& );

int main(){
  int T, N, num;
  vector<int> candies; 
  cin >> T;
  for(int i=1; i<=T; ++i){
    cin >> N;
    candies.clear();
    while(N>0){
      --N;
      cin >> num;
      candies.push_back(num);
    }
    int sum = 0;
    for(vector<int>::iterator it = candies.begin(); it != candies.end(); ++it)
      sum += *it;
    if(sum%2 == 1){
      cout << "Case #" << i << ": NO" << endl;
    }else{
      sort(candies.begin(), candies.end());
      int ans = solve(candies);
      cout << "Case #" << i << ": ";
      if(ans)
        cout << ans;
      else
        cout << "NO";
      cout << endl;
    }
  }
  return 0;
}

int giveChotu(int c, int i, vector<int>& candies, vector<bool>& H){
  if(i >= (int)candies.size())
    return 0;
  if(c == 0){
    int falseA = 0, falseB = 0, ans = 0;
    for(int j=0; j<(int)candies.size(); ++j){
      if(H[j]){
        falseA ^= candies[j];
      }else{
        falseB ^= candies[j];
        ans += candies[j];
      }
    }
    if(falseA == falseB)
      return ans;
    else
      return 0;
  }
  int with, without;
  H[i] = true;
  with = giveChotu(c-1, i+1, candies, H);
  
  H[i] = false;
  without = giveChotu(c, i+1, candies, H);
  
  return ( (with>without)?with:without );
}

int solve(vector<int>& candies){
  int sz = candies.size();
  vector<bool> H(sz, false);
  for(int chotu = 1; chotu != sz; ++chotu){
    int badaPart = giveChotu(chotu, 0, candies, H);
    if(badaPart != 0)
      return badaPart;
  }
  return 0;
}
