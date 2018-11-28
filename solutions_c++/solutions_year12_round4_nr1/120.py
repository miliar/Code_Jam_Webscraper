#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
using namespace std;
int H[10005], D[10005];
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int N;
		scanf("%d",&N);
		bool can = 0;
		for(int i=0;i<N;++i) {
			int l;
			scanf("%d%d",&D[i],&l);
			H[i] = 0;
			if(!i) H[i] = D[i];
			for(int j=0;j<i;++j)
				if(D[i] <= D[j]+H[j]) {
					H[i] = D[i]-D[j];
					break;
				}
			if(H[i] > l) H[i] = l;
		}
		int K;
		scanf("%d",&K);
		for(int i=0;i<N;++i)
			if(D[i]+H[i] >= K) can = 1;
		printf("Case #%d: ",cn);
		if(can) printf("YES\n");
		else printf("NO\n");
	}
}
