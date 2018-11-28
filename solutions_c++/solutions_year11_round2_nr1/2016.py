#include <cstdio>


char play[103][103];
int wc[103], gc[103];
long double wp[103], owp[103], oowp[103];
int globalcount;

int main() {
	
	int T, N;
	char c;
	scanf("%d ", &T);
	for(int t=0; t<T; t++){
		scanf("%d ", &N);
		for(int i=0; i<N; i++) {
			wc[i]=0; gc[i]=0;
			for(int j=0; j<N; j++) {
				scanf("%c ", &play[i][j]);
				//printf("%c", play[i][j]);
				if(play[i][j]=='1')
					wc[i]++;
				if(play[i][j]!='.')
					gc[i]++;
			}
			//printf("\n");
			scanf(" ");
			globalcount += wc[i];
			if(gc[i]==0)
				wp[i]=0;
			else
				wp[i] = (long double)wc[i] / (long double)gc[i];
		}	
		for(int i=0; i<N; i++) {
			owp[i] = 0;int ct=0;
			for(int j=0; j<N; j++) {
				
				if(j!=i && play[i][j]!='.') {
					ct++;
					int gamesplayed = (gc[j]-1);
					if(gamesplayed > 0) {
						long double x = (long double)(wc[j]-(play[j][i]=='1'?1:0))/ (double)gamesplayed;
						//printf("%d %d %Lf\n", i, j, x);
						owp[i] += x;
					}
				}
			}
			//printf("owp %d %Lf\n", i, owp[i]); 
			owp[i] = owp[i] / (double)ct;
		}
		for(int i=0; i<N; i++) {
			oowp[i]=0;
			int ct=0;
			for(int j=0; j<N; j++) {
			
				if(i!=j&& play[i][j]!='.') {
					ct++;
					oowp[i]+=owp[j];
					}
			}
			oowp[i] = oowp[i]/(double)ct;
		}
		
		printf("Case #%d:\n", t+1);
		for(int n=0; n<N; n++) {
			printf("%.12Lf\n", 0.25*wp[n]+0.5*owp[n]+0.25*oowp[n]);
		}
	
	
	
	}




	return 0;
}

