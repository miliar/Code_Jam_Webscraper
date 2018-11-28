#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
	char R;
	int T, N, P, pO, pB, dO, dB, d, ans;
	ifstream in("A-large-0.in");
	ofstream out("A-large-0.out");
	in >> T;
	for (int t = 1; t < T + 1; ++t)
	{
		in >> N;
		pO = pB = 1;
		dO = dB = 0;
		ans = 0;
		while (N-->0)
		{
			in >> R >> P;
			if (R == 'O')
			{
				d = max(0, abs(P - pO) - dO) + 1;
				pO = P;
				dO = 0;
				dB += d;
				ans += d;
			}
			else
			{
				d = max(0, abs(P - pB) - dB) + 1;
				pB = P;
				dB = 0;
				dO += d;
				ans += d;
			}
		}
		out << "Case #" << t << ": " << ans << '\n';
	}
}
