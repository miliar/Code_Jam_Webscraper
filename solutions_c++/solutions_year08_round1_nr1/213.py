#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

vector <long long> v1, v2;
long long t, n;
long long sol;

int main()
{
  ifstream in("a.in");
  ofstream out("a.out");
  in >> t;
  for (long long loop = 1; loop <= t; loop++)
    {
      long long i;
      in >> n;
      v1.resize(n); 
      v2.resize(n);
      for (i=0; i<n; i++) in >> v1[i];
      for (i=0; i<n; i++) in >> v2[i];
      sort(v1.begin(), v1.end());
      sort(v2.begin(), v2.end());
      sol = 0;
      for (i=0; i<n; i++)
	sol += v1[i]*v2[n-1-i];
      out << "Case #" << loop << ": " << sol << endl;
    }
  in.close();
  out.close();
  return 0;
}
