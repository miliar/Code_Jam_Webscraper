#include <cstdio>
#include <cstring>
#include <set>
#include <algorithm>

using namespace std;

set <pair<int, int> > S;

int main(){
	int ans, n, a, b, tmp, len;
	char s[20];
	
	scanf("%d", &n);
	for (int t = 1; t <= n; t++){
		scanf("%d%d", &a, &b);
		ans = 0;
		S.clear();
		
		for (int i = a; i <= b; i++){
			sprintf(s, "%d", i);
			
			len = strlen(s);
			
			for (int j = 1; j < len; j++){
				tmp = 0;
				for (int q = 0; q < len; q++)
					tmp = tmp * 10 + (s[(j + q) % len] - '0');
				
				if (i < tmp && tmp <= b && !S.count(make_pair(i, tmp)))
					ans++, S.insert(make_pair(i, tmp));
			}
		}
		
		printf("Case #%d: %d\n", t, ans);
	}
}
