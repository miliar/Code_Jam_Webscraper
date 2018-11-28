#include <iostream>
#include <cmath>
#include <set>

using namespace std;

int p10[] = {1, 10, 100, 1000, 10000, 100000, 1000000};
int A, B;
typedef pair<int, int> rec;
set<rec> seta;

void
func(int n)
{
	int d, m = n, i;
	int l = ceil(log(n)/log(10));

	for(i = 1; i < l; ++i)
	{
		d = m / p10[l-1];
		m = m % p10[l-1];
		m *= 10;
		m += d;
		if(m > n && m <= B)
			seta.insert(rec(n, m));
	}
}

int
main()
{
	int T, ca=0, i;

	cin >> T;
	while(T--)
	{
		cin >> A >> B;
		seta.clear();
		for(i = A; i < B; ++i)
			func(i);
		cout << "Case #" << ++ca << ": " << seta.size() << endl;
	}

	return 0;
}

