#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

int g[105][105];
double WP[105], OWP[105], OOWP[105];
int n;

void calcWP(int ind){
	int win = 0, sh = 0;
	for (int i = 0;i < n;i++){
		if (g[ind][i] == 0){
			sh++;
		}
		if (g[ind][i] == 1){
			win++;
			sh++;
		}
	}
	WP[ind] = win / (sh * 1.0);
}

double calcNWP(int ind, int not){
	int win = 0, sh = 0;
	for (int i = 0;i < n;i++){
		if (g[ind][i] != 2){
			if (i != not){
				if (g[ind][i] == 0){
					sh++;
				}
				if (g[ind][i] == 1){
					win++;
					sh++;
				}
			}
		}
	}
	return (win / (sh * 1.0));
}

void calcOWP(int ind){
	double vsp = 0;
	int sh = 0;
	for (int i = 0;i < n;i++){
		if (g[ind][i] != 2){
			vsp += calcNWP(i, ind);
			sh++;
		}
	}
	OWP[ind] = vsp / (sh * 1.0);
}

void calcOOWP(int ind){
	double sum = 0;
	int sh = 0;
	for (int i = 0;i < n;i++){
		if (g[ind][i] != 2){
			sum += OWP[i];
			sh++;
		}
	}
	OOWP[ind] = (sum / (sh * 1.0));
}

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int test, t, i, j;
	double res;
	char c;
	scanf("%d\n",&test);
	for (t = 0;t < test;t++){
		if (t)
			printf("\n");
		scanf("%d\n",&n);
		for (i = 0;i < n;i++){
			for (j = 0;j < n;j++){
				scanf("%c",&c);
				if (c == '0'){
					g[i][j] = 0;
				}
				if (c == '1'){
					g[i][j] = 1;
				}
				if (c == '.'){
					g[i][j] = 2;
				}
			}
			scanf("\n");
		}
		printf("Case #%d:",t + 1);
		for (i = 0;i < n;i++){
			calcWP(i);
		}
		for (i = 0;i < n;i++){
			calcOWP(i);
		}
		for (i = 0;i < n;i++){
			calcOOWP(i);
		}
		for (i = 0;i < n;i++){
			res = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
			printf("\n%.10lf",res);
		}
	}
	return 0;
}