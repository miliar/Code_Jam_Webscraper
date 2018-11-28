// gcj.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"
#include "stdio.h"
#include "stdlib.h"

int snapproc(int socketsize, int snapcount)
{
	int snapstate[1024];
	int powerindex = -1;

	// initialize
	for(int i = 0; i < socketsize; i++)
		snapstate[i] = 0;

	// start snap
	for(int i = 0; i < snapcount; i++)
	{
		// calc power index
		powerindex = socketsize - 1;
		for(int j = 0; j < socketsize; j++)
		{
			if(snapstate[j] == 0)
			{
				powerindex = j;
				break;
			}
		}

		// do snap
		for(int j = 0; j <= powerindex; j++)
			snapstate[j] = ( snapstate[j] == 0 ) ? 1 : 0;

//		printf("#%d ---\n", i);
//		for(int j = 0; j < socketsize; j++)
//			printf("  %d: %d\n", j, snapstate[j]);
	}

	// check light power
	int light_power = 1;
	for(int j = 0; j < socketsize; j++)
	{
		if(snapstate[j] == 0)
		{
			light_power = 0;
			break;
		}
	}

	return light_power;

}


void input_file()
{
	FILE* fp = fopen("c:\\temp\\input.txt", "r");
	if(fp==NULL)
	{
		return;
	}

	char buf[30000];
	fgets(buf, 30000, fp);
	int testsize = atoi(buf);
//	printf("%d\n", testsize);

	FILE* outfp = fopen("c:\\temp\\output.txt", "w");
	for(int i=0; i<testsize; i++)
	{
		int ss, sc;
		fscanf(fp, "%d %d", &ss, &sc);
//		printf("%d %d\n", ss, sc);

		int power = snapproc(ss, sc);

		fprintf(outfp, "Case #%d: %s\n", i+1, power ? "ON" : "OFF");
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	input_file();

	return 0;
}
