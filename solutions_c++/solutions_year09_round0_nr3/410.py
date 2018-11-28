#include <iostream>
#include <fstream>

using namespace std;

const string P = "welcome to code jam";

ifstream fin("in.txt");
ofstream fout("out.txt");

int N;
string S;
int f[501][31];

void solve()
{
	getline(fin, S);
	int lens = S.length();
	int lenp = P.length();
	memset(f, 0, sizeof(f));
	f[0][0] = 1;
	for (int i = 1; i <= lens; ++i)
	{
		f[i][0] = 1;
		for (int j = 1; j <= lenp; ++j)
		{
			f[i][j] = f[i-1][j];
			if (S[i - 1] == P[j - 1])
				f[i][j] += f[i-1][j-1], f[i][j] %= 10000;
		}
	}
//	for (int i = 0; i <= lens; ++i)
//		for (int j = 0; j <= lenp; ++j)
//			cout << f[i][j] << endl;
	int ans = f[lens][lenp];
	if (ans < 10) fout << 0;
	if (ans < 100) fout << 0;
	if (ans < 1000) fout << 0;
	fout << ans << endl;
}


int main()
{
	fin >> N;
	string junk; getline(fin, junk);
	for (int cas = 1; cas <= N; ++cas)
	{
		fout << "Case #" << cas << ": ";
		solve();
	}
	fin.close();
	fout.close();
	return 0;
}
