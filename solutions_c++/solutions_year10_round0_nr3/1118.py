#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <queue>

using namespace std;

bool flag[11111];

struct Node{
	int value, id;
};
queue <Node>  que;

int main()
{
	freopen("C-small-attempt0.in", "r",  stdin);
	freopen("small.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int kk=1; kk<=T;kk++){
		int r, k, n;
		while(!que.empty()) que.pop();
		scanf("%d%d%d", &r, &k, &n);
		Node t;
		memset(flag, 0, sizeof(flag));
		for(int i=0; i<n; i++){
			scanf("%d", &t.value);
			t.id = i;
			que.push(t);
		}
		int ans = 0;
		for(int i=0; i<r; i++){	
			memset(flag, 0, sizeof(flag));
			int tmp = 0;
			Node fr;
			while(tmp + que.front().value<= k){
				fr = que.front();
				if(flag[fr.id]) break;
				flag[fr.id] = true;
				tmp += fr.value;
				que.pop();
				que.push(fr);
			}
			ans += tmp;
		}
		printf("Case #%d: %d\n", kk, ans);
	}
	return 0;
}