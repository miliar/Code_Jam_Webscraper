#include <cstdio>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

int main(){
	int T, ca = 0;
	scanf("%d", &T);
	while (T--){
		int x, ox;
		scanf("%d", &x);
		ox = x;
		int ac = 0;
		int a[30]; memset(a, 0, sizeof(a));
		vector<int> v; v.clear();
		while (x>0){
			a[ac++] = x % 10;
			x /= 10;
		}
		for (int i=ac-1; i>=0; i--) v.push_back(a[i]);

		int ans;
		next_permutation(v.begin(), v.end());
		ans = 0;
		for (int i=0; i<ac; i++)
			ans = ans * 10 + v[i];
		//printf("~~ %d\n", ans);
		if (ans <= ox){
			for (int i=0; i<ac; i++)
				if (v[i] != 0){
					int t = v[0];
					v[0] = v[i];
					v[i] = t;
					break;
				}
			v.insert(v.begin()+1, 1, 0);
			ac++;
			/*
			printf("------\n");
			for (int i=0; i<ac; i++)
				printf("%d ", v[i]);
			printf("\n");
*/
			ans = 0;
			for (int i=0; i<ac; i++)
				ans = ans * 10 + v[i];
		}

		printf("Case #%d: %d\n", ++ca, ans);
	}
	return 0;
}
