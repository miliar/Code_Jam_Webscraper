#include <stdio.h>
int n, m;			//range from n to m
int Recycle[10];				// Store the recycle number for each number between n and m
int GenerateDistinctRecycleNumber(int n);
int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t;			//t cases
	int i,j;		//loop varibles
	int sum;
	scanf("%d", &t);

	for( i = 1; i <= t; i++) {
		scanf("%d %d", &n, &m);
		sum = 0;
		for( j = n; j <= m; j++) {
			sum += GenerateDistinctRecycleNumber(j) - 1;
		}
		//sum = sum / 2;
		printf("Case #%d: %d\n",i,sum);
	}
	return 0;
}

int GenerateDistinctRecycleNumber(int n) {
	int count = 0;				//有多少个符合条件的数
	int i, j, power = 10, nn;
	int digit = 1;
	for(i = 10; n >= i; i = i * 10,digit++);
	Recycle[count++] = n;
	for(int k = 0; k < digit - 1; k++) {
		nn = n % power * (i / power) + n / power;
		if(nn >=n && nn <= m) {
			for(j = 0; j < count; j++)
				if(Recycle[j] == nn)
					break;
			if(j == count)
				Recycle[count++] = nn;
		}
		power *= 10;
	}
	return count;
}