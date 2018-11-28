#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

int B[1010], E[1010], w[1010];
int pos[1010];

bool cmp(int a, int b){
	return w[a] < w[b];
}

int main(){
	int caso = 1;
	int casos;
	scanf("%d", &casos);
	
	for(int i = 1; i <= casos; i++){
		int N;
		double X,S,R;
		double t;
		
		scanf("%lf%lf%lf%lf%d", &X, &S, &R, &t, &N);
		
		int totalL = 0;
		int running = 0;
		for(int i = 0; i < N; i++){
			scanf("%d%d%d", &B[i], &E[i], &w[i]);	
			totalL += E[i]-B[i];
			pos[i] = i;
		}
		sort(pos,pos+N,cmp);
		double res = 0;
		
		if((X-totalL) <= t*R){
			t -= (X-totalL)/(double)R;
			res += (X-totalL)/(double)R;
			for(int i = 0; i < N; i++){
				if((E[pos[i]]-B[pos[i]])/(double)(R+w[pos[i]]) <= t){
					t -= (E[pos[i]]-B[pos[i]])/(double)(R+w[pos[i]]);
					res += (E[pos[i]]-B[pos[i]])/(double)(R+w[pos[i]]);
				}else{
					double dist = (E[pos[i]]-B[pos[i]]);
					dist -= t*(R+w[pos[i]]);
					res += t + dist/(double)(S+w[pos[i]]);
					t = 0;
				}
			}
		}else{
			X -= totalL;
			X -= t*R;
			
			res += t + X/(double)S;
			
			//printf("%lf\n", res);
			for(int i = 0; i < N; i++){
				res += (E[i]-B[i])/(double)(S+w[i]);
			}
		}
		printf("Case #%d: %.9lf\n",caso++,res);
	}
	
	return 0;
}