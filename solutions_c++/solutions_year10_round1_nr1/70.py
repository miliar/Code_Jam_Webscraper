#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;
int n,k;
vector<int> p;
const int dx[8]={-1,-1,-1,0,1,1,1,0};
const int dy[8]={-1,0,1,1,1,0,-1,-1};
char s[60][60], ss[60][60];

void turn()
{
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			ss[j][n - 1 - i] = s[i][j];
	for (int j = 0; j < n; ++j)
	{
		p.clear();
		for (int i = n - 1; i >= 0; --i)
			if (ss[i][j] != '.') p.push_back(i);
		for (int i = 0; i < p.size(); ++i)
			s[n - 1 - i][j] = ss[p[i]][j];
		for (int i = n - 1 - p.size(); i >= 0; --i) s[i][j] = '.';
	}
}

bool check(char c)
{
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			if (s[i][j] == c)
				for (int d = 0; d < 8; ++d)
				{
					int cnt = 1;
					int x,y;
					x = i + dx[d]; y = j + dy[d];
					while (x < n && x >= 0 && y < n && y >= 0)
					{
						if (s[x][y] != c) break;
						++cnt;
						x += dx[d]; y += dy[d];
					}
					if (cnt >= k) return true;
				}

	return false;
}

int main()
{
	freopen("A-large.in","r", stdin);
	freopen("output.txt","w", stdout);
	int cases;
	scanf("%d", &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		scanf("%d%d" , &n, &k);
		for (int i = 0; i < n; ++i) scanf("%s" ,s[i]);
		turn();
		bool ok1 = check('B');
		bool ok2 = check('R');
		printf("Case #%d: ", ca);
		if (ok1 && ok2) puts("Both"); else if (ok1) puts("Blue"); else if (ok2) puts("Red"); else puts("Neither");
	}
	fclose(stdin);
	fclose(stdout);
}
