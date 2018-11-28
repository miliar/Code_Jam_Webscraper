#include <iostream>
#include <vector>

using namespace std;

int ts;
int H, W;
int a[100][100];

int w[100][100];
int wc;

int di[] = {-1, 0, 0, 1};
int dj[] = {0, -1, 1, 0};

bool ok(int i, int j) { return i >= 0 && i < H && j >= 0 && j < W; }

int dfs(int i, int j)
{
	if (w[i][j] != -1) return w[i][j];
	int m = a[i][j];
	for (int k = 0; k < 4; k++)
	{
		int ii = i + di[k];
		int jj = j + dj[k];
		if (ok(ii,jj) && a[ii][jj] < m) m = a[ii][jj];
	}
	if (m == a[i][j]) w[i][j] = wc++;
	else
	{
		for (int k = 0; k < 4; k++)
		{
			int ii = i + di[k];
			int jj = j + dj[k];
			if (ok(ii,jj) && a[ii][jj] == m) {
				w[i][j] = dfs(ii,jj);
				break;
			}
		}		
	}
	return w[i][j];
}

void solve()
{
	wc = 0;
	memset(w, -1, sizeof w);
	cin >> H >> W;
	for (int i = 0; i < H; i++) for (int j = 0; j < W; j++) cin >> a[i][j];
	
	cout << "Case #" << ++ts << ":" << endl;
	
	for (int i = 0; i < H; i++) for (int j = 0; j < W; j++) if (w[i][j] == -1) dfs(i, j);
	vector<char> ch(26, -1);
	char cur = 'a';
	
	for (int i = 0; i < H; i++)
	{
		for (int j = 0; j < W; j++)
		{
			if (ch[w[i][j]] == -1)
			{
				ch[w[i][j]] = cur++;
			}
			putc((char)ch[w[i][j]], stdout);
			//cout << w[i][j];
			if (j != W - 1) cout << ' '; else cout << endl;
		}
	}
	
}

int main()
{
	int t; cin >> t;
	for (int i = 0; i < t; i++) solve();
	return 0;
}