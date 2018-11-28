#include <stdio.h>
#define max(a,b) (((a)>(b))?(a):(b))
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	int n;
	scanf("%d",&T);
	while(T>0){T--;
		scanf("%d",&n);
		int i, to, tb, po, pb, dis;
		to = tb = 0;
		po = pb = 1;
		for(i=0;i<n;i++){
			char robot[5];
			int pos;
			scanf("%s %d", robot, &pos);
			if(robot[0] == 'O'){
				dis = pos - po; if(dis < 0) dis = -dis;
				po = pos;
				to = max(tb, to + dis) + 1;
			}
			if(robot[0] == 'B'){
				dis = pos - pb; if(dis < 0) dis = -dis;
				pb = pos;
				tb = max(to, tb + dis) + 1;
			}
		}
		static int cs = 1;
		printf("Case #%d: %d\n", cs++, max(to,tb));
	}
	return 0;
}