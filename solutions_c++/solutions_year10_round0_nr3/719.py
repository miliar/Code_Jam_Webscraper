#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int r, k, n, a[1010];
typedef long long ll;
int ile[1010], pos[1010];

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int iii=1; iii<=cases; ++iii){
		printf("Case #%d: ", iii);
		scanf("%d%d%d", &r, &k, &n);
		for(int i=0; i<n; ++i) scanf("%d", &a[i]);
		ll s = 0;
		for(int i=0; i<n; ++i) s += a[i];
		if((ll)k >= s){ printf("%lld\n", s*r); continue; }
		for(int i=0; i<n; ++i){
			ile[i] = 0;
			for(int j=i; true; j = (j+1)%n){
				if(ile[i] + a[j] > k){
					pos[i] = j;
					break;
				}
				ile[i] += a[j];
			}
		}
		int p = 0;
		ll res = 0;
		while(r--){
			res += ile[p];
			p = pos[p];
		}
		printf("%lld\n", res);
	}
	return 0;
}
