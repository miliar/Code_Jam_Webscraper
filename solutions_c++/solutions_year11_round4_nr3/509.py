#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define N 50000
long mark[N];
long p[N];
void prime( long n ){
	int num = 0, i, j;
	memset( mark, 0, sizeof( mark ) );
	for( i = 2; i <= n; i ++ ){
		if( !mark[i] ) {
			p[num++] = i;
			mark[i] = i;
		}
		for( j = 0; j < num && i*p[j] < n; j ++ ){
			mark[i*p[j]] = p[j];
			if( i%p[j] == 0 ) break;
		}
	}
}

int time[N];
int main(){
	int test, t;
	int n;
	int a, b, mul;
	int temp;
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	prime(N-1);
	scanf("%d", &test);
	for(t=1; t<=test; t++){
		printf("Case #%d: ", t);
		scanf("%d", &n);
		a = 0;
		b = 0;
		mul = 1;
		memset(time, 0, sizeof(time));
		for(int i=0; p[i]<=n; i++){
			temp = n;
			while(temp >= p[i]){
				temp /= p[i];
				a ++;
				if(mul * p[i] > n){
					b ++;
					mul = p[i];
				}
				else
					mul *= p[i];
			}
		}
		printf("%d\n", a-b);
	}
	return 0;
}