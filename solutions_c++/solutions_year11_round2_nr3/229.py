#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <assert.h>
#include <queue>
#include <deque>

using namespace std;
//static double a[100];
//s/tatic double b[100];
//static double c[100];
//static char d[100][100];
//static int cnt[100];

/*static void solve(int t)
{
	int n;
	memset(a, 0, sizeof(a));
	memset(b, 0, sizeof(b));
	memset(c, 0, sizeof(c));
	memset(d, 0, sizeof(d));
	memset(cnt, 0, sizeof(cnt));
	
	scanf("%d", &n);
	getchar();
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			char r  = getchar();
			d[i][j] = r;
			switch(r) {
			case '1':
				a[i] += 1; 
				break;
			case '0':
				break;
			case '.':
				cnt[i]--;
				break;
			}
		}
		getchar();
		cnt[i] += n;
		a[i] /= cnt[i];
		fprintf(stderr, "%lf\n", a[i]);
	}

	// compute b[i]
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) if (i != j && d[i][j] != '.') {
			double tmp = a[j] * cnt[j];
			fprintf(stderr, "tmp %d %d %lf %c %c\n", i, j, tmp, d[i][j], d[j][i]); 
			b[i] += (tmp - (d[j][i] == '1'? 1: 0)) / (cnt[j] - 1);
		}
		b[i] /= cnt[i];
		fprintf(stderr, "%lf\n", b[i]);
	}

	// compute c[i]
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) 
			if (i != j && d[i][j] != '.')
				c[i] += b[j];
		c[i] /= cnt[i];
	}
	printf("\n");
	for (int i = 0; i < n; i++) {
		printf("%.6lf\n", a[i] / 4 + b[i] / 2 + c[i] / 4);
	}
}*/

static bool judge(const set<vector<int> >& g, vector<int>& color, int n)
{
	int* cnt = new int[n];
	bool res = true;
	for (set<vector<int> >::iterator i = g.begin(); i != g.end(); ++i) {
		fill(cnt, cnt + n, 0);
		for (int j = 0; j < i->size(); j++) {
			cnt[color[i->at(j)]] = 1;
		}
		for (int j = 0; j < n; j++)
			if (cnt[j] == 0) {
				res = false;
				break;
			}
	}

	delete []cnt;
	return res;
}

static bool dfs(const set<vector<int> >& g, vector<int>& colors, int step, int count)
{
	if (step >= colors.size()) {
		if (judge(g, colors, count))
			return true;
		return false;
	}
	for (int i = 0; i < count; i++) {
		colors[step] = i;
		if (dfs(g, colors, step + 1, count))
			return true;
	}
	return false;
}


static void solve(int t)
{
	int n, m;
	set < vector<int> > groups;

	scanf("%d%d", &n, &m);
	vector<int> start(m);
	vector<int> end(m);
	for (int i = 0; i < m; i++) {
		scanf("%d", &start[i]);
		start[i] -= 1;
	}
	for (int i = 0; i < m; i++) {
		scanf("%d", &end[i]);
		end[i] -= 1;
	}

	// build group
	for (int i = 0; i < (1<<n); i++) {
		vector<int> tmp;
		for (int j = 0; j < n; j++) {
			if (((1 << j) & i) != 0)
				tmp.push_back(j);
		}
	//	tmp.push_back(0);
		//tmp.push_back(2);
		//tmp.push_back(3);
		//tmp.push_back(4);
		//tmp.push_back(5);
		//tmp.push_back(6);
		if (tmp.size() < 3) continue;
		bool found = true;
		for (int j = 0; j < tmp.size() - 1; j++) {
			bool flag = false;
			for (int l = 0; l < m; l++)
				if ((start[l] == tmp[j] && end[l] == tmp[j + 1])
					|| (end[l] == tmp[j] && start[l] == tmp[j + 1])
					|| (tmp[j] == tmp[j + 1] - 1)) {
					flag = true;
					break;
				}
			if (!flag) {
				found = false;
				break;
			}
			if (tmp.size() == 3) continue;
			int upper = j == 0? tmp.size() - 1: tmp.size();
			for (int k = j + 2; k < upper; k++) {
				for (int l = 0; l < m; l++)
					if ((start[l] == tmp[j] && end[l] == tmp[k])
						|| (start[l] == tmp[k] && end[l] == tmp[j]))
						found = false;
			}

		}
		bool flag = false;
		for (int l = 0; l < m; l++)
			if ((start[l] == tmp[0] && end[l] == tmp[tmp.size() - 1])
				|| (end[l] == tmp[0] && start[l] == tmp[tmp.size() - 1])
				|| tmp[tmp.size() - 1] == n - 1 && tmp[0] == 0) {
				flag = true;
				break;
			}
		if (!flag) {
			found = false;
		}
		if (found) groups.insert(tmp);
	}

	vector<int> colors(n);
	for (int c = n - 1; c >= 1; c--) {
		bool res = dfs(groups, colors, 0, c);
		if (res) {
			printf("%d\n", c);
			break;
		}
	}
	for (int i = 0; i < n; i++) {
		if (i > 0) printf(" ");
		printf("%d", colors[i] + 1);
	}
}

int main()
{
  int T;
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  freopen("err.out", "w", stderr);
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    printf("Case #%d: ", i + 1);
    solve(i + 1);
    printf("\n", i + 1);
  }
  return 0;
}