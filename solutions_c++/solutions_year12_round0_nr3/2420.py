#include <iostream>

using namespace std;

int rotate(int x){
  int k = 1;
  int t = 0;
  while(!t){
    t = x % 10;
    x /= 10;
    k *= 10;
  }
  int a = x;
  while(a){
    a /= 10;
    k *= 10;
  }
  return x + t * k / 10;
}

int main(){
  ios_base::sync_with_stdio(0);
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; ++test){
    int ans = 0;
    int a, b;
    cin >> a >> b;
    for(int i = a; i <= b; ++i){
      int x = i;
      while((x = rotate(x)) != i)
	if(x >= a && x <= b)
	  ++ans;
    }
    cout << "Case #" << test << ": " << ans / 2 << endl;
  }
}
