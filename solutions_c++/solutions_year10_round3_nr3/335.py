#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#define MAX 512

int n, m;
bool map[MAX][MAX], able[MAX][MAX];

inline int min(int a, int b){return (a < b)?a:b;}
inline int max(int a, int b){return (a > b)?a:b;}

int get_num(char cc){
	if (cc >= '0' && cc <= '9') return cc - '0';
	else return cc - 'A' + 10;
}

void init(){
	int i, j;
	scanf("%d %d", &m, &n);
	memset(map, false, sizeof map);
	memset(able, true, sizeof able);
	for (i = 0; i < m; i++){
		char buf[MAX / 4 + 2];
		scanf("%s", buf);
		for (j = 0; j < strlen(buf); j++){
			int tmp = get_num(buf[j]);
			map[i][4*j+3] = (tmp % 2 == 1); tmp >>= 1;
			map[i][4*j+2] = (tmp % 2 == 1); tmp >>= 1;
			map[i][4*j+1] = (tmp % 2 == 1); tmp >>= 1;
			map[i][4*j] = (tmp % 2 == 1);
		}
	}
}

bool is_chess(int x, int y, int ptr){
	bool src = map[x][y];
	for (int i = 0; i < ptr; i++)
		for (int j = 0; j < ptr; j++)
			if ((i + j) % 2 && map[x + i][y + j] == src){
				return false;
			}
			else if ((i + j) % 2 == 0 && map[x + i][y + j] != src){
				return false;
			}
	return true;
}

void remove(int x, int y, int ptr){
	for (int i = 0; i < ptr; i++)
		for (int j = 0; j < ptr; j++){
			able[x + i][y + j] = false;
		}
}

bool could(int x, int y, int ptr){
	for (int i = 0; i < ptr; i++)
		for (int j = 0; j < ptr; j++){
			if (!able[x+i][y+j]) return false;
		}
	return true;
}

void solve(int cases){
	int rec[MAX], cnt, ptr, res = 0;
	memset(rec, 0, sizeof rec);
	for (ptr = min(m, n); ptr > 0; ptr--){
		int ret = 0;
		for (int x = 0; x <= m - ptr; x++)
			for (int y = 0; y <= n - ptr; y++){
				if (could(x, y, ptr) && is_chess(x, y, ptr)){ 
					ret++;
					remove(x, y, ptr);
				}
			}
		rec[ptr] = ret;
		if (ret) res++;
	}
	
	printf("Case #%d: %d\n", cases, res);
	for (ptr = min(m, n); ptr; ptr--)
		if (rec[ptr] != 0) printf("%d %d\n", ptr, rec[ptr]);
}

int main(){
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	int t, cases = 1;
	scanf("%d", &t);
	while (cases <= t){
		int res;
		init();
		solve(cases++);
	}
	return 0;
}