#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
	freopen("message.in", "r", stdin);
	int t;
	scanf("%d\n", &t);
	for (int casenr = 1; casenr <= t; casenr++){
		int p, k, l;
		scanf("%d %d %d\n", &p, &k, &l);
		int freq[1001] = {0};
		for (int i = 0; i < l; i++)
			scanf("%d", &freq[i]);
		sort(freq, freq+l);
		int tc = 0;
		int mult = 0;
		int count = 0;
		for (int i = l-1; i >= 0; i--){
			if (tc == 0) mult++;	
			count += freq[i]*mult;
			tc = (tc+1)%k;
		}
		printf("Case #%d: %d\n", casenr, count);
	}
}
