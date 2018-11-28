#include <stdio.h>
#include <algorithm>

using namespace std;

int n,s,p;
int sc[110];

int main() {

	int T;
	scanf("%d",&T);

	for (int z = 0;z < T;z++) {
		scanf("%d%d%d",&n,&s,&p);
		for (int i = 0;i < n;i++) scanf("%d",&sc[i]);
		int ans = 0,a1 = 0,a2 = 0;
		for (int i = 0;i < n;i++) {
			if (sc[i] >= p * 3 - 2 && sc[i] >= p) a1++;
			else if (sc[i] >= p * 3 - 4 && sc[i] >= p) a2++;
		}
		ans = a1 + min(a2,s);
		printf("Case #%d: %d\n",z+1,ans);
		//printf("!!%d %d %d %d\n",p,s,a1,a2);
	}

	return 0;
}
