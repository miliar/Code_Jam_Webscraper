#include <cstdio>
#include <cstring>

using namespace std;

bool zero;
char str[256];
long long ans = 0;
int M[256], cas, len, tot;

int main()
{
//	freopen("input.txt", "r", stdin);
// 	freopen("A-small-attempt0.in", "r", stdin);
// 	freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &cas);
	for(int c = 1; c <= cas; c ++) {
		scanf("%s", str);
		len = strlen(str);
		
		zero = false;
		for(int i = 0; i < 256; i ++)
			M[i] = -1;
		M[str[0]] = 1;
		tot = 2;
		for(int i = 1; i < len; i ++) {
			if(M[str[i]] == -1) {
				if(! zero) {
					M[str[i]] = 0;
					zero = true;
				}
				else {
					M[str[i]] = tot ++;
				}
			}
		}

		ans = 0;
		for(int i = 0; i < len; i ++) {
			ans = ans * tot + M[str[i]];
		}
		printf("Case #%d: %lld\n", c, ans);
	}

	return 0;
}