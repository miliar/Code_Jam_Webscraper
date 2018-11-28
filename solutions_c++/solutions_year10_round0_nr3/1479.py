#include <stdio.h>

int t, r, k, n;
int it;
long long int money;
long long int recMoney;

int groups[1010];
int bigGr[1010][3];
int order[1010];

int main() {
	FILE* fp = fopen("C.out", "w");
	
	it = 1;
	scanf("%d", &t);

	for (it=1; it <= t; it++) {
		scanf(" %d%d%d", &r, &k, &n);

		for (int i=0; i<n; i++) {
			scanf(" %d", &groups[i]);
		}

		for (int i=0; i<n; i++) {
			int sum=0, j=i;
			
			do {
				sum+=groups[j];
				j++;
	
				if (j==n)
					j=0;
			} while ((sum+groups[j])<=k && i!=j);

			bigGr[i][0]=sum;
			bigGr[i][1]=j;
			bigGr[i][2]=0;
		}

		int g=0;
		int end;

		for (end=0; end<r; end++) {
			order[end]=g;
			
			if (bigGr[g][2])
				break; /* opa, recursao! */
			
			bigGr[g][2]=1;
			g=bigGr[g][1];						
		}

		money=0;
		recMoney=0;		
		int init;
		int aux;

		if (end == r) { /* nao achou recursao, soma o vet todo */
			for (int i=0; i<r; i++) 
				money += bigGr[order[i]][0];

		} else {
			recMoney= bigGr[order[end]][0];

			for (init = end-1; order[init] != g; init--) {
				recMoney += bigGr[order[init]][0];
			}

			aux=init-1;
			r-=init;

			for (aux; aux>=0; aux--) 
				money += bigGr[order[aux]][0];

			money += (recMoney*(r/(end-init)));

			for (int i=init; i < (init + r%(end-init)); i++)
				money+= bigGr[order[i]][0];
		}

		fprintf(fp, "Case #%d: %lld\n", it, money);
	}

	fclose(fp);

	return 0;
}
