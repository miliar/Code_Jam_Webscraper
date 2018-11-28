#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int main() {
  int k;
  cin >> k;
  for (int kk = 0; kk < k; kk++) {
    cout << "Case #" << kk +1 << ": ";
    string s;
    int n;
    cin >> n;
    vector<int> vet(n);
    for (int i = 0; i < n; i++) {
      cin >> s;
      int sz = s.size();
      vet[i] = 0;
      for (int j = sz-1; j>= 0; j--) {
	if (s[j] == '1') {
	  vet[i] = j;
	  break;
	}
      }
    }
    
    int soma = 0;
    for (int i = 0; i < n; i++) {
      if (vet[i] <= i) continue;
      for (int j = i+1;j < n; j++) {
	if (vet[j] <= i) {
	  for (int k = j; k > i; k--) {
	    swap(vet[k],vet[k-1]);
	    soma++;
	  }
	  break;
	}
      }
    }
    //for (int i = 0; i < n; i++) cout << vet[i] << " ";
    //cout << endl;
    printf("%d\n",soma);
  }
  return 0;
}
