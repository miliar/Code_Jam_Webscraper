#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

const int maxN = 100 + 5;
string S[maxN];
double WP[maxN], OWP[maxN], OOWP[maxN];
int cnt[maxN];

void solve(int cID)
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i ++)
		cin >> S[i];

	for (int i = 0; i < N; i ++)
	{
		cnt[i] = 0;
		WP[i] = 0.0;
		for (int j = 0; j < N; j ++)
			if (S[i][j] != '.') 
			{
				cnt[i] ++;
				WP[i] += (S[i][j] == '1');
			}
		WP[i] /= cnt[i];
	}

	for (int i = 0; i < N; i ++)
	{
		OWP[i] = 0.0;
		for (int j = 0; j < N; j ++)
			if (S[i][j] != '.') 
			{
				double tmp = WP[j] * cnt[j];
				if (S[i][j] == '0') tmp -= 1.0;
				OWP[i] += tmp / (cnt[j] - 1);

			}
		OWP[i] /= cnt[i];
	}

	for (int i = 0; i < N; i ++)
	{
		OOWP[i] = 0.0;
		for (int j = 0; j < N; j ++)
			if (S[i][j] != '.') OOWP[i] += OWP[j];
		OOWP[i] /= cnt[i];
	}

	cout << "Case #" << cID << ":" << endl;
	for (int i = 0; i < N; i ++)
		cout << setprecision(10) << 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i] << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t ++)
		solve(t);
}
