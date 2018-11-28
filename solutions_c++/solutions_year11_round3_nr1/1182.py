#include <iostream>
#include <fstream>
#include <cmath>


using namespace std;

#define for_all(V, B) for(int V = 0; V < B; V++)
#define for_all_dec(V, B) for(int V = B - 1; V >= 0; V--)
#define READ(X) in >> X
#define DECREAD(T, X) T X; in >> X

int main(int argc, char* argv[])
{
  ifstream in(argv[1]);
  if (!in.good())
    cout << "Cannot open file " << argv[1] << std::endl;

  DECREAD(int, T);

  for_all(t, T)
  {
    DECREAD(int, R);
    DECREAD(int, C);

    char tab[100][100];

    for_all(r, R)
      for_all(c, C)
        READ(tab[r][c]);

    for_all(r, R)
      for_all(c, C)
    {
      if (tab[r][c] == '#')
      {
        if (r == R-1 || c == C-1 ||
            tab[r][c+1] != '#' || tab[r+1][c] != '#' ||
            tab[r+1][c+1] != '#') goto impossible;

        tab[r][c] = tab[r+1][c+1] = '/';
        tab[r][c+1] = tab[r+1][c] = '\\';
      }
    }

  possible:
    cout << "Case #" << (t+1) << ":" << endl;
    for_all(r, R)
    {
      for_all(c, C)
      {
        cout << tab[r][c]; 
      }
      cout << endl;
    }
    continue;
  impossible:
    cout << "Case #" << (t+1) << ":\nImpossible" << endl;
  }

  return 0;
}
