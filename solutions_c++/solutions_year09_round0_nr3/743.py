#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

char str[1000];
int ans[1000][50];
char sour[50];


void fix(int &a) {
	if(a >= 10000)a %= 10000;
}

void solve() {
	memset(ans,-1,sizeof(ans));
	int len = strlen(str),sl = strlen(sour);;
	for(int i = 0;i < len;++i) {
		if(str[i] == sour[0]) {
			ans[i][0] = 1;
		}
		for(int j = 1;j < sl;++j) {
			if(str[i] != sour[j])continue;
			for(int k = 0;k < i;++k) {
				if(str[k] == sour[j - 1] && ans[k][j - 1] != -1) {
					if(ans[i][j] == -1) {
						ans[i][j] = ans[k][j - 1];
					} else {
						ans[i][j] += ans[k][j - 1];
					}
					fix(ans[i][j]);
				}
			}
		}
	}
	int ret = 0;
	for(int i = 0;i < len;++i) {
		if(ans[i][sl - 1] != -1) {
			ret += ans[i][sl - 1];
			fix(ret);
		}
	}
	ans[len - 1][sl - 1] = ret;
	fix(ans[len - 1][sl - 1]);
	if(ans[len - 1][sl - 1] >= 1000) {
		printf("%d\n",ans[len - 1][sl - 1]);
	} else {
		if(ans[len - 1][sl - 1] < 1000 && ans[len - 1][sl - 1] >= 100) {
			printf("0%d\n",ans[len - 1][sl - 1]);
		} else {
			if(ans[len - 1][sl - 1] < 100 && ans[len - 1][sl - 1] >= 10) {
				printf("00%d\n",ans[len - 1][sl - 1]);
			} else {
				printf("000%d\n",ans[len - 1][sl - 1]);
			}
		}
	}
}


int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	strcpy(sour,"welcome to code jam");
	int T;
	int cas = 1;
	scanf("%d",&T);
	getchar();
	while(T--) {
		gets(str);
		printf("Case #%d: ",cas++);
		solve();
	}
	return 0;
}