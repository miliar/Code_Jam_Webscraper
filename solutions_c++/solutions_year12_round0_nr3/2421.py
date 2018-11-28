#include <iostream>
#include <cmath>
#include <set>
using namespace std;

int cycle(int n, int dig, int totalDig){
  int part = n % static_cast<int>(pow((double)10, dig));
  return n / static_cast<int>(pow((double)10, dig)) + part * static_cast<int>(pow((double)10, totalDig - dig));
}

unsigned NumRecycled(int a, int b){
  unsigned count = 0;
  int digits;
  for (digits = 1; static_cast<int>(pow((double)10, digits)) <= b; ++digits);
  if (digits == 1) return 0;
  for (int i = a; i < b; ++i){ //optimization, don't test b
    set<int> generated;
    for (int j = 1; j < digits; ++j){
      int m = cycle(i, j, digits);
      if (m / static_cast<int>(pow((double)10,digits - 1)) != 0 && m > i && m <= b)
        generated.insert(m);
    }
    count += generated.size();
  }
  return count;
}

int main(){
  int n; cin>>n;
  for (int i = 0; i < n; ++i){
    int a, b; cin>>a>>b;
    cout<<"Case #"<<i+1<<": "<<NumRecycled(a,b)<<endl;
  }
}
