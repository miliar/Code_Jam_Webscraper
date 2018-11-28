#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

struct Edge {
	int begin;
	int end;
	long long cost;
};

template<typename AnswerType>
AnswerType SolveTestCase(int runs, long long capacity, vector<long long> groups)
{
	vector<bool> visited(groups.size(), false);
	
	size_t cur = 0;
	vector<Edge> edges;
	do {
		visited[cur] = true;
		long long sum = 0;
		size_t pos = cur;
		while (sum + groups[pos] <= capacity) {
			sum += groups[pos];
			pos++;
			if (pos == groups.size())
				pos = 0;
			if (pos == cur)
				break;
		}
		edges.push_back(Edge());
		edges.back().begin = cur;
		edges.back().end = pos;
		edges.back().cost = sum;
		cur = pos;
	} while (!visited[cur]);
	size_t artPoint = 0;
	for (size_t i = 0; i < edges.size(); i++)
		if (edges[i].begin == edges.back().end)
			artPoint = i;
	
	
	long long ans = 0;
	for (size_t i = 0; i < min(runs, (int)artPoint); i++)
		ans += edges[i].cost;
	if (runs > artPoint) {
		long long cycleCost = 0;
		for (size_t i = artPoint; i < edges.size(); i++)
			cycleCost += edges[i].cost;
		ans += cycleCost * ( (runs - artPoint) / (edges.size() - artPoint) );
		for (size_t i = 0; i < (runs - artPoint) % (edges.size() - artPoint); i++)
			ans += edges[artPoint + i].cost;
	}
	return ans;
}

template<typename AnswerType>
void PrintAnswerToTestCase(int caseNumber, AnswerType ans)
{
	cout << "Case #" << caseNumber << ": " << ans << endl;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);
	
	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++) {
		int runs, n;
		long long capacity;
		cin >> runs >> capacity >> n;
		vector<long long> groups(n);
		for (size_t i = 0; i < groups.size(); i++)
			cin >> groups[i];
		PrintAnswerToTestCase(caseNumber, SolveTestCase<long long>(runs, capacity, groups));
	}

	return 0;
}