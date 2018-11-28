#include <iostream>

using namespace std;

int div(long long a, long long b);

int main(){
	long long T, N, i, j, k, p[10000];
	long long L, H;
	cin >> T;
	for (i=0; i<T; i++){
		cin >> N >> L >>H;
		for(j=0; j<N; j++){
			cin >> p[j];
		}
		if (L==1) {
			printf("Case #%lld: %lld\n", i+1, 1);
			continue;
		}
		for (k=L; k<=H; k++){
			for (j=0; j<N; j++){
				if (div(p[j], k) !=1)	break; 
			}
			if (j==N) {
				printf("Case #%lld: %lld\n", i+1, k);
				break;}
		}
		if (k==H+1) printf("Case #%lld: NO\n", i+1);
	}

	return 0;
}

int div(long long a, long long b){
	int c=0;
	if (a>b) {
		if (a%b==0) c=1;
	}
	else {
		if (b%a ==0) c=1;
	}
	return c;
}