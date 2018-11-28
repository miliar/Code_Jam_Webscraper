#include <cstdio>

int W,L,U,G;
double x[110][2], y[110][2];

double get(double xlim, int ind, int tam){
	double res = 0;
	
	for(int i = 0; i+1 < tam && x[i][ind] < xlim; i++){
		if(x[i+1][ind] < xlim){
			res += (y[i][ind] + y[i+1][ind])*(x[i+1][ind]-x[i][ind])/2.0;
		}else{
			double yy = y[i][ind] + (y[i+1][ind]-y[i][ind])*(xlim-x[i][ind])/(x[i+1][ind]-x[i][ind]);
			res += (y[i][ind] + yy)*(xlim-x[i][ind])/2.0;
			
			
			break;
		}
	}
	return res;
}

int main(){
	
	int casos;
	
	scanf("%d", &casos);
	
	for(int i = 1; i <= casos; i++){
		
		scanf("%d%d%d%d", &W, &L, &U, &G);
		
		for(int j = 0; j < L; j++)
			scanf("%lf%lf", &x[j][0], &y[j][0]);
			
		
		for(int j = 0; j < U; j++)
			scanf("%lf%lf", &x[j][1], &y[j][1]);
		
		double area = get(W,1,U)-get(W,0,L);
		double pedaco = area/G;
		double ant = 0;
		printf("Case #%d:\n", i);
		
		for(int j = 1; j < G; j++){
			double ini = ant, fim = W, med;
			double alvo = pedaco*j;
			
			for(int k = 0; k <= 100 && fim-ini > 1E-8; k++){
				med = (ini+fim)/2;
				
				if(get(med,1,U)-get(med,0,L) < alvo - 1E-8)
					ini = med;
				else
					fim = med;
			}
			printf("%.7lf\n", ini);
			ant = ini;
		}
	}
	
	return 0;
}
