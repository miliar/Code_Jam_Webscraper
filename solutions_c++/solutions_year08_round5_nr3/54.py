
#include <iostream>
#include <vector>

int tbl[10][1<<10];
int bpop_tbl[1<<10];
int bpop(int n){
	int t = 0;
	while(n){
		t += n&1;
		n >>= 1;
	}
	return t;
}
using namespace std;
int main(void){
	int cases;
	cin >> cases;
	for(int case_no=1; case_no<=cases; case_no++){
		int h,w;
		cin >> h >> w;
		vector<int> broken_mask;
		for(int y=0; y<h;y++){
			string s;
			cin >> s;
			int mask = 0;
			for(int x=0; x<w; x++)
				mask |= (s[x] == 'x') << x;
			broken_mask.push_back(mask);
		}
		memset(tbl, 0x00, sizeof(tbl));
		for(int cur=0; cur<(1<<w); cur++){
			bpop_tbl[cur] = bpop(cur);
			if(cur & broken_mask[0]) continue;
			if(((cur >> 1)&cur)||((cur << 1) & cur)) continue;
			tbl[0][cur] = bpop_tbl[cur];
		}
		for(int y=1; y<h; y++){
			for(int prev = 0; prev < (1<<w); prev++){
				for(int cur=0; cur<(1<<w); cur++){
					if(cur & broken_mask[y]) continue;
					if(((cur >> 1)&cur)||((cur << 1) & cur)) continue;
					if((prev&(cur<<1))||((prev << 1) & cur)) continue;
					tbl[y][cur] = max(tbl[y][cur], tbl[y-1][prev] + bpop_tbl[cur]);
				}
			}
		}
		int ans = 0;
		for(int i=0; i<(1<<w); i++)
			ans = max(ans, tbl[h-1][i]);
		cout << "Case #"<<case_no<<": " << ans << endl;
	}
	return 0;
}
