#include <fstream>
#include <string>

using namespace std;

ifstream fin ("file1.in");
ofstream fout("file1.out");

const int D_MAX = 5010;
const int L_MAX = 20;
const int N_MAX = 520;

int l, d, n;

string s[D_MAX];
string st;
bool w[N_MAX][L_MAX][300];

int main()
{
	memset(w, 0, sizeof(w));

	fin >> l >> d >> n;

	for (int i = 0; i < d; ++i)
		fin >> s[i];
	
	for (int pos, i = 0; i < n; ++i)
	{
		fin >> st;
		pos = 0;
		for (int j = 0; j < l; ++j)
		{
			if (st[pos] == '(')
			{
				++pos;
				while (st[pos] != ')')
				{
					w[i][j][st[pos]] = true;
					++pos;
				}
				++pos;
			}
			else
			{
				w[i][j][st[pos]] = true;
				++pos;
			}
		}
	}

	for (int ct, i = 0; i < n; ++i)
	{
		ct = 0;
		for (int j = 0; j < d; ++j)
		{
			bool f = true;
			for (int k = 0; k < l; ++k)
				if (!w[i][k][s[j][k]])
				{
					f = false;
					break;
				}
			if (f) ++ct;
		}
		fout << "Case #" << i+1 << ": " << ct << endl;
	}

	return 0;
}                             