#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

#define MAXN 1000

struct Line{
	int a, b;
}line[MAXN];
bool cmp(Line l1, Line l2){
	return l1.a < l2.a;
}

int main(){
	freopen("D:\\A-large.in", "r", stdin);
	freopen("D:\\out.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for(int case_t = 1; case_t <= cases; ++case_t){
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; ++i) scanf("%d%d", &line[i].a, &line[i].b);
		sort(line, line + n, cmp);
		int res = 0;
		for(int i = 0; i < n; ++i)
			for(int j = i + 1; j < n; ++j)
				if(line[i].b > line[j].b) ++res;
		printf("Case #%d: %d\n", case_t, res);
	}
	return 0;
}