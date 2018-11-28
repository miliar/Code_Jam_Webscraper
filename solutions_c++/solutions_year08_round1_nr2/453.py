#include <iostream>
#include <vector>

using namespace std;

struct Customer
{
	vector<pair<int, int> > pairs;
};

istream &operator>>(istream &in, Customer &customer)
{
	int T;
	in >> T;
	for (int i = 0; i < T; ++i)
	{
		int X, Y;
		cin >> X >> Y;
		customer.pairs.push_back(make_pair(X - 1, Y + 1));
	}
	return in;
}

void output(const vector<int> &result)
{
	static int count = 0;
	cout << "Case #" << ++count << ':';
	if (result.empty())
		cout << " IMPOSSIBLE";
	else
	{
		for (size_t i = 0; i < result.size(); ++i)
			cout << ' ' << (result[i] ? (result[i] - 1) : 0);
	}
	cout << endl;
}

struct compare_by_types
{
	bool operator()(const Customer &lhs, const Customer &rhs)
	{
		return lhs.pairs.size() < rhs.pairs.size();
	}
};

struct compare_by_second
{
	bool operator()(const pair<int, int> &lhs, const pair<int, int> &rhs)
	{
		return lhs.second < rhs.second;
	}
};

bool solve(vector<Customer> &customers, vector<int> &result, size_t depth)
{
	if (depth == customers.size())
		return true;

	Customer &customer = customers[depth];
	sort(customer.pairs.begin(), customer.pairs.end(), compare_by_second());

	for (size_t i = 0; i < customer.pairs.size(); ++i)
	{
		int type = customer.pairs[i].first;
		int status = customer.pairs[i].second;

		if (result[type] != status)
			continue;

		if (solve(customers, result, depth + 1))
			return true;
	}

	for (size_t i = 0; i < customer.pairs.size(); ++i)
	{
		int type = customer.pairs[i].first;
		int status = customer.pairs[i].second;

		if (!result[type])
		{
			// Unused.
			result[type] = status;
			if (solve(customers, result, depth + 1))
				return true;
			result[type] = 0;
		}
	}
	return false;
}

int main()
{
	int C;
	cin >> C;
	for (int i = 0; i < C; ++i)
	{
		int N, M;
		cin >> N >> M;
		vector<Customer> customers(M);
		for (int j = 0; j < M; ++j)
			cin >> customers[j];

		sort(customers.begin(), customers.end(), compare_by_types());

		vector<int> result(N);
		if (solve(customers, result, 0))
			output(result);
		else
			output(vector<int>());
	}

	return 0;
}
