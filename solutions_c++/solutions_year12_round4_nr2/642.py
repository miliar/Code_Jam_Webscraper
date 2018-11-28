#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#define MAX 1005

using namespace std;

int N, W, L;
double r[MAX];
double px[MAX], py[MAX];
bool deu;


void f (int mask){
	if(deu)
		return;
	if (mask == (1<<N) - 1){
		for (int i = 0; i < N; i++)
			printf(" %.1f %.1f", px[i], py[i]);
		printf("\n");
		deu = true;
		return;
	}
	int x;
	for (x = 0; x < N; x++)
		if(((1<<x) & mask) == 0)
			break;
	for (int j = 0; j < 10; j++){
		double w = rand() % (W + 1);
		double l = rand() % (L + 1);
		bool valido = true;
		for (int i = 0; i < x; i++)
			if(hypot(px[i] - w, py[i] - l) < r[i] + r[x])
				valido = false;
		if(valido){
			px[x] = w;
			py[x] = l;
			f(mask | (1<<x));
		}
		if(deu)
			break;
	}
}

int main(){
	int T;
	scanf("%d", &T);
	srand(5);
	for (int t = 1; t <= T; t++){
		scanf("%d%d%d", &N, &W, &L);
		for (int i = 0; i < N; i++)
			scanf("%lf", &r[i]);
		printf("Case #%d:", t);
		deu = false;
		f(0);

	}
	return 0;
}
