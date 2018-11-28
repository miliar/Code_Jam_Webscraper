#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

const int MAX_LEN = 30;
const int MAX_N = 105;
const int MAX_CHAR = 256;

int n, m;
string word[MAX_N];
char buffer[MAX_LEN];
bool has[MAX_N][MAX_CHAR];
string choice;
bool avail[MAX_N];
string written;

bool to_try(char c) {
	bool ok = false;
	for (int i = 0; i < n; i++) if (avail[i] && has[i][(int) c]) {
		ok = true;
		break;
	}
	return ok;
}

bool match(int x, char c) {
	for (int i = 0; i < (int) word[x].size(); i++) {
		if (written[i] == c && word[x][i] != c)
			return false;
		else if (written[i] != c && word[x][i] == c)
			return false;
	}
	return true;
}

int eval(char c, int ans) {
	if (has[ans][(int) c]) {
		for (int i = 0; i < (int) word[ans].size(); i++) if (word[ans][i] == c)
			written[i] = c;

		for (int i = 0; i < n; i++) if (avail[i] && !match(i, c))
			avail[i] = false;

		return 0;
	}
	else {
		for (int i = 0; i < n; i++) if (has[i][(int) c])
			avail[i] = false;

		return 1;
	}
}

int main() {
	int tests; scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		fill(*has, *has + MAX_N*MAX_CHAR, false);

		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", buffer);
			word[i] = buffer;

			for (int j = 0; j < (int) word[i].size(); j++)
				has[i][(int) word[i][j]] = true;
		}

		vector < string > ans;
		while (m--) {
			scanf("%s", buffer);
			choice = buffer;

			int points = 0, curr = 0;
			for (int target = 0; target < n; target++) {
				fill(avail, avail + MAX_N, true);
				for (int i = 0; i < n; i++) if (word[i].size() != word[target].size())
					avail[i] = false;

				written = "";
				for (int i = 0; i < (int) word[target].size(); i++)
					written += '*';
				
				int total = 0;
				for (int i = 0; i < (int) choice.size(); i++) if (to_try(choice[i]))
					total += eval(choice[i], target);

				if (total > points) {
					points = total;
					curr = target;
				}
			}

			ans.push_back(word[curr]);
		}

		printf("Case #%d: ", test);
		for (int i = 0; i < (int) ans.size(); i++) {
			if (i > 0)
				printf(" ");
			printf("%s", ans[i].c_str());
		}
		printf("\n");
	}

	return 0;
}
