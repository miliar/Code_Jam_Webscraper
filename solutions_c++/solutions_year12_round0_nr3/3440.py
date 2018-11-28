#include <iostream>

using namespace std;

unsigned int
deg(unsigned int n)
{
  unsigned int d = 1;

  while (n / d != 0)
	d *= 10;

  return d;
}

bool
permp(unsigned int n, unsigned int m, unsigned int d)
{
  unsigned int dd = 10;

  while (d /= 10) {
	if ((n % d)*dd + (n / d) == m)
	  return true;
	dd *= 10;
  }

  return false;
}

int
main(void)
{
  unsigned int t, a, b;
  unsigned int n, m;
  unsigned int res = 0;
  unsigned int d;

  cin >> t;
  for (int tt = 0; tt < t; tt++) {
	cin >> a; cin >> b;

	res = 0;
	d = deg(a);
	for (n = a; n <= b; n++) {
	  for (m = n + 1; m <= b; m++) {
		if (permp(n, m, d))
		  res++;
	  }
	}

	cout << "Case #" << (tt+1) << ": " << res << endl;
  }

  return 0;
}
