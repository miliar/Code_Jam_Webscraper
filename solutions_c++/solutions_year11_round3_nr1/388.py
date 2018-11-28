#include<cstdio>
using namespace std;

char s[100][100];

bool work(int n, int m)
{
	for(int i = 1; i <= n; i++)
		scanf("%s", s[i] + 1);
	while(true) {
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
				if(s[i][j] == '#' && s[i - 1][j] != '#' && s[i][j - 1] != '#') {
					if(s[i + 1][j] == '#' && s[i][j + 1] == '#' && s[i + 1][j + 1] == '#') {
						s[i][j] = '/';
						s[i + 1][j] = '\\';
						s[i][j + 1] = '\\';
						s[i + 1][j + 1] = '/';
					} else
						return false;
				}
		bool flag = false;
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
				if(s[i][j] == '#')
					flag = true;
		if(!flag)
			break;
	}
	return true;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("Alarge.out", "w", stdout);
	for(int i = 0; i < 100; i++)
		for(int j = 0; j < 100; j++)
			s[i][j] = '.';
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++) {
		int n, m;
		scanf("%d%d", &n, &m);
		printf("Case #%d:\n", i);
		if(!work(n, m)) {
			puts("Impossible");
		}else{
			for(int i=1;i<=n;i++)
				puts(s[i]+1);
		}
	}
}
