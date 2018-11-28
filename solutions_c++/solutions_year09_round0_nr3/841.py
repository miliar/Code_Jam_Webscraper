#include <iostream>
#include <vector>

using namespace std;

//int a[200][200];
//char ans[200][200];

void solve(int test) {
	/*int w,h;
	scanf("%d%d", &h,&w);
	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j) {
			scanf("%d", &a[i][j]);
		}
	}*/
	char wel[] = "welcome to code jam";
	int n = strlen(wel);
	int str[30][1000];
	char a[1000];
	memset(str, 0, sizeof(str));
	cin.getline(a, 1000);
	int m = strlen(a);
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= m; ++j) {
			if (wel[i - 1] == a[j - 1])
				str[i][j] = (str[i][j-1]+str[i-1][j]+(i==1?1:0))%10000;
			else
				str[i][j] = str[i][j-1]%10000;
		}
	}
	printf("Case #%d: %04d\n", test, str[n][m]);
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int n;
	scanf("%d", &n);
	
	char str[10];
	cin.getline(str, 10);

	for (int i = 0; i < n; ++i) {
		solve(i + 1);
	}

	return 0;
}

