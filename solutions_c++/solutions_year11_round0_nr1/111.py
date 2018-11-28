#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;

char s[4];

int main(){
	int i, j, k, m, n, cas, y[110];
	char x[110];
	freopen("A-large (1).in", "r", stdin);
	freopen("w.txt", "w", stdout);
	scanf("%d", &cas);
	for(int ri = 1; ri <= cas; ri++){
		printf("Case #%d: ", ri);
		scanf("%d", &n);
		int O = 1, B = 1, to = 0, tb = 0;
		for(i = 0; i < n; i++){
			scanf("%s%d", &s, &k);
			if(s[0] == 'O'){
				to += abs(k - O) + 1;
				O = k;
				if(to <= tb) to = tb + 1;
			}else{
				tb += abs(k - B) + 1;
				B = k;
				if(tb <= to) tb = to + 1;
			}
		}
		printf("%d\n", max(tb, to));
	}
}
