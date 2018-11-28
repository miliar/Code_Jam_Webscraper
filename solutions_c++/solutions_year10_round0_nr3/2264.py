#include <iostream>
using namespace std;

int main() {
  int T, R, k, N, c, rang, periode, compteurAcc;
  int g[1000], dejaVu[1000], accumulateur[1000], sommes[1000], idAcc[1000];
  unsigned long long somme;
  cin >> T;
  for(int i = 1 ; i <= T ; i++) {
    cin >> R;
    cin >> k;
    cin >> N;
    for(int j = 0 ; j < N ; j++) {
      cin >> g[j];
      dejaVu[j] = false;
      accumulateur[j] = 0;
    }
    c = 0;
    compteurAcc = 0;
    rang = 0;
    while(!dejaVu[c % N]) {
      dejaVu[c % N] = true;
      idAcc[c % N] = compteurAcc;
      while(accumulateur[compteurAcc] + g[c % N] <= k && !(compteurAcc == 0 && c == N)) { // Il reste de la place
	accumulateur[compteurAcc] += g[c % N];
	c++;
      }
      compteurAcc++;
    }
    rang = idAcc[c % N];
    periode = compteurAcc - rang;
    sommes[0] = accumulateur[0];
    for(int j = 1 ; j < rang ; j++)
      sommes[j] = sommes[j - 1] + accumulateur[j];
    sommes[rang] = accumulateur[rang];
    for(int j = rang + 1 ; j < rang + periode ; j++)
      sommes[j] = sommes[j - 1] + accumulateur[j];
    if(R - 1 < rang) {
      somme = sommes[R - 1];
    } else {
      somme = (rang >= 1) ? sommes[rang - 1] : 0;
      somme += (R - rang) / periode * sommes[rang + periode - 1];
      if((R - rang) % periode > 0)
	somme += sommes[rang + (R - rang) % periode - 1];
    }
    cout << "Case #" << i << ": " << somme << endl;
  }
  return 0;
}
