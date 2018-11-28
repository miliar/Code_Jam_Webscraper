#include <stdio.h>
#include <string.h>

int T, C, D, N;
char Combine[256][256];
char Opposed[256][256];
char szList[256], szResult[256];

void Read()
{
	char buffer[100];
	//
	scanf("%d", &C);
	memset(Combine, 0, sizeof(Combine));
	for(int i = 0; i < C; i++){
		scanf("%s", buffer);
		Combine[buffer[0]][buffer[1]] = buffer[2];
		Combine[buffer[1]][buffer[0]] = buffer[2];
	}
	//
	scanf("%d", &D);
	memset(Opposed, 0, sizeof(Opposed));
	for(int i = 0; i < D; i++){
		scanf("%s", buffer);
		Opposed[buffer[0]][buffer[1]] = 1;
		Opposed[buffer[1]][buffer[0]] = 1;
	}
	scanf("%d", &N);
	scanf("%s", szList);
}

void Print(int nCount)
{
	bool IsFirst = true;
	printf("[");
	for(int i = 1; i <= nCount; i++){
		if(szResult[i]){
			if(!IsFirst)
				printf(", ");
			IsFirst = false;
			printf("%c", szResult[i]);
		}
	}
	printf("]\n");
}

void Solve()
{
	//n==1;
	int nCnt = 0;
	memset(szResult, 0, sizeof(szResult));
	for(int i = 0; i < N; i++){
		if(Combine[szResult[nCnt]][szList[i]]){
			szResult[nCnt] = Combine[szResult[nCnt]][szList[i]];
		}else{
			int nFlag = 1;
			for(int j = nCnt; j >= 1; j--)
				if(Opposed[szResult[j]][szList[i]]){
					nCnt = 0;
					nFlag = 0;
					break;
				}
			if(nFlag)
				szResult[++nCnt] = szList[i];
		}
	}
	Print(nCnt);
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