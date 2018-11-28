#include <cstdio>
#include <cstdlib>
#include <climits>

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <map>

using namespace std;

struct Group {
	vector<string> words;
	int score, pos;
	
	Group(vector<string> &w, int s, int p) {
		words = w;
		score = s;
		pos = p;
	}
	
	Group() {
		
	}
};

int n, m;
vector<string> words;
string seq;

queue<Group> groups;

int best = -1;
string best_word;

map<string, int> pos_in_input;

void solve() {
	best = -1;

	{
		vector<string> ngroups[10];
		for (vector<string>::iterator i = words.begin(); i != words.end(); i++) {
			ngroups[(int)i->size() - 1].push_back(*i);
		}
		
		for (int i = 0; i < 10; i++) {
			if (ngroups[i].size() > 0) {
				groups.push(Group(ngroups[i], 0, 0));
			}
		}
	}
	
	while (!groups.empty()) {
		Group &group = groups.front();
		
		if (group.words.size() == 1) {
			if (group.score > best) {
				best = group.score;
				best_word = group.words[0];
			} else if (group.score == best && pos_in_input[group.words[0]] < pos_in_input[best_word]) {
				best_word = group.words[0];
			}
			groups.pop();
			continue;
		}
		
		vector<string> ngroups[1024];
		
		for (vector<string>::iterator i = group.words.begin(); i != group.words.end(); i++) {
			int mask = 0;
			for (int j = 0; j < i->size(); j++) {
				mask <<= 1;
				if ((*i)[j] == seq[group.pos]) mask |= 1;
			}
			ngroups[mask].push_back(*i);
		}
		
		bool not_alone = false;
		for (int i = 1; i < 1024; i++) {
			if (ngroups[i].size() > 0) {
				not_alone = true;
				break;
			}
		}
		
		for (int i = 0; i < 1024; i++) {
			if (ngroups[i].size() > 0) {
				groups.push(Group(ngroups[i], group.score + (i == 0 && not_alone), group.pos + 1));
			}
		}
		
		groups.pop();
	}
	
	if (best == -1) fprintf(stderr, "warning!!!\n");
	
	cout << best_word;
}

void task() {
	cin >> n >> m;
	
	words.clear();
	pos_in_input.clear();
	for (int i = 0; i < n; i++) {
		string a;
		cin >> a;
		words.push_back(a);
		pos_in_input[a] = i;
	}
	
	for (int i = 0; i < m; i++) {
		cin >> seq;
		
		solve();
		
		if (i != m - 1)
			printf(" ");
		else
			printf("\n");
	}
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		printf("Case #%d: ", i);
		task();
	}
}

