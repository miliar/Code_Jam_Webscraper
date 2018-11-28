#include <cstdio>
using namespace std;

int t, a, b;
int list[1000][6] = {2000};

int main(){
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	for(int i = 1; i < 1000; ++i)
		list[i][0] = 0;
	for(int i = 1; i < 10; ++i){
		list[i][0] = 2;
		list[i][1] = i * 10;
		list[i][2] = i * 100;
	}
	for(int i = 1; i < 10; ++i)
		for(int j = 0; j < 10; ++j){
			int m = i * 10 + j;
			list[m][0] = 2;
			list[m][1] = i * 100 + j;
			list[m][2] = i * 100 + j * 10;
			if(i < j){
				++list[m][0];
				list[m][list[m][0]] = i + j * 10;
			}
		}
	for(int i = 1; i < 10; ++i)
		for(int j = 0; j < 10; ++j)
			for(int k = 0; k < 10; ++k){
				int m = i * 100 + j * 10 + k;
				if(i < j || (i == j && i < k)){
					++list[m][0];
					list[m][list[m][0]] = j * 100 + k * 10 + i;
				}
				if(i < k || (i == k && i > j)){
					++list[m][0];
					list[m][list[m][0]] = k * 100 + i * 10 + j;
				}
			}
	scanf("%d", &t);
	for(int i = 0; i < t; ++i){
		scanf("%d%d", &a, &b);
		int ans = 0;
		for(int j = a; j < b; ++j)
			for(int k = 1; k <= list[j][0]; ++k){
				//printf("%d ", list[j][k]);
				if(list[j][k] <= b) ++ans;
			}
		//printf("\n");
		if(b == 1000){
			if(a <= 100) ++ans;
			if(a <= 10) ++ans;
			if(a == 1) ++ans;
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}

