#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

void output_result(int result)
{
	static int case_id = 0;
	cout << "Case #" << ++case_id << ": " << result << endl;
}

void solve(map<string, bool> &engines, const vector<string> &queries)
{
	size_t true_count = 0;
	int switch_count = 0;

	for (size_t i = 0; i < queries.size(); ++i)
	{
		if (!engines[queries[i]])
		{
			if (true_count == engines.size() - 1)
			{
				// Clears flags.
				for (map<string, bool>::iterator it = engines.begin();
					it != engines.end(); ++it)
				{
					it->second = false;
				}

				++switch_count;
				true_count = 0;
			}

			engines[queries[i]] = true;
			++true_count;
		}
	}

	output_result(switch_count);
}

int main()
{
	int num_cases;
	cin >> num_cases;

	for (int i = 0; i < num_cases; ++i)
	{
		int num_engines;
		cin >> num_engines;

		string line;
		getline(cin, line);

		// Reads engine names.
		map<string, bool> engines;
		for (int j = 0; j < num_engines; ++j)
		{
			getline(cin, line);
			engines[line] = false;
		}

		int num_queries;
		cin >> num_queries;

		getline(cin, line);

		// Reads queries.
		vector<string> queries;
		for (int i = 0; i < num_queries; ++i)
		{
			getline(cin, line);
			queries.push_back(line);
		}

		solve(engines, queries);
	}

	return 0;
}
