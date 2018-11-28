#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void output_result(int num_a, int num_b)
{
	static int case_id = 0;
	cout << "Case #" << ++case_id << ": "
		<< num_a << ' ' << num_b << endl;
}

int read_time()
{
	int hour, min;
	char dummy;
	cin >> hour >> dummy >> min;
	return hour * 60 + min;
}

void solve(vector<pair<int, int> > &a_pairs, vector<pair<int, int> > &b_pairs)
{
	bool is_a = false;
	int num_a = 0, num_b = 0;
	pair<int, int> time_chosen;

	// The number of trips is small, no problem.
	while (!a_pairs.empty() && !b_pairs.empty())
	{
		// Puts a new train.
		is_a = (a_pairs.front() < b_pairs.front());
		if (is_a)
		{
			time_chosen = a_pairs.front();
			a_pairs.erase(a_pairs.begin());
			++num_a;
		}
		else
		{
			time_chosen = b_pairs.front();
			b_pairs.erase(b_pairs.begin());
			++num_b;
		}

		// Checks the other side;
		for (is_a = !is_a; is_a ? !a_pairs.empty() : !b_pairs.empty();
			is_a = !is_a)
		{
			// Departure time is no use.
			time_chosen.first = time_chosen.second;

			if (is_a)
			{
				vector<pair<int, int> >::iterator earliest_it =
					lower_bound(a_pairs.begin(), a_pairs.end(), time_chosen);
				if (earliest_it == a_pairs.end())
					break;
				time_chosen = *earliest_it;
				a_pairs.erase(earliest_it);
			}
			else
			{
				vector<pair<int, int> >::iterator earliest_it =
					lower_bound(b_pairs.begin(), b_pairs.end(), time_chosen);
				if (earliest_it == b_pairs.end())
					break;
				time_chosen = *earliest_it;
				b_pairs.erase(earliest_it);
			}
		}
	}

	output_result(num_a + a_pairs.size(), num_b + b_pairs.size());
}

int main()
{
	int num_cases;
	cin >> num_cases;

	for (int i = 0; i < num_cases; ++i)
	{
		int turnaround_time;
		cin >> turnaround_time;

		int n_from_a, n_from_b;
		cin >> n_from_a >> n_from_b;

		// Reads time tables and adds a penalty to arrival time.
		vector<pair<int, int> > a_pairs, b_pairs;
		for (int j = 0; j < n_from_a; ++j)
		{
			int departure_time = read_time();
			int arrival_time = read_time() + turnaround_time;
			a_pairs.push_back(make_pair(departure_time, arrival_time));
		}
		for (int j = 0; j < n_from_b; ++j)
		{
			int departure_time = read_time();
			int arrival_time = read_time() + turnaround_time;
			b_pairs.push_back(make_pair(departure_time, arrival_time));
		}

		// Sorts by departure time.
		sort(a_pairs.begin(), a_pairs.end());
		sort(b_pairs.begin(), b_pairs.end());

		solve(a_pairs, b_pairs);
	}

	return 0;
}
