#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct Node
{
	int G;  // Gate.
	int C;  // Changable or not.
	int cost;
	int value;
};

istream &operator>>(istream &in, Node &node)
{
	node.cost = 0;
	node.value = -1;
	return in >> node.G >> node.C;
}

int solve_one(vector<Node> &nodes, int n);

int solve_one(vector<Node> &nodes, int n, int C)
{
	n = n * 2 + 1;

	int left = solve_one(nodes, n);
	int right = solve_one(nodes, n + 1);
	cout << "IN " << C << ' ' << n + 1 << ": " << left << ", " << right << endl;

	if (C)
	{
		if (left < 0 || right < 0)
			return -1;
		return left + right;
	}

	if (left < 0)
		return right;
	else if (right < 0)
		return left;

	return min(left, right);
}

int solve_one(vector<Node> &nodes, int n)
{
	if (nodes[n].value == 1)
		return 0;
	else if (nodes[n].value == 0)
		return -1;

	if (nodes[n].G)
	{
		int as_is = solve_one(nodes, n, nodes[n].C);
		int changed = solve_one(nodes, n, !nodes[n].C) + 1;
		cout << n + 1 << ": " << as_is << ", " << changed << endl;
		return min(as_is, changed);
	}
	else
	{
		cout << n + 1 << ": " << solve_one(nodes, n, nodes[n].C) << endl;
		return solve_one(nodes, n, nodes[n].C);
	}

	return -1;
}

int main()
{
	int N;
	cin >> N;
	cerr << "N: " << N << endl;

	for (int i = 0; i < N; ++i)
	{
		int M, V;
		cin >> M >> V;

		cerr << "Case: " << i << ": " << M << ", " << V << endl;

		vector<Node> nodes(M);
		for (int j = 0; j < (M - 1) / 2; ++j)
		{
			cin >> nodes[j];
			if (!V)
				nodes[j].G = !nodes[j].G;
		}

		for (int j = (M - 1) / 2; j < M; ++j)
		{
			nodes[j].cost = 0;
			cin >> nodes[j].value;
			if (!V)
				nodes[j].value = !nodes[j].value;
		}

		for (int j = (M - 1) / 2 - 1; j >= 0; --j)
		{
			Node &node = nodes[j];
			Node &left = nodes[j * 2 + 1];
			Node &right = nodes[j * 2 + 2];

			if (node.G)
			{
				node.cost = 1 << 20;
				node.value = left.value & right.value;
				if (node.value)
					node.cost = left.cost + right.cost;

				if (node.C)
				{
					int value = left.value | right.value;
					if (value)
					{
						int cost = 1 << 20;
						if (left.value)
							cost = left.cost;
						if (right.value)
							cost = min(cost, right.cost);

						if (cost < node.cost)
						{
							node.value = value;
							node.cost = cost + 1;
						}
					}
				}
			}
			else
			{
				node.cost = 1 << 20;
				node.value = left.value | right.value;
				if (node.value)
				{
					if (left.value)
						node.cost = left.cost;
					if (right.value)
						node.cost = min(node.cost, right.cost);
				}
			}
			cerr << "node: " << j + 1 << ", " << node.cost << endl;
		}

		if (nodes[0].cost > 1 << 19)
			cout << "Case #" << (i + 1) << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << (i + 1) << ": " << nodes[0].cost << endl;
	}

	return 0;
}
