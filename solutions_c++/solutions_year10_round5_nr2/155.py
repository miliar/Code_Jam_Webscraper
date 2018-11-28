#include<fstream>
#include<algorithm>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

const int maxl = 100000;
int b[maxl];

void work()
{
	long long l;
	int n;
	fin >> l >> n;
	int a[n], c = 0;
	fill(b, b + maxl, maxl);
	for (int i = 0; i < n; i++) {
		fin >> a[i];
		c = max(a[i], c);
	}
	b[0] = 0;
	for (int i = 1; i < maxl; i++)
		for (int j = 0; j < n; j++)
			if (a[j] <= i)
				b[i] = min(b[i-a[j]]+1, b[i]);
	long long p = (l - maxl) / c + 1;
	l -= p * c;
	if (b[l] >= maxl)
		fout << "IMPOSSIBLE\n";
	else
		fout << b[l] + p << endl;
}

int main()
{
	int t, m = 0;
	fin >> t;
	while (t--) {
		fout << "Case #" << ++m << ": ";
		work();
	}
}
