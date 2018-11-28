#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int T, H, W;

int a[100][100];
char s[100][100];

char o[300];

bool isSink(int i, int j)
{
	if (i && a[i - 1][j] < a[i][j]) return false;
	if (j && a[i][j - 1] < a[i][j]) return false;
	if (i + 1 < H && a[i + 1][j] < a[i][j]) return false;
	if (j + 1 < W && a[i][j + 1] < a[i][j]) return false;

	return true;
}

char test(int i, int j)
{
	if (s[i][j]) return s[i][j];

	int minh = a[i][j];

	if (i && a[i - 1][j] < minh) minh = a[i - 1][j];
	if (j && a[i][j - 1] < minh) minh = a[i][j - 1];
	if (i + 1 < H && a[i + 1][j] < minh) minh = a[i + 1][j];
	if (j + 1 < W && a[i][j + 1] < minh) minh = a[i][j + 1];

	if (minh == a[i][j])
	{
		puts("MJOOOOO!");
		return 1 / s[i][j];
	}

	if (i && a[i - 1][j] == minh) s[i][j] = test(i - 1, j);
	else
	if (j && a[i][j - 1] == minh) s[i][j] = test(i, j - 1);
	else
	if (j + 1 < W && a[i][j + 1] == minh) s[i][j] = test(i, j + 1);
	else
	if (i + 1 < H && a[i + 1][j] == minh) s[i][j] = test(i + 1, j);
	else
	{
		puts("MJOOOOO!");
		return 1 / s[i][j];
	}

	return s[i][j];
}

int main()
{
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d:\n", t);

		scanf("%d %d", &H, &W);

		for(int i = 0; i < H; i++)
		for(int j = 0; j < W; j++) scanf("%d", &a[i][j]);

		memset(s, 0, sizeof s);

		char ch = 'a';

		for(int i = 0; i < H; i++)
		for(int j = 0; j < W; j++) if (isSink(i, j)) s[i][j] = ch++;

		memset(o, 0, sizeof o);

		ch = 'a';
		
		for(int i = 0; i < H; i++)
		{
			for(int j = 0; j < W; j++)
			{
			    if (j) printf(" ");

			    char q = test(i, j);
			    if (o[q] == 0) o[q] = ch++;
				
				printf("%c", o[q]);
			}
			puts("");
		}
	}

	return 0;
}