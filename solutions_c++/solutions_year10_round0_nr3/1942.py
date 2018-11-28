#include <iostream>
#include <vector>

using namespace std;

int main() {

  long long int n;

  cin >> n;

  for (int cc=1;cc<=n;cc++) {

    long long int r;
    long long int k;
    long long int ng;
    vector<long long int> somamais(1000);
    vector<int> next(1000);
    cin >> r >> k >> ng;

    vector<long long int> groups;
    for (int i=0;i<ng;i++) {
      long long int a;
      cin >> a;
      groups.push_back(a);
    };

    for (int i=0;i<ng;i++) {
      long long int soma = 0;
      int j;
      for (j=0;j<ng;j++) {
	soma += groups[(i+j)%ng];
	if (soma > k) {
	  soma -= groups[(i+j)%ng];
	  break;
	};
      };
      next[i] = (i+j)%ng;
      somamais[i] = soma;
    };

    long long int total = 0;
    int cur = 0;
    for (int i=0;i<r;i++) {
      
      total += somamais[cur];
      cur = next[cur];

    };

    cout << "Case #" << cc << ": " << total << endl;
    
  };

  return 0;

};
