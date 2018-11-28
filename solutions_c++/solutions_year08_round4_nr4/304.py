#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>

#define INF 0x3f3f3f3f

using namespace std;

vector<int> v;

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i, k, len, T, test, cans, ans;
	char str[20000], u[20000];
	
	scanf("%d\n", &T);
	
	for (test=1; test<=T; test++) {
		scanf("%d\n", &k);
		gets(str);
		
		len = strlen(str);
		
		ans = INF;
		
		v.clear();
		
		for (i=0; i<k; i++) v.push_back(i);

		do {
			cans = 1;
			
			for (i=0; i<len; i++) {
				u[i] = str[(i/k)*k + v[i%k]];
				//printf("%d -> %d %d\n", i, (i/k)*k, i%k);
				
				if ( i != 0 && u[i] != u[i-1] ) cans++;
			}
			
			if ( cans < ans ) ans = cans;
		} while( next_permutation(v.begin(), v.end()) );
		
		printf("Case #%d: %d\n", test, ans);
	}
	
	return 0;
}
