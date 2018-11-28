#include<cstdio>

char wczyt[111][111];
long double wp[111], owp[111], oowp[111];
int wygrane[111], przegrane[111];
int N;

int main(){
	int testy;
	scanf("%d", &testy);
	for(int t = 1; t <= testy; t++){
		for(int i = 0; i < N; i++){
			wp[i] = 0;
			owp[i] = 0;
			oowp[i] = 0;
			wygrane[i] = 0;
			przegrane[i] = 0;
		}
		scanf("%d", &N);
		for(int i = 0; i < N; i++)
			scanf("%s", wczyt[i]);
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				if(wczyt[i][j]=='0')
					przegrane[i]++;
				else if(wczyt[i][j]=='1')
					wygrane[i]++;
			}
			wp[i] = (long double)(wygrane[i])/(wygrane[i]+przegrane[i]);
		}
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				if(wczyt[j][i]=='0')
					owp[i] += (long double)(wygrane[j])/(wygrane[j]+przegrane[j]-1);
				else if(wczyt[j][i]=='1')
					owp[i] += (long double)(wygrane[j]-1)/(wygrane[j]-1+przegrane[j]);
			}
			owp[i] /= wygrane[i]+przegrane[i];
		}
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++)
				if(wczyt[i][j]!='.')
					oowp[i] += owp[j];
			oowp[i] /= wygrane[i]+przegrane[i];
		}
		printf("Case #%d:\n", t);
		for(int i = 0; i < N; i++){
//printf("%Lf %Lf %Lf   ", wp[i], owp[i], oowp[i]);
			printf("%.10Lf\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}
	return 0;
}
