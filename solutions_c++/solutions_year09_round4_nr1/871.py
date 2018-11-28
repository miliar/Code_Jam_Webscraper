#include <cstdio>
#include <vector>
#include <algorithm>

int main(){
	int T = 0;
	char buf[64];
	scanf("%d ", &T);
	for(int ttt = 1; ttt <= T; ttt++){
		int N = 0;
		scanf("%d ", &N);
		std::vector<char> temp(N), over(N);
		for(int x = 0; x < N; x++){
			scanf("%s ", buf);
			for(int i = 0; buf[i]; i++){
				if(buf[i] == '1') temp[x] = i;
			}
			over[x] = x;
		}
		int count = 0;
		while(temp.size()){
			int max_val = 0, max_pos = 0, max_idx = 0;
			for(int i = 0; i < (int)temp.size(); i++){
				const char pos = std::lower_bound(over.begin(), over.end(), temp[i]) - over.begin();
				const char val = pos - i;
				if(val <= max_val) continue;
				max_val = val;
				max_pos = pos;
				max_idx = i;
			}
			if(max_val == 0) break;
			temp.erase(temp.begin() + max_idx);
			over.erase(over.begin() + max_pos);
			count += max_val;
		}
		printf("Case #%d: %d\n", ttt, count);
	}
	return 0;
}
