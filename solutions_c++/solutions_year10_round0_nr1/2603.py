#include <stdio.h>
#include <string.h>

using namespace std;

char Binary[100];

int main(){
	int N, K, T, caso = 1 , i, count;
	
	scanf("%d", &T);
	while(T > 0){
		scanf("%d %d", &N, &K);
		memset(Binary, 0, sizeof(Binary));
		i = 0;
		while(K > 0){
			Binary[i++] = K%2;
			K /= 2;
		}
		count = 1;
		for(i = 0; i < N; i++){
			count &= Binary[i];
		}
		if(count != 1)
			printf("Case #%d: OFF\n", caso++);
		else
			printf("Case #%d: ON\n", caso++);
		T--;
	}
	return 0;
}
