#include <iostream>
#include <fstream>

using namespace std;

int L, D, N;
string dict[5001];
bool used[16][27];

ifstream fin("in.txt");
ofstream fout("out.txt");

void solve()
{
	memset(used, 0, sizeof(used));
	for (int i = 0; i < L; ++i)
	{
		char temp;
		fin >> temp;
		if (temp == '(')
		{
			do
			{
				fin >> temp;
				if (temp == ')') break;
				used[i][temp-'a'] = 1;
			}
			while (1);
		}
		else
			used[i][temp-'a'] = 1;
	}

	int ans = 0;
	for (int i = 0; i < D; ++i)
	{
		bool match = 1;
		if ((int)dict[i].length() != L) continue;
		for (int j = 0; j < L; ++j)
		{
			if (used[j][dict[i][j]-'a']) continue;
			match = 0; break;
		}
		if (match) ++ans;
	}

	fout << ans << endl;
}

int main()
{
	fin >> L >> D >> N;
	for (int i = 0; i < D; ++i)
		fin >> dict[i];
	for (int cas = 1; cas <= N; ++cas)
	{
		fout << "Case #" << cas << ": ";
		solve();
	}
	fin.close();
	fout.close();
	return 0;
}
