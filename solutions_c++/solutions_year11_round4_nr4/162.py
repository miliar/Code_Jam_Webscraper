#include <cstdio>
#include <cstring>
#include <queue>
#include <list>

using namespace std;

int p, ans1, ans2;
int level[402];
int marked[402];

list<int> ls[402];

void DFS(int n) {
	list<int>::iterator it;
	int count;

	if (n == 0) {
		count = 0;
		for (int i = 0; i < p; i++)
			if (marked[i] == 1)
				for (it = ls[i].begin(); it != ls[i].end(); it++)
					if (marked[*it] == 0) {
						marked[*it] = 2;
						count++;
					}
		if (ans2 < count)
			ans2 = count;
		for (int i = 0; i < p; i++)
			if (marked[i] == 2)
				marked[i] = 0;
		return;
	}

	for (it = ls[n].begin(); it != ls[n].end(); it++)
		if (level[*it] + 1 == level[n]) {
			marked[*it] = 1;
			DFS(*it);
			marked[*it] = 0;
		}
}

void BFS() {
	list<int>::iterator it;
	int node;
	queue<int> q;

	memset(marked, 0, sizeof marked);
	memset(level, 0xff, sizeof level);
	level[0] = 0;
	q.push(0);

	while (!q.empty()) {
		node = q.front();
		q.pop();

		for (it = ls[node].begin(); it != ls[node].end(); it++)
			if (level[*it] == -1) {
				level[*it] = level[node] + 1;
				q.push(*it);
			}
	}

	ans2 = 0;
	ans1 = level[1] - 1;
	DFS(1);
}

int main() {
	int case_no, w, x, y, t;

	scanf("%d", &t);
	for (case_no = 1; case_no <= t; case_no++) {
		scanf("%d%d", &p, &w);

		for (int i = 0; i < p; i++)
			ls[i].clear();
	
		for (int i = 0; i < w; i++) {
			scanf("%d", &x);
			getchar();
			scanf("%d", &y);

			ls[x].push_back(y);
			ls[y].push_back(x);
		}

		BFS();

		fprintf(stderr, "Running: %d\n", case_no);
		printf("Case #%d: %d %d\n", case_no, ans1, ans2);
	}

	return 0;
}
