#include <algorithm>
#include <fstream>
#include <vector>
#include <string>
#include <set>

using namespace std;


void format(string& s)
{
	string::size_type pos = s.find_last_of('/');
	s.erase(pos, string::npos);
}

int main(int argc, char* argv[])
{
	std::ifstream input_file("in");
	std::ofstream output_file("out");

	size_t count_tests = 0;
	input_file >> count_tests;

	for (size_t i = 0; i < count_tests; ++i)
	{
		int N = 0, M = 0;
		input_file >> N >> M;
		////

		set<string> has;
		for (int j = 0; j < N; ++j)
		{
			char a[110] = {};
			input_file >> a;
			has.insert(a);
		}
		has.insert("");

		vector<string> need;
		for (int j = 0; j < M; ++j)
		{
			char a[110] = {};
			input_file >> a;
			need.push_back(a);
		}


		size_t cnt = 0;

		for (int j = 0; j < M; ++j)
		{
			string s = need[j];
			while (has.find(s) == has.end())
			{
				++cnt;
				has.insert(s);
				format(s);
			}
		}

		////
		output_file << "Case #" << i+1 << ": ";
		output_file << cnt << std::endl;	
	}

	input_file.close();
	output_file.close();

	return 0;
}