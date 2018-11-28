#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin("in");
	ofstream fout("out");
	int T;
	fin >> T;
	for (int C = 1; C <= T; C++)
	{
		int P;
		int tmp;
		fin >> P;
		int W[1025];
		for (int i = 1; i <= (1 << P); i++)
			fin >> W[i];
		for (int i = 0; i < P; i++)
			for (int j = 0; j < (1 << (P - i - 1)); j++)
				fin >> tmp;
		int need[1024];
		memset(need, 0, sizeof(need));
		for (int i = 1; i <= (1 << P); i++)
		{
			W[i] = P - W[i];
			double pos = (1 << (P-1)) + 0.5;
			int cur = 1;
			for (int j = 0; j < W[i]; j++)
			{
				need[cur] = 1;
				if (pos < i)
				{
					cur = 2 * cur;
					pos -= (1 << (P - 2 - j));
				}
				else
				{
					cur = 2 * cur + 1;
					pos += (1 << (P - 2 - j));
				}
			}
		}
		int ans = 0;
		for (int i = 1; i < 1024; i++)
			ans += need[i];
		cout << "Case #" << C << ": " << ans << endl;
		fout << "Case #" << C << ": " << ans << endl;
	}
}