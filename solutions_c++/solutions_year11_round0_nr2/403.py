#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <queue>
#include <map>
#include <stack>
using namespace std;

char change[100][10], ope[50][10];
char str[200];
string ans;


bool judge(int len, int pos1, int pos2){

	if (ans[len-1] == change[pos2][0] && str[pos1] == change[pos2][1])
		return true;

	else if(ans[len-1] == change[pos2][1] && str[pos1] == change[pos2][0])
		return true;

	else
		return false;
}

int main(){

	freopen("", "r", stdin);
	freopen("B.txt", "w", stdout);

	int T;
	int C, D, N;
	int cas = 1;


	scanf("%d", &T);
	while (T--){

		ans = "";

		scanf("%d", &C);
		for (int i = 0; i < C; i++){
			scanf("%s", change[i]);
		}

		scanf("%d", &D);
		for (int i = 0; i < D; i++){
			scanf("%s", ope[i]);
		}

		scanf("%d", &N);
		scanf("%s", str);

		
		ans += str[0];
		for (int i = 1; i < N; i++){

			int len = ans.size();
			bool flag1 = false;
			bool flag2 = false;

			if (C != 0 && len >= 1){
				for (int j = 0; j < C; j++){
					if (judge(len, i, j)){
						ans[len-1] = change[j][2];
						flag1 = true;
						break;
					}
				}
			}

			if (flag1 == false && D != 0){
				for (int j = 0; j < D; j++){

					if (str[i] == ope[j][1]){
						for(int k = len-1; k >= 0; k--){
							if(ans[k] == ope[j][0]){
								flag1 = true;
								flag2 = true;
								break;
							}
						}
					}


					else if (str[i] == ope[j][0]){
						for (int k = len - 1; k >= 0; k--){
							if (ans[k] == ope[j][1]){
								flag1 = true;
								flag2 = true;
								break;
							}
						}
					}
					if (flag2)
						break;
				}
				if (flag2)
					ans = "";
			}

			if (flag1 == false)
				ans += str[i];
		}

		printf("Case #%d: [", cas++);
		int len = ans.size();
		if (len == 0)
			printf("]\n");

		else{
			for (int i = 0; i < len; i++){
				if (i == len-1)
					printf("%c]\n", ans[i]);

				else
					printf("%c, ", ans[i]);
			}
		}

	}
	return 0;
}