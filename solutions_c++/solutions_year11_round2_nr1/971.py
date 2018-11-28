#include <stdio.h>

char teams[100][101];
int match[100], won[100];
double wp[100], owp[100], oowp[100];
void solve(){
	int i,j,k,n;
	double sum;
	scanf("%d", &n);
	for(i=0;i<n;i++)
		scanf("%s", teams[i]);
	for(i=0;i<n;i++){
		match[i]=0;
		won[i]=0;
		for(j=0;j<n;j++){
			if(teams[i][j] != '.')
				match[i]++;
			if(teams[i][j] == '1')
				won[i]++;
		}
		wp[i] = (double)won[i]/(double)match[i];
	}
	for(i=0;i<n;i++){
		sum = 0.0;
		for(j=0;j<n;j++){
			if(teams[i][j] == '0')
				sum += (double)(won[j]-1)/(double)(match[j]-1);
			else if(teams[i][j] == '1')
				sum += (double) won[j] / (double)(match[j]-1);
		}
		owp[i] = sum/(double)match[i];
	}
	for(i=0;i<n;i++){
		sum=0;
		for(j=0;j<n;j++){
			if(teams[i][j]!='.')
				sum += owp[j];
		}
		oowp[i] = sum/(double)match[i];
	}
	for(i=0;i<n;i++)
		printf("%.10lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
}
int main(){
	int i, T;
	scanf("%d", &T);
	for(i=0;i<T;i++){
		printf("Case #%d: \n", i+1);
		solve();
	}
	return 0;
}
