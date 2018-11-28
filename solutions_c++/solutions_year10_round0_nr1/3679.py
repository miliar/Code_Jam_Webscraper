// SnapperChain.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fp = fopen("input.txt", "r");
	
	int nCase;
	fscanf(fp, "%d", &nCase);
	int *nSnapper = (int *)calloc(sizeof(int), nCase);
	int *nSnapped = (int *)calloc(sizeof(int), nCase);

	for(int i = 0; i < nCase; i++)
	{
		fscanf(fp, "%d %d", &nSnapper[i], &nSnapped[i]);
	}

	fclose(fp);

	fp = fopen("output.txt", "w");
	for(int i = 0; i < nCase; i++)
	{
		//printf("%d %d\n", nSnapper[i], nSnapped[i]);
		int m = 1 << nSnapper[i];
		int x = nSnapped[i] - (m - 1);

		int flag = 0;
		if(!x)
			flag = 1;
		else if(x < 0)
			flag = 0;
		else if(x > 0 && x%m == 0)
			flag = 1;

		fprintf(fp, "Case #%d: %s\n", i+1, flag ? "ON" : "OFF");
		printf("Case #%d: %s\n", i+1, flag ? "ON" : "OFF");
	}
	fclose(fp);

	free(nSnapper);
	free(nSnapped);
	return 0;
}

