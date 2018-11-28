#include <iostream>
#include <fstream>
#include <cmath>


using namespace std;

#define for_all(V, B) for(int V = 0; V < B; V++)
#define for_all_dec(V, B) for(int V = B - 1; V >= 0; V--)
#define READ(X) in >> X;
#define DECREAD(T, X) T X; in >> X;

int ps[200];

int main(int argc, char* argv[])
{
  ifstream in(argv[1]);
  if (!in.good())
    cout << "Cannot open file " << argv[1] << std::endl;


  DECREAD(int, T);

  for_all(t, T)
  {
    DECREAD(int, N);
    DECREAD(int, L);
    DECREAD(int, H);
    for_all(n, N)
      READ(ps[n]);

    unsigned f;
    for (f = L; f <= H; f++)
    {
      bool found = true;
      for_all(n, N)
      {
        if ((f % ps[n]) && (ps[n] % f))
        {
          found = false;
          break;
        }
      }
      if (found) goto ok;
    }

    ko:
       cout << "Case #" << (t+1) << ": NO" << endl;
    continue;
    ok:
       cout << "Case #" << (t+1) << ": " << f << endl;

  }

  return 0;
}
