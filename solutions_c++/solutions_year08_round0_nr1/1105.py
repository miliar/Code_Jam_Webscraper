#include <cstdio>
#include <string.h>

char a[110][110], b[1010][110];
bool check(int x, int y){
	bool flag = true;
	int len1 = strlen(b[x]);
	int len2 = strlen(a[y]);
	if (len1 != len2) flag = false;
	else{
		for (int i=0; i<len1; i++)
			if (a[y][i] != b[x][i]){
				flag = false;
				break;
			}
	}
	//printf("%d %d %s %s %d\n", len1, len2, a[y], b[x], flag);
	return flag;
}

int main(){
	int T, ca = 0;
	bool vis[110];
	scanf("%d", &T);
	while (T--){
		char ts[10];
		int s, q;
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		scanf("%d", &s);gets(ts);
		for (int i=0; i<s; i++)
			gets(a[i]);
		scanf("%d", &q);gets(ts);
		for (int i=0; i<q; i++)
			gets(b[i]);
		
		int c = 0, ans = 0, k;
		memset(vis, 0, sizeof(vis));
		for (int i=0; i<q; i++){
			for (int j=0; j<s; j++)
				if (!vis[j] && check(i, j)){
					vis[j] = true;
					k = j;
					c++;
					break;
				}
			if (c == s) {
				ans++;
				c = 1;
				memset(vis, 0, sizeof(vis));
				vis[k] = true;
			}
		}
		printf("Case #%d: %d\n", ++ca, ans);
	}
	return 0;
}
