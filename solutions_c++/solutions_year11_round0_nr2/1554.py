#include <cstdio>
#include <vector>
using namespace std;
vector<char> op[26];
char invoke[26][26];
int cnt[26];
vector<char> stack;
void add(char x)
{
	stack.push_back(x);
	++cnt[x];
	while(stack.size() > 1)
	{
		char a = stack[stack.size() - 1];
		char b = stack[stack.size() - 2];
		if (invoke[a][b] == -1) break;
		--cnt[a];
		--cnt[b];
		++cnt[invoke[a][b]];
		stack.pop_back();
		stack.pop_back();
		stack.push_back(invoke[a][b]);
	}
	char c = stack[stack.size() - 1];
	for (int i = 0; i < op[c].size(); ++i)
	{
		if (cnt[op[c][i]] != 0)
		{
			stack.clear();
			for (int i = 0; i < 26; ++i)
			{
				cnt[i] = 0;
			}
			return;
		}
	}
}
void solve()
{
	stack.clear();
	for (int i = 0; i < 26; ++i)
	{
		op[i].clear();
		cnt[i] = 0;
		for (int j = 0; j < 26; ++j)
		{
			invoke[i][j] = -1;
		}
	}
	int C, D, N;
	char buff[110];
	scanf ("%d", &C);
	for (int i = 0; i < C; ++i)
	{
		scanf("%s", buff);
		for (int j = 0; j < 3; ++j) buff[j] -= 'A';
		invoke[buff[0]][buff[1]] = buff[2];
		invoke[buff[1]][buff[0]] = buff[2];
	}
	scanf ("%d", &D);
	for (int i = 0; i < D; ++i)
	{
		scanf("%s", buff);
		for (int j = 0; j < 2; ++j) buff[j] -= 'A';
		op[buff[0]].push_back(buff[1]);
		op[buff[1]].push_back(buff[0]);
	}
	scanf ("%d %s", &N, buff);
	for(int i = 0; i < N; ++i)
	{
		add(buff[i] - 'A');
	}
	printf ("[");
	if (stack.size() > 0)
		printf ("%c", stack[0] + 'A');
	for (int i = 1; i < stack.size(); ++i)
	{
		printf (", %c", stack[i] + 'A');
	}
	printf ("]\n");
}
int main()
{
	freopen ("test.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf ("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}