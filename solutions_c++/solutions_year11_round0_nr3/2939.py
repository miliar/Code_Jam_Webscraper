#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main()
{
	int T, N, ans, partition, limit, sum1, sum2, xor1, xor2;
	vector<int> C;
	ifstream in("C-small-0.in");
	ofstream out("C-small-0.out");
	in >> T;
	for (int t = 1; t < T + 1; ++t)
	{
		in >> N;
		C.resize(N);
		for (int i = 0; i < N; ++i) in >> C[i];
		ans = -1;
		partition = 1;
		limit = (1 << N) - 1;
		while (partition < limit)
		{
			sum1 = sum2 = xor1 = xor2 = 0;
			for (int i = 0; i < N; ++i)
			{
				if ((partition & (1 << i)) != 0)
				{
					sum1 += C[i];
					xor1 ^= C[i];
				}
				else
				{
					sum2 += C[i];
					xor2 ^= C[i];
				}
			}
			if (xor1 == xor2) ans = max(ans, max(sum1, sum2));
			++partition;
		}
		if (ans != -1)
			out << "Case #" << t << ": " << ans << '\n';
		else
			out << "Case #" << t << ": NO\n";
	}
}
