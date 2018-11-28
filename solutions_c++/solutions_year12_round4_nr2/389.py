#include<stdio.h>
#include<stdlib.h>

#define MAX(a,b) (a)>(b)?(a):(b)
#define MIN(a,b) (a)<(b)?(a):(b)

int rad[2000];
int X[2000];
int Y[2000];

int dummy[2000];

int N,W,L;

int comparerad(const void* left, const void* right)
{
	return - rad[*((int*)left)] + rad[*((int*)right)];
}

int main()
{
	int T;

	FILE* fin = fopen("input.txt", "r");
	FILE* fout = fopen("output.txt","w");

	fscanf(fin, "%d\n", &T);

	// 정사각형으로 놓고 해도 충분할것이다.
	// 그러니까 각 사람이 차지하는 공간을 정사각형으로 간주하고,
	// 큰 정사각형부터 시작한다.
	// 0,0부터, 오른쪽으로 움직이면서 채우기 시작한다.
	// 왼쪽은 꽉 막힐 위험이 있다. 따라서 왼쪽 최소값을 잡아둔다.
	
	for(int i = 1; i <= T; i++)
	{
		for(int i = 0; i < 2000; i++)
			dummy[i] = i;

		fscanf(fin, "%d%d%d\n", &N, &W, &L);

		int curX = 0;
		int right = 1; // 오른쪽으로 움직이는가(1) 왼쪽으로 움직이는가(-1)

		int llimit = 0; // 왼쪽 최소값

		for(int j = 0; j < N; j++)
			fscanf(fin, "%d", rad + j);
		rad[N] = 0;

		// 소트한다.
		qsort(dummy, N, sizeof(int), comparerad);

		for(int j = 0; j < N; j++)
		{
			if(curX != 0 && curX != W)	// 외각은 벗어날 수 있다.
			{
				curX += right * rad[dummy[j]];
				if(curX > W)
				{
					curX = W;
					right = -1;
				}
				else if(curX < llimit)
				{
					curX = llimit;
					right = 1;
				}
			}

			X[dummy[j]] = curX;
			Y[dummy[j]] = 0;
			for(int k = 0; k < j; k++)
			{
				if(X[dummy[k]] + rad[dummy[k]] + rad[dummy[j]] > curX && X[dummy[k]] - rad[dummy[k]] - rad[dummy[j]] < curX)
				{
					Y[dummy[j]] = MAX(Y[dummy[j]], Y[dummy[k]] + rad[dummy[k]] + rad[dummy[j]]);
				}
			}
			if(Y[dummy[j]] + rad[dummy[j]] > L)
			{
				llimit = rad[dummy[j]] + X[dummy[j]];
			}
			curX += right * rad[dummy[j]];
			if(curX > W)
			{
				curX = W;
				right = -1;
			}
			else if(curX < llimit)
			{
				curX = llimit;
				right = 1;
			}
		}

		fprintf(fout,"Case #%d:", i);
		for(int j = 0; j < N; j++)
			fprintf(fout, " %d %d", X[j], Y[j]);
		fprintf(fout, "\n");
	}
	return 0;
}
