#include <iostream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

const int maxn = 500000;
const int maxm = 100;
const long prime = 1000000007;

long data[maxn];
long f[maxn];
long A[maxm];

int main()
{
	int N;
	int tc;
	cin >> N;
	for (tc = 0; tc < N; tc ++)
	{
		long long X,Y,Z;
		long n,m;
		long count = 0;
		cin >> n >> m >> X >> Y >> Z;
		for (int i=0; i<m; i++)
			cin >> A[i];
		for (int i=0; i<n; i++)
		{
			data[i] = A[i % m];
			assert(data[i] >= 0);
			A[i % m] = (X * A[i % m] + Y * (i+1)) % Z;
		}
		for (int i=n-1; i>=0; i--)
		{
			f[i] = 1;
			for (int j=i+1; j<n; j++)
				if (data[j] > data[i])
					f[i] = (f[i] + f[j]) % prime;
			count = (count + f[i]) % prime;
		}
		cout << "Case #" << tc+1 << ": " << count << endl;
	}
	return 0;
}

