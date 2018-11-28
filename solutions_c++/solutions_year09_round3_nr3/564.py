#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INFILE "C-small-attempt0.in"
#define OUTFILE "C-small-attempt0.out"

#define maxQ 5


typedef struct _node {
	char id[maxQ+1];
	int cost;
} node_t;

node_t value[maxQ+1][120];

int P, Q;

int dp(int *cell, int *rls, int rlsCnt)
{
	if (rlsCnt == 0)
		return 0;
	int curCell[104];	
	int curRls[5];
	// memcpy(curRls, rls, 5*4);
	
	int minCost = 100*5;
	for (int i = 0; i < rlsCnt; i++) {
		memcpy(curCell, cell, 104*4);
		int thisCost = 0;
		for (int j = rls[i]-1; (j >= 1) && (cell[j] == 1); j--)
			thisCost++;
		for (int j = rls[i]+1; (j <= P) && (cell[j] == 1); j++)
			thisCost++;
		for (int j = 0, k=0; j < rlsCnt; j++) {
			if (j != i) {
				curRls[k] = rls[j]; k++;
			}
		}
		curCell[rls[i]] = 0;
		thisCost = thisCost + dp(curCell, curRls, rlsCnt-1);
		if (thisCost < minCost)
			minCost = thisCost;
	}
	return minCost;
}

int main()
{
	FILE *fpIn = freopen(INFILE, "r", stdin);
	FILE *fpOut = fopen(OUTFILE, "w");

	int N;
	scanf("%d", &N);
	for (int cnt1 = 0; cnt1 < N; cnt1++) {		
		scanf("%d %d", &P, &Q);
		int cell[104];
		for (int i = 0; i < 104; i++)
			cell[i] = 1;
		int rls[5];
		for (int i = 0; i < Q; i++)
			scanf("%d", &rls[i]);
		int res = dp(cell, rls, Q);
		fprintf(fpOut, "Case #%d: %d\n", cnt1+1, res);
	}
	fclose(fpIn);
	fclose(fpOut);
}