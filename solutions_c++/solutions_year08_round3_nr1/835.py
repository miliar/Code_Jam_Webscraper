#include <math.h>
#include <iostream>
#include <vector>

using namespace std;
// const double pi = 2.0 * acos(0.0);

void solve();

void main()
{
	long i, N = 0;

	cin >> N;
	for(i = 0;i < N;++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}

int compare(const void *p1, const void *p2)
{
	long l1 = *(long *)p1;
	long l2 = *(long *)p2;

	if(l1 == l2)
		return 0;
	if(l1 > l2)
		return -1;
	return 1;
}

void solve()
{
	long i;
	long P, K, L;
	long f[100];
	long k[12];

	cin >> P >> K >> L;
	for(i = 0;i < 100;++i)
		f[i] = 0;
	for(i = 0;i < L;++i)
		cin >> f[i];
	qsort(f, 100, sizeof(long), &compare);
	for(i = 0;i < 12;++i)
		k[i] = 1;

	long min = 0, currk = 0;

	for(i = 0;i < L;++i)
	{
		min += k[currk] * f[i];
		++k[currk];
		currk = (currk + 1) % K;
	}
	cout << min;
	cerr << ".";
}
