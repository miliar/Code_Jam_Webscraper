#include <iostream>
#include <string>
#include <map>
using namespace std;

const int LL = 16, NN = 5005;
char dict[NN][LL];

int main(int argc, char** argv){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int L, D, N;
	scanf("%d%d%d", &L, &D, &N);
	for(int i = 0; i < D; ++i){
		scanf("%s", dict[i]);
	}
	for(int cs = 1; cs <= N; ++cs){
		int res = 0;
		char str[LL * 30];
		scanf("%s", str);
		bool flag[LL][26];
		memset(flag, 0, sizeof(flag));
		int index = 0, len = strlen(str);
		for(int i = 0; i < len; ++index){
			if(str[i] == '('){
				int j = i + 1;
				for(; str[j] >= 'a' && str[j] <= 'z'; ++j)
					flag[index][str[j] - 'a'] = true;
				i = j + 1;
			}
			else{
				flag[index][str[i] - 'a'] = true;
				++i;
			}
		}
		if(index == L){
			for(int i = 0; i < D; ++i){
				int j = 0;
				for(; j < L && flag[j][dict[i][j] - 'a']; ++j);
				if(j >= L) ++res;
			}
		}
		printf("Case #%d: %d\n", cs, res);
	}
	return 0;
}