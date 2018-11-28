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

template<class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cout << "Case #" << caseNumber << ": " << ans.first << endl;
	for (int i = 0; i < ans.second.size() - 1; i++)
		cout << ans.second[i] << " ";
	cout << ans.second.back() << endl;
}

bool IsRoom(const vector< vector<bool> > & graph, const vector<int>& cand) {
	if (cand.size() < 3)
		return false;
	if (!graph[cand[0]][cand[cand.size() - 1]])
		return false;
	for (int i = 0; i < cand.size() - 1; i++)
		if (!graph[cand[i]][cand[i + 1]])
			return false;

	for (int i = 0; i < cand.size(); i++)
		for (int j = i + 2; j < cand.size(); j++)
			if (graph[cand[i]][cand[j]] && (i != 0 || j != cand.size() - 1))
				return false;

	return true;
}

const int maxColors = 5;
vector<int> colors;
vector< vector<int> > rooms;

pair<int, vector<int> > ans;

int GetUsedColors(const vector<int>& room, const vector<int>& colors) {
	vector<bool> usedColors(maxColors + 1, false);
	for (int i = 0; i < room.size(); i++)
		usedColors[colors[room[i]]] = true;
	int count = 0;
	for (int i = 0; i < maxColors + 1; i++)
		count += usedColors[i];
	return count;
}

bool Check(const vector<int>& colors, int usedColors) {
	for (int i = 0; i < rooms.size(); i++) {
		if (GetUsedColors(rooms[i], colors) != usedColors)
			return false;
	}
	return true;
}

void Rec(int deep, int usedColors) {
	if (deep == colors.size()) {
		if (Check(colors, usedColors) && usedColors > ans.first) {
			ans.first = usedColors;
			ans.second = colors;
		}
	} else {
		for (int i = 1; i <= min(maxColors, usedColors + 1); i++) {
			colors[deep] = i;
			Rec(deep + 1, max(i, usedColors));
		}
	}
}


template <class AnswerType>
AnswerType SolveTestCase() {
	int n, m;
	cin >> n >> m;
	vector< vector<bool> > graph(n, vector<bool>(n, 0));
	for (int i = 0; i < n; i++) {
		graph[i][(i + 1) %n ] = true;
		graph[(i + 1) % n ][i] = true;
	}
	
	vector<int> u(m, 0);
	vector<int> v(m, 0);
	for (int i = 0; i < m; i++) {
		cin >> u[i];
	}
	for (int i = 0; i < m; i++) {
		cin >> v[i];
	}

	for (int i = 0; i < m; i++) {
		graph[u[i] - 1][v[i] - 1] = true;
		graph[v[i] - 1][u[i] - 1] = true;
	}

	int len = 1 << n;
	rooms.clear();
	for (int i = 1; i < len; i++) {
		vector<int> candidate;
		for (int j = 0; j < n; j++)
			if (i & (1 << j)) candidate.push_back(j);
		if (IsRoom(graph, candidate))
			rooms.push_back(candidate);
	}

	colors = vector<int>(n, 0);
	ans = make_pair(0, vector<int>());
	Rec(0, 0);
	return ans;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("small.in", "r", stdin);
	//freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase< pair<int, vector<int> > >() );

	return 0;
}