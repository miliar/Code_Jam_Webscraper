#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

vector<long long> readVector(int n) {
	int value;
	vector<long long> result;
	for (size_t i = 0; i < n; i++)	{
		cin >> value;
		result.push_back(value);
	}
	return result;
}

void spike() {
	int graph[128][128] = {};
	int opposite[128][128] = {};

	int c, d, n;
	cin >> c;
	for (size_t i = 0; i < c; i++) {
		char a,b,c;
		cin >> a >> b >> c;
		graph[a][b] = graph[b][a] = c;
	}

	cin >> d;
	for (size_t i = 0; i < d; i++) {
		char a,b;
		cin >> a >> b;
		opposite[a][b] = opposite[b][a] = 1;
	}

	cin>>n;
	string content; 
	cin >> content;
	vector<char> stack;

	for (size_t i = 0; i < content.size(); i++) {
		stack.push_back(content[i]);
		while (stack.size() >= 2) {
			int s = stack.size();
			char a = stack[s-1], b = stack[s-2];
			if (graph[a][b]) {
				stack.pop_back();
				stack.pop_back();
				stack.push_back(graph[a][b]);
			}
			else 
				break;
		}

		for (int i = 0; i < stack.size() - 1; i++) {
			if(opposite[stack[i]][stack[stack.size() - 1]]) {
				stack.clear();
				break;
			}
		}
	}

	cout << "[" ;
	for (size_t i = 0; i < stack.size(); i++) {
		if (i > 0)
			cout << ", ";
		cout << stack[i];
	}
	cout << "]" << endl;
}

int main() {
	freopen("small.in", "rt", stdin);
	freopen("small.out", "wt", stdout);

	int z;
	cin >> z;
	for (int i = 0; i < z; i++) {
		cout << "Case #" << i+1 << ": ";
		spike();
	}
}