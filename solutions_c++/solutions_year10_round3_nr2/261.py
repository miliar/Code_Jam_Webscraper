#include <iostream>
#include <cmath>
using namespace std;

long long mypow(long long C, int k)
{
	if (k==0) return C;
	long long tmp = mypow(C,k-1);
	return tmp*tmp;
}

void solve()
{
	long long L, P, C;
	cin >> L >> P >> C;

	if (L*C >= P) { cout << 0 << endl; return; }

	double dP = P, dL = L, dC = C;
	double x = log(dP/dL)/log(dC);
	double k = log(x)/log(2.0);

	int m = (int)k;
	if (m > 0) m--;

	while(L * mypow(C,m) < P)
		m++;
	cout << m << endl;
}

int main()
{
	int ncase; cin >> ncase;
	for(int icase=0; icase < ncase; icase++)
	{
		cout << "Case #" << (icase+1) << ": ";
		solve();
	}
}
