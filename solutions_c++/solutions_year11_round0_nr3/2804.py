#include<cstdio>
#include<cstring>
int tc, n, ar[105];
int max(int a, int b) {
	if (a>b) return a; return b;
}

int main(){ 
	scanf("%d",&tc);
	for (int ti = 1; ti <= tc; ti++) {
		scanf("%d",&n);
		memset(ar,0,sizeof(ar));
		for (int i = 0; i < n; i++) {
			scanf("%d",&ar[i]);
		}
		int maxRes = -1;

		for (int i = 0; i < (1<<n); i++) {
			int first = -1; int second = -1;
			int jumlFirst = 0; int jumlSecond = 0;
			for (int j =0; j < n; j++) {
				if ((i&(1<<j)) != 0) {
					if (first == -1) first = ar[j];
					else first ^= ar[j];
					jumlFirst += ar[j];
				} else {
					if (second == -1) second = ar[j];
					else second ^= ar[j];
					jumlSecond += ar[j];
				}
			}
			
			if (first == second) maxRes = max(maxRes, max(jumlFirst,jumlSecond));
		}
		if (maxRes == -1) printf("Case #%d: NO\n",ti);
		else printf("Case #%d: %d\n",ti,maxRes);
	}
}