#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;

typedef long double ldouble;

typedef ldouble answer_type;

const int N = 20;

double SF[N];
double F[N];
double D[N];

double P(int n, int s)
{
	return F[n] / (F[s] * F[n - s]) * SF[s];
}

void precalc()
{
/*	cout << fixed << setprecision(10);
	cerr << fixed << setprecision(10);
	F[0] = 1.0;
	for (int i = 1; i < N; i++)
	{
		F[i] = i * F[i - 1];
		for (int j = 0; j <= i; j++)
			SF[i] += F[i] / F[j] * (1 - (j % 2) * 2);
	}
	D[0] = 0;
	for (int i = 1; i < N; i++)
	{
		double de = F[i] - SF[i];
		double en = F[i];
		for (int j = 0; j < i; j++)
			en += P(i, j) * D[j];
		D[i] = en / de;
	}
	for (int i = 0; i < N; i++)
		cerr << F[i] << endl;
	cerr << endl;
	for (int i = 0; i < N; i++)
		cerr << SF[i] << endl;
	cerr << endl;
	for (int i = 0; i < N; i++)
		cerr << D[i] << endl;
	cerr << endl;
*/
	cerr << "precalc finished" << endl;
}

answer_type solve()
{
	int n;
	cin >> n;
	int t;
	int s = 0;
	for (int i = 1; i <= n; i++)
	{
		cin >> t;
		s += t != i;
	}
	return s;
}

int main()
{
	precalc();
	int T;
	cin >> T;
	answer_type ans;
	for (int i = 1; i <= T; i++)
		ans = solve(),
		cout << "Case #" << i << ": " << ans << endl,
		cerr << "Case #" << i << ": " << ans << endl;
}
