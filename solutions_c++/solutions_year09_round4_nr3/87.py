#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

struct stock
{
	vector<int> elem;

	bool operator < (const stock &a) const
	{
		for (int i = 0; i < elem.size(); ++i)
		{
			if (elem[i] < a.elem[i]) return true;
			if (elem[i] > a.elem[i]) return false;
		}
		return false;
	}
};

const int MAXN = 105;
const int MAXM = 105;

int N, M;
vector<int> graph[MAXN];
int match1[MAXN];
int match2[MAXM];
char check[MAXM];

bool extendMatch(int a) {
	for (int i = 0 ; i < graph[a].size() ; i++) {
		int b = graph[a][i];
		if (check[b]) continue;
		if (match2[b] == -1) {
			match1[a] = b;
			match2[b] = a;
			return true;
		}
	}
	for (int i = 0 ; i < graph[a].size() ; i++) {
		int b = graph[a][i];
		if (check[b]) continue;
		check[b] = 1;
		if (extendMatch(match2[b])) {
			match1[a] = b;
			match2[b] = a;
			return true;
		}
	}
	return false;
}

int maxMatch() {
	memset(match1, -1, N * sizeof(int));
	memset(match2, -1, M * sizeof(int));
	int cnt = 0;
	for (int i = 0 ; i < N ; i++) {
		memset(check, 0, M);
		if (extendMatch(i))
			cnt++;
	}
	return cnt;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn)
	{
		printf("Case #%d: ", cn);
		int n, m;
		scanf("%d %d", &n, &m);

		vector<stock> a;

		for (int i = 0; i < n; ++i)
		{
			stock tmp;
			tmp.elem.resize(m);
			for (int j = 0; j < m; ++j)
			{
				scanf("%d", &tmp.elem[j]);
			}
			a.push_back(tmp);
			graph[i].clear();
		}

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
			{
				bool isok = true;
				for (int k = 0; k < m; ++k)
					if (a[i].elem[k] >= a[j].elem[k]) isok = false;
				if (isok) graph[i].push_back(j);
			}

		N = n, M = n;
		printf("%d\n", N - maxMatch());
	}
}

