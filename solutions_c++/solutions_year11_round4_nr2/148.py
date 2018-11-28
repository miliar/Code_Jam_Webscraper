#include<iostream>
using namespace std;

const int maxl = 500 + 10;

int b[maxl][maxl][3], a[maxl][maxl];
int h, w, d, ans;

void init() 
{
	scanf("%d %d %d\n", &h, &w, &d);
	char ch;
	for (int i = 1; i <= h; i++) {
		for (int j = 1; j <= w; j++) {
			scanf("%c", &ch);
			a[i][j] = ch - '0';
		}		
		scanf("\n");		
	}	
}

void count1()
{
	for (int i = 1; i <= h; i++) {		
		for (int j = 1; j <= w; j++) {
			b[i][j][0] = b[i][j - 1][0] + b[i - 1][j][0] - b[i - 1][j - 1][0] + a[i][j] * i;
			b[i][j][1] = b[i][j - 1][1] + b[i - 1][j][1] - b[i - 1][j - 1][1] + a[i][j] * j;
			b[i][j][2] = b[i][j - 1][2] + b[i - 1][j][2] - b[i - 1][j - 1][2] + a[i][j];
		}
	}
	
	for (int i = 2; i <= h - 1; i++)
		for (int j = 2; j <= w - 1; j++) {
			double s1, s0;
			s1 = s0 = 0;						
			for (int k = 1; ; k++) {
				if (i - k < 1 || i + k > h || j - k < 1 || j + k > w) break;
				s0 = b[i + k][j + k][0] - b[i - k - 1][j + k][0] - b[i + k][j - k - 1][0] + b[i - k - 1][j - k - 1][0];
				s1 = b[i + k][j + k][1] - b[i - k - 1][j + k][1] - b[i + k][j - k - 1][1] + b[i - k - 1][j - k - 1][1];
				s0 -= i * (b[i + k][j + k][2] - b[i - k - 1][j + k][2] - b[i + k][j - k - 1][2] + b[i - k - 1][j - k - 1][2]);
				s1 -= j * (b[i + k][j + k][2] - b[i - k - 1][j + k][2] - b[i + k][j - k - 1][2] + b[i - k - 1][j - k - 1][2]);
				s0 -= (a[i + k][j + k] + a[i + k][j - k] - a[i - k][j + k] - a[i - k][j - k]) * k;
				s1 -= (a[i + k][j + k] - a[i + k][j - k] + a[i - k][j + k] - a[i - k][j - k]) * k;
				if (s0 == 0 && s1 == 0) ans = max(ans, k * 2 + 1);
			}
		}
	for (int i = 1; i <= h; i++)
		for (int j = 1; j <= w; j++) {
			double s1, s0;
			s1 = s0 = 0;						
			for (int k = 2; ; k++) {
				if (i - k +  1 < 1 || i + k > h || j - k  + 1 < 1 || j + k > w) break;
				int mx = i - k + 1, my = j - k + 1, nx = i + k, ny = j + k;
				s0 = b[nx][ny][0] - b[mx - 1][ny][0] - b[nx][my - 1][0] + b[mx - 1][my - 1][0];
				s1 = b[nx][ny][1] - b[mx - 1][ny][1] - b[nx][my - 1][1] + b[mx - 1][my - 1][1];
				s0 -= (i + 0.5) * (b[nx][ny][2] - b[mx - 1][ny][2] - b[nx][my - 1][2] + b[mx - 1][my - 1][2]);
				s1 -= (j + 0.5) * (b[nx][ny][2] - b[mx - 1][ny][2] - b[nx][my - 1][2] + b[mx - 1][my - 1][2]);
				s0 -= (a[nx][ny] + a[nx][my] - a[mx][ny] - a[mx][my]) * (k - 0.5);
				s1 -= (a[nx][ny] - a[nx][my] + a[mx][ny] - a[mx][my]) * (k - 0.5);
				if (s0 == 0 && s1 == 0) ans = max(ans, k * 2);
			}
		}
}

void solve()
{
	ans = 0;
	count1();	
	if (ans == 0)
		printf("IMPOSSIBLE\n");
	else printf("%d\n", ans);
}
	
int main()
{
	int t, T;
	for (scanf("%d", &T), t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		init();
		solve();
	}
}
