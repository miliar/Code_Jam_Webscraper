#include <fstream>
//#include <iostream> //debugging
#include <cmath>
using namespace std;

int main(int argc, char* argv[])
{
  ifstream in(argv[1]);
  ofstream out("output");

  int T;
  in >> T;

  for(int t = 1;t <= T;++t)
  {
    //cerr << "t: " << t << endl;
    int N, S, p;
    in >> N >> S >> p;

    //cerr << "N: " << N << ", S: " << S << ", p: " << p << endl;

    //number of totals at p-1 and which can benefit from a bump
    int nclose = 0;
    //number that are already at p or higher
    int ngood = 0;
    for(int i = 0;i < N;++i)
    {
      int total;
      in >> total;
      if(ceil(total/3.0) >= p)
        ++ngood;
      else if(total != 0 && total%3 != 1 && ceil(total/3.0) == p-1)
        ++nclose;
    }

    //cerr << "nclose: " << nclose << endl;
    //cerr << endl;

    out << "Case #" << t << ": " << ngood + min(nclose,S) << endl;
  }

  in.close();
  out.close();

  return 0;
}
