#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

int runs, N, M;

int main()
{
	freopen("a_large.in", "r", stdin);
	freopen("a_large.out", "w", stdout);

	map<string, bool> dirs;

	cin >> runs;
	for (int run = 1; run <= runs; ++run)
	{
		dirs.clear();
		dirs.insert(pair<string, bool>("/", true));
		string line;
		cin >> N >> M;
		getline(cin, line);
		int count = 0;
		for (int i = 0; i < N; ++i)
		{
			getline(cin, line);
			line += "/";
			for (int j = 1; j < line.size(); ++j)
				if (line[j] == '/')
					dirs.insert(pair<string, bool>(line.substr(0, j), true));
		}
		for (int i = 0; i < M; ++i)
		{
			getline(cin, line);
			line += "/";
			for (int j = 1; j < line.size(); ++j)
				if (line[j] == '/')
				{
					string tmp = line.substr(0, j);
					if (dirs.find(tmp) == dirs.end())
					{
						count++;
						//cout << tmp << endl;
						dirs.insert(pair<string, bool>(tmp, true));
					}
				}
		}
		cout << "Case #" << run << ": " << count << endl;
	}
}
