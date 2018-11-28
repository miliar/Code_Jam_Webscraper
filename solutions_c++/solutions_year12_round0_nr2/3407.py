#include <iostream>

using namespace std;

int
main(void)
{
  unsigned int n, t, s, p;
  unsigned int *tp;
  unsigned int res, surp;

  cin >> t;
  for (int tt = 0; tt < t; tt++) {
	cin >> n; cin >> s; cin >> p;
	tp = new unsigned int[n];
	for (int nn = 0; nn < n; nn++)
	  cin >> tp[nn];
	res = 0;
	surp = 0;

	for (int nn = 0; nn < n; nn++) {
	  switch (tp[nn] % 3) {
	  case 0:
		if (tp[nn]/3 >= p) res++;
		else if (tp[nn]/3 + 1 >= p && tp[nn] != 0) surp++;
		break;
	  default:
	  case 1:
		if (tp[nn]/3 + 1 >= p) res++;
		break;
	  case 2:
		if (tp[nn]/3 + 1 >= p) res++;
		else if (tp[nn]/3 + 2 >= p) surp++;
		break;
	  }
	}
	cout << "Case #" << (tt+1) << ": " << (res + ((s > surp) ? surp : s)) <<
	  endl;

	delete[] tp;
  }

  return 0;
}
