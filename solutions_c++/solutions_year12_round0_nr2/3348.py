#include <cstdio>
#include <iostream>

using namespace std;

int P;

/*
 * Can I achieve a non Suprising result of at least P,
 * having current sum = sum.
 *
 */
bool nonSuprising(int sum){
  sum -= P;
  if(sum < 0) return 0;

  if(P-1+P-1 <= sum) return 1;
  return 0;
}

/*
 * Can I achieve a Suprising result of at least P,
 * having current sum = sum.
 *
 */
bool Suprising(int sum){
  sum -= P;
  if(sum < 0) return 0;

  if(P-2+P-2 <= sum) return 1;
  return 0;
}

void solve(int T){
  int n, numSuprising, ret = 0;
  cin >> n >> numSuprising >> P;
  for(int i = 0; i < n; i++){
    int sum;
    cin >> sum;

    if(nonSuprising(sum)) ret++;
    else if(numSuprising > 0 && Suprising(sum)){
      ret++;
      numSuprising--;
    }
  }
  cout << "Case #" << T+1 << ": " << ret << endl;
}

int main(){
  int T;
  cin >> T;

  for(int i = 0; i < T; i++ )
    solve(i);
  return 0;
}
