
#include <iostream>

using namespace std;

bool test(int p, int v, int D, int N, int* po, int *le)
{
	//cout << "test: " << p << " " << v << endl;
	int man = po[v] - p;
	if (man > le[v]) man = le[v];

	//cout << "man = " << man << endl;

	if (po[v] + man >= D) return true;

	int zv = v + 1;
	while (zv < N && po[zv] <= po[v] + man) zv++;

	for (int i = zv-1; i > v; i--)
	{
		//if (le[zv] < man) continue;
		if (test(po[v], i, D, N, po, le)) return true;
	}

	return false;
}

void main2()
{
	int N, D;
	cin >> N;

	int* po = new int[N];
	int* le = new int[N];

	for (int i = 0; i < N; i++)
	{
		cin >> po[i];
		cin >> le[i];
	}

	cin >> D;

	bool res = test(0, 0, D, N, po, le);

	cout << ((res) ? "YES" : "NO");

	delete [] po;
	delete [] le;
}

int main()
{
	int N;

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cout << "Case #" << (i+1) << ": ";
		main2();
		cout << endl;
	}

	return 0;
}

