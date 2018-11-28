#include <stdio.h>
#include <string.h>

int N, L, H;
int Array[200000];

void Read()
{
	scanf("%d %d %d", &N, &L, &H);
	for(int i = 0; i < N; i++)
		scanf("%d", &Array[i]);
}

void Solve()
{
	int nResult = 0;
	for(int i = L; i <= H; i++){
		int j = 0;
		for(j = 0; j < N; j++){
			if(i % Array[j] == 0) continue;
			if(Array[j] % i == 0) continue;
			break;
		}
		if(j == N){
			printf("%d\n", i);
			return ;
		}
	}
	printf("NO\n");
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		Read();
		printf("Case #%d: ", i);
		Solve();
	}
}
