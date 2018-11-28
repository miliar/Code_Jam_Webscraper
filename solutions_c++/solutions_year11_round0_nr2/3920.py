#include <ext/hash_map>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
using namespace __gnu_cxx;

int
magicka(const char *T,
        int N,
        hash_map<int, char>& H1,
        hash_map<int, char>& H2,
        vector<char>& V)
{
  int n = -1;
  while (++n < N) {
    V.push_back(T[n]);

    int size = V.size();
    if (size == 1)
      continue;

    char c = H1[(V[size - 2] << 8) + V[size - 1]];
    if (c == 0)
      c = H1[V[size - 1] + (V[size - 2] << 8)];


    if (c) {
      V.pop_back();
      V.pop_back();
      V.push_back(c);
    } else {
      char d = H2[V[size - 1]];
      if (d && find(V.begin(), V.end(), d) != V.end())
          V.clear();
    }
  }

  return 0;
}

int
main(int agrc, char *argv[]) {
  int num_c, num_d, num_t;
  char C[3], D[2];
  char *T;
  int line = 0;
  
  ifstream fin("data1.txt");
  int dummy;
  fin >> dummy;

  while (fin) {
    fin >> num_c;
    if (fin.fail())
      break;

    hash_map<int, char> H1;
    hash_map<int, char> H2;
    vector<char> V;

    for (int i = 0; i < num_c; ++i) {
      fin >> C;
      H1[(C[0] << 8) + C[1]] = C[2];
      H1[(C[1] << 8) + C[0]] = C[2];
    }

    fin >> num_d;
    for (int i = 0; i < num_d; ++i) {
      fin >> D;
      H2[D[0]] = D[1];
      H2[D[1]] = D[0];
    }

    fin >> num_t;
    T = new char[num_t];
    fin >> T;

    magicka(T, num_t, H1, H2, V);

    cout << "Case #" << ++line << ": [";
    if (V.size() > 0) {
      vector<char>::const_iterator iter = V.begin();
      cout << *iter;
      for (++iter;
           iter != V.end();
           ++iter) {
        cout << ", " << *iter;
      }
    }
    cout << "]" << endl;

    // cout << num_c << ' ' << C << ' '
    //      << num_d << ' ' << D << ' '
    //      << num_t << ' ' << T << endl;

    delete [] T;
  }
  fin.close();

  return 0;
}
