#include <fstream>
#include <string>
#include <set>

using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int T;
	fin >> T;

	for (int i = 1; i <= T; i++)
	{
		int N, M;
		fin >> N >> M;

		set <string> existing;

		for (int j = 0; j < N; j++)
		{
			string s;
			fin >> s;
			existing.insert(s);
		}

		int r = 0;

		for (int j = 0; j < M; j++)
		{
			string s;
			fin >> s;

			int sz = s.size();
			int sep = 0;
			for (int k = 1; k < sz; k++)
			{
				if (s[k] != '/')
					continue;

				sep = k;

				string parent(s.begin(), s.begin() + k);

				if (existing.count(parent) == 0)
				{
					existing.insert(parent);
					r++;
				}
			}

			if (existing.count(s) == 0)
			{
				existing.insert(s);
				r++;
			}
		}

		fout << "Case #" << i << ": " << r << endl;
	}

	return 0;
}
