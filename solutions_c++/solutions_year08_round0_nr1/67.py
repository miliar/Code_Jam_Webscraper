#include <cstdio>
#include <cstdlib>
#include <string>
 
using namespace std;

int t, s, q, base, ans;
char name[100][110], query[1000][110];
int len;

int main()
{
	int i, j, k;
	
	freopen("A.output", "w", stdout);
	
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%d", &s);
		getchar();
		for (j = 0; j < s; j++)
			gets(name[j]);
		scanf("%d", &q);
		getchar();
		for (j = 0; j < q; j++)
			gets(query[j]);
		ans = -1;
		base = 0;
		while (base < q) {
			len = 0;
			for (j = 0; j < s; j++) {
				for (k = 0; base + k < q; k++)
					if (strcmp(name[j], query[base + k]) == 0)
						break;
				if (k > len)
					len = k;
			}
			base += len;
			ans++;
		}
		
		printf("Case #%d: %d\n", i + 1, ans < 0 ? 0 : ans);
	}
	
	return (0);
}

