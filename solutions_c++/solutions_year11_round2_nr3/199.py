#include <stdio.h>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>

int p[10];
int has[10][10];
int fil[10];

bool ok(const std::vector<std::vector<int> >& rooms, std::vector<int>& count, int max, int i = 0) {
	memset(has, 0, sizeof(has));
	memset(fil, 0, sizeof(fil));
	for (int j = 0; j <= i; ++j)
		for (int k=  0; k < rooms[j].size(); ++k) {
			has[rooms[j][k]][p[j]]++;
			fil[rooms[j][k]]++;
		}
	for (int j = 0; j < count.size(); ++j) if (count[j]) {
		if (count[j] - fil[j] < std::count(has[j], has[j] + max, 0))
			return false;
	}
	return true;
}

bool find(const std::vector<std::vector<int> >& rooms, std::vector<int>& count, int max, int i = 0) {
	if (i < rooms.size())
		for (int j = 0; j < max; ++j) {
			p[i] = j;
			if (ok(rooms, count, max, i))
				if (find(rooms, count, max, i+1)) 
					return true;
		}
	else {
		printf("%d\n", max);
		for (int i = 0; i < rooms.size(); ++i)
			printf("%d ", p[i]+1);
		printf("\n");
		return true;
	}
	return false;
}

void solve() {
	int n, m;
	scanf("%d%d", &n, &m);
	std::vector<int> start(n), stop(n), count(n);
	std::vector<std::vector<int> > rooms(n);
	std::vector<int> st;
	for (int i = 0; i < m; ++i) {
		int a;
		scanf("%d", &a);
		st.push_back(a);
	}
	for (int i = 0; i < m; ++i) {
		int a;
		scanf("%d", &a);
		start[std::min(a-1, st[i]-1)]++;
		stop[std::max(a-1, st[i]-1)]++;
	}
	std::stack<int> s;
	int cur = 0, last = 1;
	for (int i = 0; i <= n; ++i) {
		int j = i % n;
		if (i != 0) {
			count[cur]++;
			rooms[j].push_back(cur);
		}
		if (i != 0)
			for (int k = 0; k < stop[j]; ++k) {
				cur = s.top();
				s.pop();
				rooms[j].push_back(cur);
				count[cur]++;
			}
		if (i != n)
			for (int k = 0; k < start[j]; ++k) {
				s.push(cur);
				cur = last++;
				rooms[j].push_back(cur);
				count[cur]++;
			}
	}
	int max = *std::max_element(count.begin(), count.end());
	while (!find(rooms, count, max)) --max;
}

char s[1024];
int main(int argc, char* argv[]) {
    freopen(argv[1], "r", stdin);
    strcat(s, argv[1]);
    strcat(s, ".out");
    freopen(s, "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d: ", i+1);
		solve();
    }
}