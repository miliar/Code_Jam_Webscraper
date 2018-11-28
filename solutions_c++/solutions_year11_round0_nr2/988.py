#include <iostream>
#include <memory.h>
#include <map>
#include <string>
#include <cstdlib>
using namespace std;

typedef string answer_type;

answer_type solve()
{
	int C;
	cin >> C;
	char a, b, c;
	char comp[256][256];
	memset(comp, -1, sizeof(comp));
	for (int i = 0; i < C; i++)
	{
		cin >> a >> b >> c;
		comp[a][b] = comp[b][a] = c;
	}
	int D;
	cin >> D;
	bool bad[256][256];
	memset(bad, 0, sizeof(bad));
	for (int i = 0; i < D; i++)
	{
		cin >> a >> b;
		bad[a][b] = bad[b][a] = 1;
	}
	int N;
	cin >> N;
	char arr[200];
	int pt = 0;
	for (int i = 0; i < N; i++)
	{
		cin >> a;
		if (pt && comp[arr[pt - 1]][a] != -1)
		{
			arr[pt - 1] = comp[arr[pt - 1]][a];
			goto nexti;
		}
		for (int j = pt - 1; j >= 0; j--)
			if (bad[arr[j]][a])
			{
				pt = 0;
				goto nexti;
			}
		arr[pt++] = a;
	nexti:;
	}
	string ans = "[";
	if (pt == 0)
		ans += "]";
	else
	{
		for (int i = 0; i < pt; i++)
			ans += arr[i], ans += ", ";
		ans.resize(ans.size() - 1);
		ans[ans.size() - 1] = ']';
	}
	return ans;
}

int main()
{
	int T;
	cin >> T;
	answer_type ans;
	for (int i = 1; i <= T; i++)
		ans = solve(),
		cout << "Case #" << i << ": " << ans << endl,
		cerr << "Case #" << i << ": " << ans << endl;
}
