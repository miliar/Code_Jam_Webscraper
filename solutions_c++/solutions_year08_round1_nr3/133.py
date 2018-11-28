#include <fstream>

using namespace std;

long long t, n, sol;
long long c[31][31];


long long pow( long long a, long long b )
{
  long long ret = 1;
  for (long long i = 1; i<=b; i++)
    {
      ret = (ret * a)%1000;
    }
  return ret;
}

int main()
{
  long long i, j, loop;  
  ifstream in("c.in");
  ofstream out("c.out");
  for (i=0; i<=30; i++)
  {
    c[i][0] = 1;
  }
  for (i=1; i<=30; i++)
    for (j=1; j<=i; j++)
      c[i][j] = (c[i-1][j-1]+c[i-1][j])%1000;
  in >> t;
  for (loop=1; loop<=t; loop++)
    {
      in >> n;
      sol = 0;
      for (j=0; j<=n; j+=2)
	{
	  sol = (sol + 2*pow(3, n-j)*pow(5, j/2)*c[n][j])%1000;
	}
      sol --;
      out << "Case #" << loop << ": ";
      if (sol == 0) out << "000" << endl;
      else if (sol<10)  out << "00" << sol << endl;
      else if (sol<100) out << "0" << sol << endl;
      else out << sol << endl;
    }
  in.close();
  out.close();  
  return 0;
}
