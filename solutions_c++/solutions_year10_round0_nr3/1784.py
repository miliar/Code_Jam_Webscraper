# include <stdio.h>
# include <string.h>
# include <algorithm>

using namespace std;

# define MAXN 1024

int T, R, k, N;
long long vet[MAXN];
long long numeros[(MAXN)*(MAXN)];
long long sum[MAXN];
int marca[MAXN];
int pai[MAXN];
int next[MAXN];

int main (void){
	int tc = 1;
	scanf("%d", &T);
	while(T--){
		scanf("%d%d%d", &R, &k, &N);
		for(int i = 0;i<N;i++) scanf("%I64d", &vet[i]);
		int cnt = 0;
		for(int i = 0;i<N+1;i++) for(int j = 0;j<N;j++) numeros[cnt++] = vet[j];
		int soma = 0;
		for(int i = 0;i<MAXN;i++) sum[i] = 0;
		memset(marca, 0, sizeof(marca));
		memset(pai, 0, sizeof(pai));
		memset(next, 0, sizeof(next));
		int cont = 0;
		int flag = 0;
		int nelem = 0;
		for(int i = 0;i<cnt;i++){
			if(soma + numeros[i] <= k && nelem < N){
//				printf("%d\n", numeros[i]);
				soma+=numeros[i];
				nelem++;
			}
			else{
//				printf("%d\n", soma);
//				printf("---\n");
				if(soma == 0){
					flag = 1;
					break;
				}
				int ind = (i-1)%N;
				if(marca[ind] ==0){
					marca[ind] = 1;
					if(ind == N-1) pai[cont] = 0, next[ind] = 0;
					else{
						pai[cont] = cont+1;
						next[ind] = cont+1;
					}
					sum[cont++] = soma;
					i--;
					soma = nelem = 0;
				}
				else{
					pai[cont] = next[ind];
					sum[cont++] = soma;
					i--;
					soma = 0;
					nelem = 0;
					break;
				}
			}
		}
		// 1 4 2 1
		long long resp = 0;
		int tot = 0;
		int i = 0;
		printf("Case #%d: ", tc++);
		if(flag){
			int menor = min(cont, R);
			for(int i = 0;i<menor;i++) resp+=sum[i];
		}
		else{
			while(tot < R){
//				printf("%d\n", sum[i]);
				resp+=sum[i];
				i = pai[i];
				tot++;
			}
		}
		printf("%I64d\n", resp);
	}
	return 0;
}