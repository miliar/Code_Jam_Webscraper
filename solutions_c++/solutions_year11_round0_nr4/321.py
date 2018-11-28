#include <stdio.h>
#include <string.h>

int T, N;
int nArray[1200];

void Read()
{
	scanf("%d", &N);
	for(int i = 0; i < N; i++){
		scanf("%d", &nArray[i]);
		nArray[i]--;
	}
}

void Solve()
{
	int nResult = 0;
	for(int i = 0; i < N; i++){
		if(nArray[i] != i){
			nResult++;
		}
	}
	printf("%d.000000\n", nResult);
}


int main()
{
	scanf("%d", &T);
	for(int i = 0; i < T; i++){
		Read();
		printf("Case #%d: ", i+1);
		Solve();
	}
	return 0;
}