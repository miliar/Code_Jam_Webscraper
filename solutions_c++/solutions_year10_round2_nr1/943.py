// A.cpp : Defines the entry point for the console application.
//

#include <fstream>

#include <set>
#include <string>

typedef std::set< std::string > StringSet;
std::ifstream in("A-large.in");
std::ofstream out("A.out");

int solve()
{
	int N, M;
	in >> N >> M;

	StringSet folders;
	folders.insert("/");

	for (int i = 0; i < N; ++i)
	{
		std::string s;
		in >> s;

		int j = 0;
		while (j < s.size())
		{
			++j;
			for(; (s[j] != '/') && j < s.size(); ++j);
			folders.insert(s.substr(0, j));
		}
	}

	int result = 0;

	for (int i = 0; i < M; ++i)
	{
		std::string s;
		in >> s;

		int j = 0;
		while (j < s.size())
		{
			++j;
			for(; (s[j] != '/') && j < s.size(); ++j);

			std::string folder = s.substr(0, j);
			if (folders.end() == folders.find(folder))
			{
				++result;
				folders.insert(folder);
			}
		}
	}

	return result;
}

int main()
{
	int T;
	in >> T;

	for (int i = 0; i < T; ++i)
	{
		out << "Case #" << (i + 1) << ": " << solve() << "\n";
	}

	return 0;
}

