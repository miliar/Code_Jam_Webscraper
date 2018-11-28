#include <vector>
#include <iostream>
using namespace std;

inline int abs(int x) {	return x < 0 ? (-x):x; }

int main(void)
{
	int T, N, p;
	char c;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> N;
		vector <int> O, B;
		vector <char> seq;
		for (int i = 0; i<N; i++)
		{
			cin >> c >> p;
			seq.push_back(c);
			if (c == 'O')	O.push_back(p);
			else	B.push_back(p);
		}
		int o = 1, b = 1, iO = 0, iB = 0, ans = 0;
		for (int i = 0; i<seq.size(); i++)
			if ( seq[i] == 'O')
			{
				ans += abs(O[iO] - o) + 1;
				if ( iB < B.size())
					b = ( B[iB] >= b ? min(B[iB], b + abs(O[iO] - o) + 1):max(B[iB], b - abs(O[iO]-o) - 1));
				o = O[iO], iO++;
			}
			else
			{
				ans += abs(B[iB] - b) + 1;
				if ( iO < O.size())
					o = ( O[iO] >= o ? min(O[iO], o + abs(B[iB] - b) + 1):max(O[iO], o - abs(B[iB]-b) - 1));
				b = B[iB], iB++;
			}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
