#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char data[2000000+1];
void process()
{
	int a, b, i;
	int j, k, tmp;
	int result;
	int totalcount = 0;

	scanf("%d %d", &a, &b);
	for(i=a; i<b; i++) {
		j = 1000000;
		k = -1;
		memset(data,0, sizeof(char)*2000001);
		while(j != 1) {
			if( i/j == 0 ) {
				j/=10;
				continue;
			}
			if( k == -1 ) k=10;
			tmp = i/j;
			result = i%j;
			result *=k;
			result += tmp;
			if( data[result] == 0 && result > i && result <= b ) {
				data[result] = 1;
				totalcount ++;
			}
			j/=10;
			k*=10;
		}
	}
	printf("%d\n", totalcount);

}
int main()
{
	int i, n;
	freopen("input.txt","r", stdin);
	freopen("ouptut.txt","w", stdout);
	scanf("%d", &n);
	for(i=0; i<n; i++) {
		printf("Case #%d: ", i+1);
		process();
	}
	return 0;
}