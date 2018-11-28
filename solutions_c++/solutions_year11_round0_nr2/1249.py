#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
using namespace std;

char com[256], com2[256], op[256], res[105], tmp[5];

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int testCase;
	scanf("%d", &testCase);
	for(int tc = 1; tc <= testCase; ++tc){
		map<char, int> freq;
		int C, D, N, cnt = 0;
		cin >> C;
		for(int i = 0; i < C; ++i){
			cin >> tmp;
			com[tmp[0]] = tmp[1];
			com2[tmp[0]] = tmp[2];
			com[tmp[1]] = tmp[0];
			com2[tmp[1]] = tmp[2];
		}
		cin >> D;
		for(int i = 0; i < D; ++i){
			cin >> tmp;
			op[tmp[0]] = tmp[1];
			op[tmp[1]] = tmp[0];
		}
		cin >> N >> res;
		for(int i = 0; i < N; ++i){
			res[cnt++] = res[i];
			++freq[res[i]];
			bool combined = false;
			while(cnt >= 2 && com[res[cnt - 1]] == res[cnt - 2]){
				char c = com2[res[cnt - 1]];
				cnt -= 2;
				res[cnt++] = c;
				--freq[res[cnt - 1]];
				--freq[res[cnt - 2]];
				++freq[c];
				combined = true;
			}
			if(!combined && freq[op[res[cnt - 1]]] > 0){
				cnt = 0;
				freq.clear();
			}
		}

		printf("Case #%d: [", tc);
		for(int i = 0; i < cnt; ++i){
			if(i > 0) printf(", ");
			printf("%c", res[i]);
		}
		printf("]\n");
	}
	return 0;
}
