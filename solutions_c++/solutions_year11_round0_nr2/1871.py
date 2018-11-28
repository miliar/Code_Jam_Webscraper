#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iostream>
#include <cassert>

using namespace std;

const char base[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
char pairs[256][256];
vector<vector<char> > op;

int visited[256];
string sequence;

void ClearString() {
	sequence.clear();
	memset(visited, 0, sizeof(visited));
}

string solve(const string& input) {
	for (size_t c_ind = 0; c_ind < input.size(); ++c_ind) {
		char curr = input[c_ind];
		while (!sequence.empty()) {
			// Check if we have to combine;
			char old = sequence[sequence.size() - 1];
			if (pairs[curr][old] != -1) {
				curr = pairs[curr][old];
				sequence.resize(sequence.size() - 1);
				--visited[old];
			}
			else {
				break;
			}
		}
		bool should_add = true;
		for (size_t op_ind = 0; op_ind < op[curr].size(); ++op_ind) {
			char oponent = op[curr][op_ind];
			if (visited[oponent] > 0) {
				ClearString();
				should_add = false;
				break;
			}
		}
		if (should_add) {
			++visited[curr];
			sequence.push_back(curr);
		}
	}
	return sequence;
}

void ClearData() {
	memset(pairs, -1, sizeof(pairs));
	op.clear();
	op.resize(256);
	ClearString();
}

void PrintResult()  {
	printf("[");
	for (size_t c_ind = 0; c_ind < sequence.size(); ++c_ind) {
		if (c_ind > 0) {
			printf(", ");
		}
		printf("%c", sequence[c_ind]);
	}
	printf("]");
}

int main() {
	int T, N;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	scanf("%d", &T);
	int k = 0;
	while (k < T) {
		ClearData();
		int C, D;
		cin >> C;
		for (size_t combo_ind = 0; combo_ind < C; ++combo_ind) {
			char a, b, c;
			cin >> a >> b >> c;
			pairs[a][b] = pairs[b][a] = c;
		}
		cin >> D;
		for (size_t op_ind = 0; op_ind < D; ++op_ind) {	
			char a, b;
			cin >> a >> b;
			op[a].push_back(b);
			op[b].push_back(a);
		}

		string input;
		cin >> N >> input;
		solve(input);
		printf("Case #%d: ", k + 1);
		PrintResult();
		printf("\n");
		++k;		
	}
	return 0;
}

