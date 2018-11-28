#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<map>
#define ZERO 1e-9

using namespace std;

double vel[1000100];

int main (void) {
	int T, cases, X, B[1010], E[1010], N;
	double S, R, w[1010], t;
	
	scanf("%d",&T);
	
	for(int cases = 1; cases <= T; cases++) {
	
		scanf("%d %lf %lf %lf %d",&X,&S,&R,&t,&N);
		for(int j = 0; j <= X; j++) vel[j] = S;
		
		for(int j = 0; j < N; j++) {
			scanf("%d %d %lf",&(B[j]),&(E[j]),&(w[j]));
			for(int k = B[j]; k < E[j]; k++) vel[k] += w[j];
		}
		
		sort(vel,vel+X);
		double corri_tot = t, resp = 0., corri_loc, vel1, vel2;
		
		//correndo em cima das esteiras...
		for(int j = 0; j< X; j++) {
		//	printf(">> %lf\n",resp);
			vel1 = vel[j]+(R-S);
			vel2 = vel[j];
			
			if ( corri_tot > ZERO) {
				
				corri_loc = 1./vel1;
				if ( corri_loc > corri_tot ) {
					corri_loc = corri_tot;
					resp += (1-vel1*corri_tot)/vel2;
				}
				
				resp += corri_loc;
				corri_tot -= corri_loc;
			}
			
			else resp += 1./vel2;
		}
				
		printf("Case #%d: %.10lf\n",cases,resp);
	}
	return 0;
}
