#include <cstdio>

char map[101][101];
int cntone[101];
double one[101];
double two[101];
double three[101];

void newprob(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		cntone[i] = 0;
		one[i] = 0.0;
		two[i] = 0.0;
		three[i] = 0.0;
	}
	for(int i=0;i<n;i++){
		scanf("%s",map[i]);
		for(int j=0;j<n;j++){
			if(map[i][j] != '.'){
				cntone[i]++;
			}
			one[i] += (double)(map[i][j] == '1');
		}
	}
	for(int i=0;i<n;i++){
		// we will calc $i OWP
		int cnt = 0;
		for(int j=0;j<n;j++){
			if(map[i][j] == '.')continue;
			cnt++;
			if(map[i][j] == '0'){
				two[i] += (one[j] - 1.0) / (double)(cntone[j] - 1);
			}else{
				two[i] += (one[j]) / (double)(cntone[j] - 1);
			}
		}
		two[i] /= (double)cnt;
	}
	for(int i=0;i<n;i++){
		int cnt = 0;
		for(int j=0;j<n;j++){
			if(map[i][j] == '.')continue;
			cnt++;
			three[i] += two[j];
		}
		three[i] /= (double)cnt;
	}
	for(int i=0;i<n;i++){
		printf("%lf\n",0.25 * (one[i]/(double)cntone[i]) + 0.5 * two[i] + 0.25 * three[i]);
	}
}

int main(){
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		printf("Case #%d:\n",i+1);
		newprob();
	}
	return 0;
}
