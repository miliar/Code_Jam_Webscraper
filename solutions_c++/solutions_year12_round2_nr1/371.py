#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <cstring>

using namespace std;

int t,n,soma;
int num[250];

bool pode (double val, int at){
	double ponto = val*soma;
	ponto += num[at];
	double rest = 1.0-val;
	for(int i = 0; i < n; ++i) if(i != at){
		double meu = ponto-num[i];
		if(meu <= 0) continue;
		double rem = meu/soma;
		rest -= rem;
		if(rest < 0) return true;
	}
	return false;
}

int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int caso = 0;
	
	scanf("%d", &t);
	
	while(t--){
		printf("Case #%d:", ++caso);
		scanf("%d", &n);
		int maior = 0, maior2 = 0;
		soma = 0;
		for(int i = 0; i < n; ++i) scanf("%d", num+i);
		for(int i = 0; i < n; ++i){
			soma += num[i];
			if(num[i] > maior2){
				maior2 = num[i];
				if(maior2 > maior) swap(maior, maior2);
			}
		}
		for(int i = 0; i < n; ++i){
			double lo = 0.0, hi = 1.0, mid;
			while(hi-lo > 1e-9){
				mid = (hi+lo)/2;
				if(pode(mid,i))
					hi = mid;
				else
					lo = mid;
			}
			printf(" %lf", lo*100);
		}
		printf("\n");
	}
	return 0;
}
