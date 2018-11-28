#include <cstdio>
#include <vector>
#include <cstring>
#define MAXN 32
#define MAXL 128
#define PB push_back
#define MP make_pair
#define GI(x) ((x)-'A')
using namespace std;
int main() {
	int cas, cs = 1;
	int trans[MAXN][MAXN];
	int cnt[MAXN];
	vector<int> op[MAXN];
	scanf("%d", &cas);
	while(cas--) {
		int c, d, n, len;
		char tmp[MAXL];
		scanf("%d", &c);
		memset(trans, -1, sizeof(trans));
		memset(cnt, 0, sizeof(cnt));
		for(int i = 0; i < MAXN; ++i)
			op[i].clear();
		for(int i = 0; i < c; ++i) {
			scanf("%s", tmp);
			trans[GI(tmp[0])][GI(tmp[1])] = GI(tmp[2]);
			trans[GI(tmp[1])][GI(tmp[0])] = GI(tmp[2]);
		}
		scanf("%d", &d);
		for(int i = 0; i < d; ++i) {
			scanf("%s", tmp);
			op[GI(tmp[0])].PB(GI(tmp[1]));
			op[GI(tmp[1])].PB(GI(tmp[0]));
		}
		scanf("%d%s", &len, tmp);
		int stk[MAXL];
		int ptr = 0;
		for(int i = 0; i < len; ++i) {
			int c = GI(tmp[i]);
			while(ptr != 0 && trans[stk[ptr - 1]][c] != -1) {
				c = trans[stk[ptr - 1]][c];
				--cnt[stk[ptr - 1]];
				--ptr;
			}
			stk[ptr++] = c;
			++cnt[c];
			for(int i = 0; i < op[c].size(); ++i) {
				if(cnt[op[c][i]] > 0) {
					while(ptr != 0) {
						--cnt[stk[ptr - 1]];
						--ptr;
					}
					break;
				}
			}
		}	
		printf("Case #%d: [", cs);
		for(int i = 0; i < ptr; ++i) {
			putchar(stk[i] + 'A');
			if(i != ptr - 1)
				printf(", ");
		}
		printf("]\n");
		++cs;
	}
	return 0;
}
