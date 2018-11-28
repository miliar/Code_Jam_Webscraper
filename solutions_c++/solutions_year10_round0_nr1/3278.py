#include <fstream>
#include <cmath>
using namespace std;


int main(int argc, char** argv)
{
  int num_case = 0;
  int pow2[30];
  for ( int i=0; i<=30; ++i )
    {
      pow2[i] = 1<<i;
    }

  ifstream fin;
  fin.open(argv[1]);
  ofstream fout;
  fout.open(argv[2]);

  fin>>num_case;
  for ( int i=0; i<num_case; ++i )
    {
      int N;
      long K;
      fin>>N>>K;
      int pow = pow2[N];
      if ( K%pow == pow-1 )
	fout<<"Case #"<<i+1<<": ON"<<endl;
      else
	fout<<"Case #"<<i+1<<": OFF"<<endl;
    }

  fin.close();
  fout.close();
  return 0;
}
