#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cassert>

using namespace std;

vector<int> bag;

main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cout << "Case #" << t+1 <<": ";

    int N;
    cin >> N;
    int sum=0;
    int summ=0;
    int min=1000001;
    
    for (int i=0;i<N;++i) {
      int k;
      cin >> k;
      if(k>1000000) {
	cerr<<" k = "<<k<<" !!!"<<endl;
	assert(false);
      }
      if (k<min) min=k;
      sum += k;
      summ ^= k;
    }
    sum-=min;
    if (summ == 0)
      cout << sum;
    else
      cout << "NO";
    cout << endl;
  }
}
