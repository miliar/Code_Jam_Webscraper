#include <cstdio>

int v1[8];
int v2[8];
int n;
bool primeiro;
int vT[8];
bool jaFoi[8];
int melhor;

void read() {
	scanf("%d", &n);
	
	for (int i = 0 ; i < n ; i++) {
		scanf("%d", &v1[i]);
	}
	
	for (int i = 0 ; i < n ; i++) {
		scanf("%d", &v2[i]);
		jaFoi[i] = false;
	}
	primeiro = true;
	
}



void process(int ind) {
	if (ind == n) {
		int soma = 0;
		for (int i = 0 ; i < n ; i++) {
			soma+= vT[i]*v2[i];
		}
		//printf("%d ", soma);
		if (primeiro) {
			melhor = soma;
			primeiro = false;
		} else if(soma < melhor) {
			melhor = soma;
		}
	} else {
		
		for (int i = 0 ; i < n ; i++) {
			if (!jaFoi[i]) {
				jaFoi[i] = true;
				vT[ind] = v1[i];
				process(ind+1);
				jaFoi[i] = false;
			}
		}
		
		
	}
	
}

int main () {
	
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	
	int qnt;
	scanf("%d", &qnt);
	
	for (int iMain = 0 ; iMain < qnt ; iMain++) {
		read();
		process(0);
		printf("Case #%d: %d\n", iMain+1, melhor);
	}
	
	return 0;
}
