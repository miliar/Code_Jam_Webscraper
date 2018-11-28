#include <stdio.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>

using namespace std;

int d[10010], l[10010], p[10010];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	while(T--> 0){
		int n;
		scanf("%d",&n);
		int i, j;
		for(i=0;i<n;i++){
			scanf("%d %d",&d[i], &l[i]);
			p[i] = 0;
		}
		int D;
		scanf("%d",&D);
		p[0] = d[0];

		for(i=0, j=0;i<n;i++){
			if (d[i] + p[i] >= D) break;
			for(j=max(j, i+1);j<n;j++){
				if (d[j] > d[i] + p[i]) break;
				p[j] = max(p[j], min(l[j], d[j] - d[i]));
			}
		}

		static int cs = 1;
		printf("Case #%d: %s\n", cs++, (i<n)?"YES":"NO");
	}
	return 0;
}