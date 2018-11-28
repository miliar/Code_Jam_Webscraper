#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Fil {
  int debut;
  int fin;
};

struct Filcomp {
  bool operator() (Fil const &a, Fil const &b) const {
    return a.debut < b.debut;
  }
};

int main() {
  int T, N, nbIntersections;
  Fil nouveauFil;
  vector<Fil> fils;
  cin >> T;
  for(int i = 1 ; i <= T ; i++) {
    cin >> N;
    nbIntersections = 0;
    fils.clear();
    for(int j = 0 ; j < N ; j++) {
      cin >> nouveauFil.debut;
      cin >> nouveauFil.fin;
      fils.push_back(nouveauFil);
    }
    sort(fils.begin(), fils.end(), Filcomp());
    for(int j = 0 ; j < N - 1 ; j++) {
      for(int k = j + 1 ; k < N ; k++)
	if(fils[j].fin > fils[k].fin)
	  nbIntersections++;
    }
    cout << "Case #" << i << ": " << nbIntersections << endl;
  }
  return 0;
}
