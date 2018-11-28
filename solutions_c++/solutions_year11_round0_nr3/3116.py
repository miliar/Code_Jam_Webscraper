/*! if g++ main.cpp; then ./a.out < test.in; fi
 */

#include <iostream>
#include <climits>
#include <iomanip>


using namespace std;


void solve(int x){
  int n;
  cin >> n;

  long sum = 0;
  long minval = 1000000;
  long buf;
  long check = 0;
  for(int i = 0; i < n; i++){
    cin >> buf;
    sum += buf;
    minval = min(minval, buf);
    check ^= buf;
  }
  sum -= minval;

  if(check == 0){
    cout << "Case #" << x << ": " << sum << endl;
  }
  else{
    cout << "Case #" << x << ": " << "NO" << endl;
  }
}

int main(int argc, char *argv[]){
  int n;
  cin >> n;

  for(int i = 0; i < n; ++i){
    solve(i + 1);
  }

  return 0;
}
