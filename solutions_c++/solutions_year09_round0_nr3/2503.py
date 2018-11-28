#include <iostream>
using namespace std;
char str[20] = "welcome to code jam";
char tmp[500];
int len;
FILE *fp = fopen("c:\\a.txt", "w");

int dfs(int p, int i)
{
	int k, j;
	int res = 0;
	for (k = p; k < len; k++) {
		if (i == 18) {
			res = 0;
			for (j = p; j < len; j++) {
				if (tmp[j] == str[i]) 
					res++;
				return res;
			}
		}
		if (tmp[k] == str[i]) {
			res += dfs(k + 1, i + 1);
		}
	}
	return res;
}

int main() 
{
	int m;
	int j;
	int ans;
	scanf("%d", &m);
	getchar();
	for (j = 1; j <= m; j++) {
		gets(tmp);
		len = strlen(tmp);
		ans = dfs(0, 0);
		fprintf(fp,"Case #%d: %05d\n", j, ans);
		//printf("Case #%d: %05d\n", j, ans);
	}
}