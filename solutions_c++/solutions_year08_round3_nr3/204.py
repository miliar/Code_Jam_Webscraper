#include <iostream>
#include <vector>
#include <numeric>
#include <list>
#include <map>
#include <CGAL/Gmpz.h>

using namespace std;

long m_arr[101];

int main()
{
  int N;
  cin >> N;
  
  for (int i = 0; i < N; ++i)
    {
      long long n, m, X, Y, Z;
      cin >> n >> m >> X >> Y >> Z;
      
      typedef map<long, long long> Map;
      Map res;

      for (int j = 0; j < m; ++j)
	{
	  int x; cin >> x;
	  m_arr[j] = x;
	}

      for (int j = 0; j < n; ++j)
	{
	  long p = m_arr[j % m];
	  m_arr[j % m] = (X * m_arr[j % m] + Y * (j + 1)) % Z;
	  
	  Map::iterator it = res.lower_bound(p);
	  long long sum = 1;
	  for (Map::iterator jt = res.begin();
	       jt != it; ++jt)
	    {
	      sum += jt->second;
	    }
	  sum %= 1000000007;
	  if ((it = res.find(p)) == res.end())
	    {
	      res.insert(make_pair(p, sum));
	    }
	  else
	    {
	      it->second += sum;
	      it->second %= 1000000007;
	    }
	}
      
      long long sum = 0;
      for (Map::iterator jt = res.begin();
	   jt != res.end(); ++jt)
	{
	  sum += jt->second;
	  sum %= 1000000007;
	}

      cout << "Case #" << i + 1 << ": " << sum << endl;
    }

  return 0;
}
