#include<cstdio>
#include<algorithm>
using namespace std;

double p[4];
double pp[10];

double min(double a1 , double a2){
	if(a1 > a2) return a2;
	return a1;
}

int main(){
	int i , a , b;
	int T;
	freopen("A-small-attempt0.in" , "r" , stdin);
	freopen("A-small-attempt0.out" , "w" , stdout);
	scanf("%d" , &T);
	int q = 1;
	while(T--){
		scanf("%d%d" , &a , &b);
		double res , temp , temp1;
		for(i = 1;i <= a;i++){
			scanf("%lf" , &p[i]);
		}
		printf("Case #%d: " , q++);
		if(a == 1){
			pp[1] = p[1];		
			pp[2] = 1 - p[1];
			res = min((b - a + 1) * pp[1] + (2 * b - a + 2) * pp[2] , b + 2);
			printf("%lf\n" , res);
		}else if(a == 2){
			pp[1] = p[1] * p[2];
			pp[2] = (1 - p[2]) * p[1];
			pp[3] = (1 - p[1]) * p[2];
			pp[4] = (1 - p[1]) * (1 - p[2]);

			temp = ((b - a + 1) * pp[1] + (2 * b - a + 2) * (1 - pp[1]));
			temp1 = ((b - a + 3) * (pp[1] + pp[2]) + (2 * b - a + 4) * (pp[3] + pp[4]));
			res = min(temp , temp1);
			res = min(res , b + 2);
			printf("%lf\n" , res);
		}else{
			pp[1] = p[1] * p[2] * p[3];
			pp[2] = (1 - p[3]) * p[1] * p[2];
			pp[3] = (1 - p[2]) * p[1] * p[3];
			pp[4] = (1 - p[1]) * p[2] * p[3];
			pp[5] = (1 - p[2]) * p[1] * (1 - p[3]);
			pp[6] = (1 - p[1]) * p[2] * (1 - p[3]);
			pp[7] = (1 - p[2]) * p[3] * (1 - p[1]);
			pp[8] = (1 - p[1]) * (1 - p[2]) * (1 - p[3]);
			
			temp = ((b - a + 1) * pp[1] + (2 * b - a + 2) * (1 - pp[1]));
			temp1 = ((b - a + 3) * (pp[1] + pp[2]) + (2 * b - a + 4) * (1 - (pp[1] + pp[2])));
			res = min(temp , temp1);
			temp = ((b - a + 5) * (pp[1] + pp[2] + pp[3] + pp[5]) + (2 * b - a + 6) * (1 - (pp[1] + pp[2] + pp[3] + pp[5])));
			res = min(temp , res);
			res = min(res , b + 2);
			printf("%lf\n" , res);
		}
		
	}


	return 0;
}