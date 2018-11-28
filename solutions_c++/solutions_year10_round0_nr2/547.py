#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef unsigned long long ull;

ull gcd(ull a, ull b)
{
  if (a<b)
    return gcd(b,a);
  if (b==0)
    return a;

  return gcd(b,a-(a/b)*b);
}

int main()
{
  int C,N;
  vector<ull> t;
  ull T;

  cin >> C;
  for (int c=0; c<C; c++)
    {
      cin >> N;
      t.resize(N);
      for (int i=0; i<N; i++)
	{
	  cin >> t[i];
	}

      cout << "Case #" << c+1 << ": ";

      T=0;
      ull d;
      for (int i=0; i<N-1; i++)
	{
	  for (int j=i+1; j<N; j++)
	    {
	      d = (t[i]>t[j] ? t[i]-t[j] : t[j]-t[i]);
	      T=gcd(d,T);
	    }
	}

      cout << (t[0]%T>0 ? T-(t[0]%T) : 0);

      cout << endl;
    }

  return 0;
}
