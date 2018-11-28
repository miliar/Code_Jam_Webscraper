
#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

double maxi(double a, double b){
	if(a > b) 
		return a;
	return b;
}

double mini(double a, double b){
	if(a < b)
		return a;
	return b;
}

double xx(double a){
	return a*a;
}

double dis(int *a, int *b){
	return (sqrt((double)xx(a[0]-b[0]) + xx(a[1]-b[1]))+a[2]+b[2])/2;
}

int main(){
	
	int T; cin >> T;
	
	int s[40][3];

	for(int testcase=1; testcase<=T; ++testcase){
		
		int N; cin >> N; 
		
		for(int i=0; i<N; ++i){
			for(int j=0; j<3; ++j){
				cin >> s[i][j];
			}
		}

		double ans = 0.0;
		double dis1, dis2, dis3;

		if(N == 1){
			ans = s[0][2];
		}else if(N == 2){
			ans = maxi(s[0][2], s[1][2]);
		}else if(N == 3){
			dis1 = maxi(dis(s[0], s[1]), s[2][2]);
			dis2 = maxi(dis(s[1], s[2]), s[0][2]);
			dis3 = maxi(dis(s[0], s[2]), s[1][2]);
			ans = mini(dis1, mini(dis2, dis3));
		}else{
			ans = -1;
		}
		printf("Case #%d: %.10lf\n", testcase, ans);
	}

	return 0;
}
