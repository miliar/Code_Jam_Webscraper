#include<cstdio>
#include<cstring>
#include<map>

using namespace std;

int main(){
	int T, ca=0;
	scanf("%d", &T);
	while (T--){
		printf("Case #%d: ", ++ca);
		map<int, int> G;
		int N;
		scanf("%d", &N);
		for (int i = 0 ; i < N; ++i){
			int x, y;
			scanf("%d%d", &x, &y);
			G[x] += y;
		}
		long long res= 0;
		while (1){
			int ok = 1;
			for (map<int, int>::iterator i = G.begin(); ok && i != G.end(); i++)
				if (i->second > 1){
					int x = i->first;
					i->second -= 2;
					res++;
					G[x-1]++, G[x+1]++;
					ok = 0;
				}
			if (ok) break;
		}
		printf("%lld\n", res);
	}
	return 0;
}
