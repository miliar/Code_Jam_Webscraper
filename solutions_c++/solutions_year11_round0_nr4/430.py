#include <stdio.h>
#include <algorithm>

using namespace std;

int n;

long double comb[1003][1003];
long double d[1020] = {1,0, };
long double f[1020] = {0,0,2};
long double fact[1003];

int dat[1003];
int v[1003];
int main(){
	comb[0][0] = 1;
	fact[0] = 1;
	d[0] = 1;
	for(int i = 1; i <= 1000 ;i++){
		fact[i] = fact[i-1] * i;
		if(i >= 2){
			d[i] = (i-1) * (d[i-1] + d[i-2]);
		}
		comb[i][0] = 1;
		for(int j = 1;j <= i;j++){
			comb[i][j] = comb[i-1][j] + comb[i-1][j-1];
		}
	}
	for(int i = 2;i <= 1000;i ++){
		f[i] = 0;
		for(int j = 1;j <= i;j ++){
			f[i] += comb[i][j] * d[i-j] * (f[i-j]);
		}
		f[i] += fact[i];
		f[i] /= fact[i] - d[i];
	}
	int T;
	scanf("%d",&T);
	for(int testcase = 1; testcase <= T; testcase ++){
		scanf("%d",&n);
		for(int i = 0;i < n;i ++){
			scanf("%d",&dat[i]);
			dat[i] --;
		}

		fill(v,v+n,0);

		long double ans = 0;

		for(int i = 0;i < n;i ++){
			if(v[i] == 0){
				v[i] = 1;
				int p = i;
				int cnt = 0;
				do{
					cnt ++;
					v[p] = 1;
					p = dat[p];
				}while(p!=i);

				ans += f[cnt];
			}
		}


		printf("Case #%d: %.10Lf\n",testcase,ans);
	}
	return 0;
}

