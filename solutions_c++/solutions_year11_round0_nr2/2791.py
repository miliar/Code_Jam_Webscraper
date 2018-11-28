#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	ifstream in("B-large-0.in");
	ofstream out("B-large-0.out");
	int c[26][26], d[26][26];
	vector<int> ans;
	int T;
	in >> T;
	for (int t = 1; t < T + 1; ++t)
	{
		for (int i = 0; i < 26; ++i) for (int j = 0; j < 26; j++) {c[i][j] = -1; d[i][j] = 0;}
		int C;
		in >> C;
		for (int i = 0; i < C; ++i)
		{
			string s;
			in >> s;
			int a = s[0] - 'A', b = s[1] - 'A';
			c[a][b] = c[b][a] = s[2] - 'A';
		}
		int D;
		in >> D;
		for (int i = 0; i < D; ++i)
		{
			string s;
			in >> s;
			int a = s[0] - 'A', b = s[1] - 'A';
			d[a][b] = d[b][a] = 1;
		}
		int N;
		in >> N;
		ans.clear();
		for (int i = 0; i < N; ++i)
		{
			char raw;
			in >> raw;
			int e = raw - 'A', e2;
			if (!ans.empty() && (e2 = c[ans.back()][e]) != -1)
			{
				ans.pop_back();
				e = e2;
			}
			bool clear = false;
			for(vector<int>::const_iterator j = ans.begin(); j != ans.end(); ++j)
			{
				if (d[*j][e] == 1)
				{
					clear = true;
					break;
				}
			}
			if (clear) ans.clear(); else ans.push_back(e);
		}
		out << "Case #" << t << ": [";
		if (!ans.empty())
		{
			out << static_cast<char>(ans.front() + 'A');
			for(vector<int>::const_iterator j = ans.begin() + 1; j != ans.end(); ++j)
				out << ", " << static_cast<char>((*j) + 'A');
		}
		out << "]\n";
	}
}
