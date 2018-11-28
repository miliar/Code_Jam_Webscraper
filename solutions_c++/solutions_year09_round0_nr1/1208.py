#include <iostream>

using namespace std;

int br[5000*16][26];
int nb = 0;
int l, d, n;

void Load()
{
	cin >> l >> d >> n;
	int i;
	char c;
	int cur;
	for (i = 0; i < d; i++) {
		c = getchar();
		while (c < 'a' || c > 'z') c = getchar();
		cur = 0;
		while (c >= 'a' && c <= 'z') {
			c -= 'a';
		    if (br[cur][c] == 0) {
		    	nb++;
		    	br[cur][c] = nb;
		    }
		    cur = br[cur][c];
			c = getchar();
		}
	}
}


int wrd[16][26];

int dp[16][5000*16];


void Solve()
{
	memset(wrd, 0, sizeof(wrd));
	char c;
	c = getchar();
	while ((c < 'a' || c > 'z') && c != '(' && c != ')') c = getchar();
	int i = 1;
	int j, k;
	while (c != ' ' && c != '\n' && c > 0) {
		if (c == '(') {
			c = getchar();
			while (c != ')') {
				wrd[i][c - 'a'] = 1;
				c = getchar();
			}
		} else wrd[i][c - 'a'] = 1;
		i++;
		c = getchar();
	}
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
	for (i = 0; i < l; i++) {
		for (j = 0; j <= nb; j++) {
			if (dp[i][j] == 0) continue;
			for (c = 0; c < 26; c++)	{
				if (br[j][c] != 0 && wrd[i+ 1][c] == 1) {
					dp[i + 1][br[j][c]] = 1;
				}
			}
		}
	}
	int res = 0;
	for (i = 0; i <= nb; i++) {
		res += dp[l][i];	
	}
	cout << res << "\n";
}



int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	Load();
	for (int ii = 1; ii <= n; ii++) {
		cout << "Case #" << ii << ": ";
		Solve();
	}	
	return 0;
}