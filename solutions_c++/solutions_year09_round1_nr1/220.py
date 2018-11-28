#include <iostream>
#include <algorithm>
using namespace std;

char s[100];
int a[100];
int res, total, times;
int used[1000000];

bool solve(int v){
	int t = res, temp;
	while(t > 1){
		if(used[t] == times) return false;
		used[t] = times;
		temp = 0;
		while(t){
			int k = t % v;
			temp += k * k;
			t = (t - k) / v;
		}
		t = temp;
	}
	return true;
}

void cal(){
	res = 2;
	while(true){
		bool flag = true;
		for(int i = 0; i < total && flag; ++i){
			++times;
			if(!solve(a[i])) flag = false;
		}
		if(flag) return;
		++res;
	}
	return;
}

int main(){
	int cases, ttt = 1;
	freopen("D:\\A-small-attempt0.in", "r", stdin);
	freopen("D:\\reslut.out", "w", stdout);
	scanf("%d", &cases);
	getchar();
	while(cases--){
		times = 0;
		total = 0;
		int pos = 0;
		scanf("%d", &a[total++]);
		char ch;
		while(ch = getchar(), ch == ' ') scanf("%d", &a[total++]);
		memset(used, 0, sizeof(used));
		cal();
		printf("Case #%d: %d\n", ttt++, res);
	}
	return 0;
}