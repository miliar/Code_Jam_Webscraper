#include <fstream>

using namespace std;

bool contained(int a1, int b1, int a2, int b2)
{
	return a1 > a2 && b1 < b2;
}

int solve(int *a, int *b, int N)
{
	int r = 0;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < i; j++)
			if (contained(a[i], b[i], a[j], b[j]) ||
			    contained(a[j], b[j], a[i], b[i]))
			    r++;

	return r;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int T;
	fin >> T;

	for (int i = 1; i <= T; i++)
	{
		int N;
		fin >> N;

		int a[N], b[N];

		for (int j = 0; j < N; j++)
			fin >> a[j] >> b[j];

		fout << "Case #" << i << ": " << solve(a, b, N) << endl;
	}

	return 0;
}
