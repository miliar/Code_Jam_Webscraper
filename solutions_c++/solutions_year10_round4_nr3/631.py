#include <cstdio>

#define FOR(i,a,b)	for(int i=(a);i<(int)(b);++i)
#define FOR_R(i,a,b)	for(int i=(b)-1;i>=(int)(a);--i)

int main(){
	int T;
	scanf("%d ", &T);
	for(int xxx = 1; xxx <= T; ++xxx){
		int R;
		scanf("%d ", &R);
		char map[500][500] = {0};
		int count = 0;
		int x_min = 1000001, x_max = -1;
		int y_min = 1000001, y_max = -1;
		FOR(i, 0, R){
			int x1, x2, y1, y2;
			scanf("%d %d %d %d ", &x1, &y1, &x2, &y2);
			FOR(x, x1, x2+1) FOR(y, y1, y2+1) if(!map[x+1][y+1]) count += map[x+1][y+1] = 1;
			if(x1 < x_min) x_min = x1;
			if(x2 > x_max) x_max = x2;
			if(y1 < y_min) y_min = y1;
			if(y2 > y_max) y_max = y2;
		}
		int ret = 0;
		while(count > 0){
			ret++;
			count = 0;
			int x_min2 = 1000001, x_max2 = -1;
			int y_min2 = 1000001, y_max2 = -1;
			FOR_R(x, x_min, x_max+2) FOR_R(y, y_min, y_max+2){
				char n = map[x+1][y+1-1];
				char w = map[x+1-1][y+1];
				if(n == w) map[x+1][y+1] = n;
				if(!map[x+1][y+1]) continue;
				count++;
				if(x < x_min2) x_min2 = x;
				if(x > x_max2) x_max2 = x;
				if(y < y_min2) y_min2 = y;
				if(y > y_max2) y_max2 = y;
			}
			x_min = x_min2;
			x_max = x_max2;
			y_min = y_min2;
			y_max = y_max2;
		}
		printf("Case #%d: %d\n", xxx, ret);
	}
	return 0;
}
