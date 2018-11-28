#include <iostream>
#include <utility>
#include <set>
#include <cassert>

using namespace std;

int pow10(int n){
  int tens = 1;
  while(n >= 10){
    tens *= 10;
    n = n / 10;
  }
  return tens;
}

int count_pairs(int a, int b){
  set< pair<int,int> > pairs;
  int count = 0;
  int p10 = pow10(a);

  for(int i = a; i <= b; ++i){
    int tens = 10;
    while(tens <= a){
      int n = i;
      int m = (n % tens) * (p10 * 10 / tens) + (n / tens);

      if(a <= n && n < m && m <= b){
        pairs.insert(make_pair(n, m));
        count++;
      }
      tens *= 10;
    }
  }
  
  return pairs.size();
}

int main(){
  int ntest;
  cin >> ntest;

  for(int itest = 0; itest < ntest; ++itest){
    int a, b;
    cin >> a;
    cin >> b;

    cout << "Case #" << itest + 1 << ": " << count_pairs(a, b) << endl;
  }

  return 0;
}