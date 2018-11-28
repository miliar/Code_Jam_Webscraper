#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char* argv[])
{
	int C;
	cin >> C;
	for (int i = 0; i < C; i++)
	{
		int N = 0;
		cin >> N;
		int M = 0;
		cin >> M;
		long long x, y, z;
		cin >> x >> y >> z;
		vector<long long> a(M);
		vector<long long> l(N);
		for (int j = 0; j < M; j++)
		{
			cin >> a[j];
		}
		for (int j = 0; j < N; j++)
		{
			l[j] = a[j % M]; 
			a[j % M] = (x * a[j % M] + y * (j + 1)) % z;
		}
		long long c = 0;
		vector<long long> t(N);
		for (int j = N - 1; j >= 0; j--)
		{
			long long lc = 1;
			long long lj = l[j];
			for (int k = j + 1; k < N; k++)
			{
				if (lj < l[k])
					lc += t[k];
				lc %= 1000000007L;
			}
			t[j] = lc;
			c += lc;
			c %= 1000000007L;
		}

		cout << "Case #" << (i+1) << ": " << c << endl;
	}
	return 0;
}
