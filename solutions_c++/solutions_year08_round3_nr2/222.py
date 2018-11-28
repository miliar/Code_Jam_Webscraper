#include <cstdio>
#include <cstring>
#include <memory>
using namespace std;

const int LEN = 64;
typedef long long int64;
int cnt, n;
char exp[LEN];
int sign[LEN];

void calc(){
	int64 res = 0;
	int tSign[LEN];
	memcpy(tSign, sign, sizeof(sign));
	for(int i = 0, x = 1; i < n; ){
		int64 tmp = 0LL;
		while(!tSign[i] && i < n){
			tmp = tmp * 10 + exp[i] - '0';
			i++;
		}
		res += x * tmp;
		x = tSign[i];
		tSign[i] = 0;
	}
	cnt += ((res % 2 == 0) || (res % 3 == 0) 
			|| (res % 5 == 0) || (res % 7 == 0));
}

void dfs(int i){
	if(i == n){
		calc();
		return;
	}
	sign[i] = 0; dfs(i + 1);
	sign[i] = 1; dfs(i + 1);
	sign[i] = -1; dfs(i + 1);
}

int main(){
	int nCase;
	scanf("%d", &nCase);
	for(int ca = 1; ca <= nCase; ++ca){
		scanf("%s", exp);
		n = strlen(exp);
		cnt = 0;
		dfs(1);
		printf("Case #%d: %d\n", ca, cnt);
	}
	return 0;
}
