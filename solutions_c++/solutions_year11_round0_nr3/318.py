#include <stdio.h>

int T, N;
int nValue[1200];

void Read()
{
	scanf("%d", &N);
	for(int i = 0; i < N; i++)
		scanf("%d", &nValue[i]);
}

void Solve()
{
	int nResult = 0, nSum = 0, nMin;
	nMin = 10000000;
	for(int i = 0; i < N; i++){
		nResult ^= nValue[i];
		nSum += nValue[i];
		if(nMin > nValue[i])
			nMin = nValue[i];
	}
	if(nResult){
		printf("NO\n");
	}else{
		printf("%d\n", nSum-nMin);
	}

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

