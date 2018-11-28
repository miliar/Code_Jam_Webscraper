#include<cstdio>
#include<algorithm>
typedef long long LL;
const int MAXN = (1<<9);
//const int MAXN = (1<<3);
const bool dbg = 0;
LL P = 100003;
LL cnt[MAXN][MAXN];// [n][k] ile jest zbiorów S < {2..n} : |S| = k i n jest "pure"
LL dwu[MAXN][MAXN];// [n][k] n po k mod P
void preprocess(){
	for(int i=0;i<MAXN;i++){
		dwu[0][i] = 0;
		dwu[i][0] = 1;
		cnt[0][i] = 0;
		cnt[1][i] = 0;
		cnt[2][i] = 0;
		cnt[i][0] = 0;
		cnt[i][1] = 1;
	}
	cnt[2][1] = 1;
	dwu[0][0] = 1;
	for(int n = 1;n<MAXN;n++)
		for(int k = 1;k<MAXN;k++)
			dwu[n][k] = (dwu[n-1][k]+dwu[n-1][k-1])%P;
	for(int n = 3; n < MAXN; n++){
		for(int k = 2; k<MAXN;k++){
			cnt[n][k] = 0;
			if(k>=n)continue;
			for(int p = 1; p < k; p++){
				cnt[n][k] += (cnt[k][p]*(dwu[n-k-1][k-1-p]))%P;
				cnt[n][k] %= P;
			}
		}
	}
	if(dbg){
		for(int n=1;n<MAXN;n++){
			for(int k=1;k<n;k++)
				printf("%2d ",(int)cnt[n][k]);
			printf("\n");
		}
	}
}

void solveCase(int c){
	int n;
	scanf("%d",&n);
	int res = 0;
	for(int i=0;i<n;i++){
		res += cnt[n][i];
		res %= P;
	}
	printf("Case #%d: %d\n",c,res);
}

int main(){
	int cas;
	preprocess();
	scanf("%d",&cas);
	for(int i=0;i<cas;i++)
		solveCase(i+1);
	return 0;
}
