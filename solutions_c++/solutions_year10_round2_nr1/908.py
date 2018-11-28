#include <iostream>
#include <set>

using namespace std;

int main(int argc, char** argv)
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		int N, M, answer = 0;
		cin >> N >> M;
		set <string> directories;
		directories.insert("/");
		string s;
		for (int j = 0; j < N; ++j)
		{
			cin >> s;
			directories.insert(s);
		}
		
		for (int j = 0; j < M; ++j)
		{
			cin >> s;
			int t = 0;
			while (!directories.count(s) && s.size())
			{
				++t;
				directories.insert(s);
				s = s.substr(0, s.find_last_of("/"));
			}
			answer += t;
		}

		cout << "Case #" << i << ": " << answer << endl;
	}
	return 0;
}
