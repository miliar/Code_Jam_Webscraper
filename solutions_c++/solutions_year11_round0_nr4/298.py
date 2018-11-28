#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int N;
 double fat[1010],f[1010];
int val[1010];
void process(){
	scanf("%d", &N);
	
	for(int i = 1; i <= N; i++){
		scanf("%d", &val[i]);
	}
	double sum = 0;
	for(int i = 1; i <= N; i++){
		if(val[i] != -1){
			int next = val[i], next2;
			int at = 1;
			val[i] = -1;
			
			while(val[next] != -1){
				next2 = val[next];
				val[next] = -1;
				next = next2;
				at++;
			}
			sum += f[at];
		}
	}
	printf("%.6lf", sum);
}

int main(){
	
	int casos;
	
	scanf("%d", &casos);
	
	f[1] = 0;
	
	for(int i = 2; i <= 1000; i++){
		double sum = 1;
		for(int j = 1; j < i; j++){
			sum += (f[j]/j);
		}
		f[i] = sum/(1 - 1.0/i);
	}
	
	for(int i = 1; i <= casos; i++){
		printf("Case #%d: ", i);
		process();
		printf("\n");
	}
	
	return 0;
}
