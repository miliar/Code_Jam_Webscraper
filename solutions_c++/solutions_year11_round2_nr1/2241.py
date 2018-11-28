#include<stdio.h>
void calWP(char mat[100][100], int WPNr[100], int WPDr[100], int N){
	for(int i = 0; i < N; i++){
		int win = 0, loss = 0;
		for(int j = 0; j < N; j++){
			switch(mat[i][j]){
				case '1': win++;
						break;
				case '0': loss++;
						break;
			}
		}
			WPNr[i] = win;
			WPDr[i] = win + loss;
	}
}

void calOWP(char mat[100][100], int WPNr[100], int WPDr[100], double OWP[100], int N){
	for(int i = 0; i < N; i++){
		double sum = 0; int total = 0;
		for(int j = 0; j < N; j++){
			if(mat[i][j] == '1'){
				if(WPDr[j] > 1){
					sum += (WPNr[j]*1.0)/(WPDr[j]-1);
				}
				total++;
			} else if(mat[i][j] == '0'){
				if(WPDr[j] > 1){
					sum += (1.0*WPNr[j]-1)/(WPDr[j]-1);
				}
				total++;
			}
		}
		if(total != 0 ){
			OWP[i] = sum/total;
		}else{
			OWP[i] = 0;
		}
	}
}

void calOOWP(char mat[100][100], double OWP[100], double OOWP[100], int N){
	for(int i = 0; i < N; i++){
		double sum = 0; int total = 0;
		for(int j = 0; j < N; j++){
			if(mat[i][j] == '1' || mat[i][j] == '0'){
				sum += OWP[j];
				total++; 
			}
		}
		if(total != 0){
			OOWP[i] = sum/total;
		}else{
			OOWP[i] = 0;
		}
	}
}
int main(){
int T, cases = 0;
scanf("%d",&T);
while(T--){
	cases++;
	int N;
	scanf("%d",&N);
	char mat[100][100];
	double OWP[100], OOWP[100];
	int WPNr[100], WPDr[100];
	for(int i = 0; i < N; i++){
		scanf("%s", mat[i]);
	}
	calWP(mat, WPNr, WPDr, N);
	calOWP(mat, WPNr, WPDr, OWP, N);
	calOOWP(mat, OWP, OOWP, N);
	printf("Case #%d:\n",cases);
	for(int i = 0; i < N; i++){
		double ans = 0;
		if(WPDr[i] != 0){
			ans += 0.25*((WPNr[i]*1.0)/(WPDr[i]));
		}
		ans += (0.5*OWP[i] + 0.25*OOWP[i]);
		printf("%lf\n", ans);
	}
}
return 0;
}
