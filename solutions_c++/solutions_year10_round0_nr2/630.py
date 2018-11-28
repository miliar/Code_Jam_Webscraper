#include <cstdio>
#include <algorithm>

using namespace std;

int t[5];
int qtd;

void read() {
	scanf("%d", &qtd);
	
	for (int i = 0; i < qtd; i++) {
		scanf("%d", &t[i]);
	}
	
	
}

void process() {
	sort(t, t+qtd);
	
	int t1 = t[0];
	int t2 = t[1];
	int t3 = t[2];
	
	int num = t2 - t1;
	if (num == 0) {
		num = t3 - t1;
	}
	
	int r;
	int T;
	int maiorT = 1;
	int y = 0;
	for (int i = 1; i*i <= num; i++) {
		
		if (num%i == 0) {
			T = i;
			r = t1%T;
			if (T > maiorT && t2%T == r && (qtd == 2 || t3%T == r)) {
				maiorT = T;
				y = (T-r)%T;
			}
		
			T = num/i;
			r = t1%T;
			if (T > maiorT && t2%T == r && (qtd == 2 || t3%T == r)) {
				maiorT = T;
				y = (T-r)%T;
			}
		}
	}
	
	printf("%d\n", y);
}

int main() {
	
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
		
	int casos;
	scanf("%d", &casos);
	for (int i = 1; i <= casos; i++) {
		read();
		printf("Case #%d: ", i);
		process();
	}
	
	return 0;
}