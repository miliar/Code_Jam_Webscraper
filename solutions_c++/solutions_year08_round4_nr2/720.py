#include <iostream>
//#include <string>
//#include <vector>
//#include <list>
//#include <algorithm>
#include <cmath>
using namespace std;
//#define M_PI       3.14159265358979323846
typedef unsigned long long tull;
//const int MAX = 100000;

int main() 
{
  freopen("B-small-attempt3.in", "rt", stdin);
  freopen("B-small-attempt3.out", "wt", stdout);

  int N1;
  cin >> N1;

  tull N,M,A;
  int x1, y1, x2, y2, x3, y3;
  bool fl;
  x1 = 0; y1 = 0;

  for (int inn=0; inn<N1; ++inn)
  {
    cin >> N >> M >> A;
    fl = true;
   // for (x1 = 0; (x1<=N) && fl; ++x1)
     // for (y1 = 0; y1<=M && fl; ++y1)s
      //{
        for (x2 = 0; x2<=N && fl; ++x2)
          for (y2 = 0 ; y2<=M && fl; ++y2)
          {
            for (x3 = 0; x3<=N && fl; ++x3)
              for (y3 = 0; y3<=M && fl; ++y3)
              {
                if (abs((x3-x1)*(y2-y1)-(x2-x1)*(y3-y1))==A)
                {
                  fl = false;
                  cout << "Case #" << inn+1 << ": " << x1 << " " << y1 << " "
                     << x2 << " " << y2 << " " << x3 << " " << y3 << " "<< endl;
                }
              }

          }

      //}

    if (fl)
      cout << "Case #" << inn+1 << ": IMPOSSIBLE" << endl;
  }
  return 0;
}
