#include <cstdio>
#include <algorithm>

bool is_max(char map[], char arr[], int len){
	int idx = 0;
	for(int i = 9; i > 0; i--){
		for(int n = map[i]; n; n--){
			if(arr[idx++] != i) return false;
		}
	}
	return true;
}

bool solve(char map[], char arr[], int len, char ret[]){
	if(len <= 1) return false;
	if(map[arr[0]]){
		map[arr[0]]--;
		ret[0] = arr[0];
		if(solve(map, arr + 1, len - 1, ret + 1)) return true;
		map[arr[0]]++;
	}
	for(int i = arr[0] + 1; i < 10; i++){
		if(!map[i]) continue;
		map[i]--;
		(ret++)[0] = i;
		while(map[0]--) (ret++)[0] = 0;
		for(int i = 1; i < 10; i++) for(int m = map[i]; m; m--) (ret++)[0] = i;
		return true;
	}
	return false;
}

int main(){
	int T = 0;
	scanf("%d ", &T);
	char arr[32];
	for(int ttt = 1; ttt <= T; ttt++){
		scanf("%s", arr);
		char map[10] = {0};
		int len = 0;
		for(; arr[len]; len++) map[arr[len] -= '0']++;
		char ret[32] = {0};
		if(is_max(map, arr, len)){
			int idx = len;
			for(int i = 0; i < len; i++){
				if(arr[i]) ret[idx--] = arr[i] + '0';
			}
			ret[0] = ret[++idx];
			for(int i = 1; i <= idx; i++) ret[i] = '0';
			printf("Case #%d: %s\n", ttt, ret);
		}else{
			solve(map, arr, len, ret);
			for(int n = 0; n < len; n++) ret[n] = ret[n] + '0';
			printf("Case #%d: %s\n", ttt, ret);
		}
	}
	return 0;
}
