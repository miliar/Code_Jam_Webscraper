#include<cstdio>

long potegi[32];

int main(){
	potegi[0] = 1;
	for(long i = 1; i < 31; i++){
		potegi[i] = potegi[i - 1] * 2;
	}

	long ilosc, N, K;
	scanf("%ld", &ilosc);

	for(long i = 1; i <= ilosc; i++){
		scanf("%ld %ld", &N, &K);
		K %= potegi[N];
		if(K == potegi[N] - 1)
			printf("Case #%ld: ON\n", i);
		else
			printf("Case #%ld: OFF\n", i);
	}


	return 0;
}
