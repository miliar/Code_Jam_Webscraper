#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cfloat>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <string>

using namespace std;

int tc = 1, resp, l, d, n, i, j, foi[32][32];
char dic[5555][32], c;

int main(void){
	scanf("%d%d%d", &l, &d, &n);
	for(i = 0; i < d; ++i)
		scanf(" %s", &dic[i]);
	while(n--) {
		for(i = 0; i < l; ++i) {
			for(j = 0; j <= 'z'-'a'; ++j)
				foi[i][j] = 0;
			scanf(" %c", &c);
			if (isalpha(c))
				foi[i][c-'a'] = 1;
			else {
				scanf(" %c", &c);
				while(c != ')') {
					foi[i][c-'a'] = 1;
					c = getchar();
				}
			}
		}
		for(resp = i = 0; i < d; ++i) {
			for(j = 0; j < l and foi[j][dic[i][j]-'a']; ++j);
			if (j == l)
				resp++;
		}
		printf("Case #%d: %d\n", tc++, resp);
	}
	return 0;
}
