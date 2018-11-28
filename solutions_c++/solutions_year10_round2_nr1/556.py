#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

int T, N, M;
set<string> paths;

int append(const string &line)
{
	int count = 0;
	for (int pos = 1; pos < (int)line.length(); ++pos)
	{
		while (line[pos] != '/' && pos < (int)line.length())
			++pos;

		string path = line.substr(0, pos);
		cerr << path << endl;
		if (paths.find(path) == paths.end())
		{
			++count;
			paths.insert(path);
		}
	}

	return count;
}

int main()
{
	cin >> T;

	for (int i = 1; i <= T; ++i)
	{
		paths.clear();

		cin >> N >> M;
		cin.ignore();

		string line;
		for (int j = 0; j < N; ++j)
		{
			getline(cin, line);
			append(line);
		}

		int count = 0;
		for (int j = 0; j < M; ++j)
		{
			getline(cin, line);
			count += append(line);
		}

		cout << "Case #" << i << ": " << count << endl;
	}

	return 0;
}
