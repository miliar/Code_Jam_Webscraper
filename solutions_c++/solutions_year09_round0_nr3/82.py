#include <cstdio>
#include <cstring>
using namespace std;

const int maxn = 600;
const int maxm = 30;
const int lp = 19;

char P[] = "welcome to code jam";
char T[maxn];
int data[maxn][maxm];
int res[5];

int get_cnt(){
	int i, j, k, p, q, ans = 0, lt = strlen(T);
	for(i = 0; i < lt; i++){
		for(j = 0; j < lp; j++) data[i][j] = 0;
	}
	for(i = lt - 1; i >= 0; i--){
		for(j = 0; j < lp; j++){
			if(T[i] != P[j]) continue;
			if(j == lp - 1){
				data[i][j] = 1;
				continue;
			}
			for(k = i + 1; k < lt; k++){
				data[i][j] = ( data[i][j] + data[k][j + 1]) % 10000;
			}
		}
	}
	for(i = 0; i < lt; i++){
		ans = (ans + data[i][0]) % 10000;
	}
	return ans;
}

void output(int cases, int ans){
	int i, j, k;
	printf("Case #%d: ", cases);
	for(k = 0; k < 4; k++) res[k] = 0;
	for(k = 0; k < 4; k++){
		i = ans % 10;
		res[3 - k] = i;
		ans /= 10;
	}
	for(k = 0; k < 4; k++) printf("%d", res[k]);
	printf("\n");
}

int main(){
	freopen("C.out", "w", stdout);
	int t, i, ans;
	scanf("%d\n", &t);
	for(i = 1; i <= t; i++){
		gets(T);
		ans = get_cnt();
		output(i, ans);
	}
}
				
				
