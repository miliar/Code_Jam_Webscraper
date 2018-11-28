#include <stdio.h>
#include <string.h>

#define MAXN 200

bool mp[2][MAXN][MAXN];

int main(){
	freopen("D:\\C-small-attempt0.in", "r", stdin);
	freopen("D:\\out.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for(int case_t = 1; case_t <= cases; ++case_t){
		int r, x1, y1, x2, y2;
		memset(mp, false, sizeof(mp));
		scanf("%d", &r);
		bool id = false;
		for(int i = 0; i < r; ++i){
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for(int xx = x1; xx <= x2; ++xx)
				for(int yy = y1; yy <= y2; ++yy)
					mp[id][yy][xx] = true;
		}
		int remain = 0;
		for(int i = 1; i <= 100; ++i)
			for(int j = 1; j <= 100; ++j)
				if(mp[id][i][j]) ++remain;
		int res = 0;
		while(remain){
			
			++res;
			for(int i = 1; i <= 100; ++i)
				for(int j = 1; j <= 100; ++j)
					if(mp[id][i][j]){
						if(!mp[id][i - 1][j] && !mp[id][i][j - 1]) mp[!id][i][j] = false, --remain;
						else mp[!id][i][j] = true;
					}
					else{
						if(mp[id][i - 1][j] && mp[id][i][j - 1]) mp[!id][i][j] = true, ++remain;
						else mp[!id][i][j] = false;
					}
			id = !id;
		}
		printf("Case #%d: %d\n", case_t, res);
	}
	return 0;
}