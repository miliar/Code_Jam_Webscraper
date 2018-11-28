#include<stdio.h>

int CountPair(int A, int B);
int SpitNum(int N, int Num[]);
int MoveNDigitToEnd(int Num[], int N, int Digit);
int FindPairs(int Num[], int Digit, int A, int B, int N);
void StoreM(int ArrM[],int* CntM, int M);
int IsMExist(int ArrM[],int CntM, int M);

int main()
{
	freopen("E://C-small-attempt0.in", "r", stdin);
	freopen("D://Downloads//myout.out", "w", stdout);
	int T;
	int i;
	int A,B;

	scanf("%d", &T);
	for (i=0; i<T; i++)
	{
		scanf("%d%d", &A, &B);
		printf("Case #%d: %d\n", i + 1, CountPair(A, B));
	}
	return 0;
}

int CountPair(int A, int B)
{
	int Num[10];
	int i,j;
	int Digit;
	int Result = 0;

	for (i=A; i<=B; i++)
	{
		Digit = SpitNum(i, Num);
		Result += FindPairs(Num, Digit, A, B, i);
	}

	return Result;
}

int  SpitNum(int N, int Num[])
{
	int Digit = 0;

	while(N)
	{
		Num[Digit++] = N % 10;
		N /= 10;
	}

	return Digit;
}

int FindPairs(int Num[], int Digit, int A, int B, int N)
{
	int i,j;
	int M;
	int Cnt = 0;
	int ArrM[50];
	int CntM = 0;

	if (Digit == 1)
	{
		return 0;
	}

	for (i=1; i<Digit; i++)
	{
		M = MoveNDigitToEnd(Num, i, Digit);
		
		if (IsMExist(ArrM, CntM, M))
		{
			continue;
		}
		else
		{
			StoreM(ArrM, &CntM, M);
		}
		//printf("%d\n", M);
		if (M > N && M <=B)
		{
			Cnt ++;
		}
	}
	return Cnt;
}

int MoveNDigitToEnd(int Num[], int N, int Digit)
{
	int i;
	int M = 0;

	for (i=Digit - 1 - N; i>=0; i--)
	{
		M = M * 10 + Num[i];
	}

	for (i=Digit - 1; i > Digit - 1 - N; i--)
	{
		M = M * 10 + Num[i];
	}

	return M;
}

void StoreM(int ArrM[],int* CntM, int M)
{
	ArrM[*CntM] = M;
	(*CntM)++;
}

int IsMExist(int ArrM[],int CntM, int M)
{
	int i;

	for (i=0; i<CntM; i++)
	{
		if (ArrM[i] == M)
		{
			return 1;
		}
	}
	return 0;
}