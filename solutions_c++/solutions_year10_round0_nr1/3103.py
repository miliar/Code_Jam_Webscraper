// CodeJam2010-1.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"



bool IsOn(unsigned int n,
		  unsigned int k)
{
	unsigned int state = 0;

	for(unsigned int i = 0; i < k; ++i) state = ( state & (state+1) ) + (~state & (-~state));

	return ((1 << n ) - 1 &  state) == (1 << n ) - 1;
}

int main(int argc, char* argv[])
{

	FILE* fp = fopen(argv[1], "r");

	int count = 0;
	fscanf(fp, "%d", &count);

	for(int i = 0; i < count; ++i)
	{
		unsigned int n, k;
		fscanf(fp, "%u %u\n", &n, &k);
		printf("Case #%u: %s\n", i+1, IsOn(n, k) ? "ON" : "OFF");
	}

	fclose(fp);

	return 0;
}

