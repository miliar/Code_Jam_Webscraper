// gcj1.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include "stdafx.h"


#include <stdio.h>

int snapper_chain(int argc, char* argv[])
{
	FILE* fpi = stdin;
	FILE* fpo = stdout;

	int T;
	if (1 != fscanf(fpi, "%d\n", &T))
		return -1;

	for(int icase=0; icase<T; icase++)
	{
		int N, K;
		if ( 2 != fscanf(fpi, "%d %d\n", &N, &K) )
			return -1;

		int o=0;

		int mask = (1<<N)-1;
		o = ((mask & K) == mask);
		//printf("N=%d, K=%d(0x%x), mask=%d(%x), k&mask=%x\n", N,K,K,mask,mask,K&mask);

		fprintf(fpo, "Case #%d: %s\n", icase+1, ( o ? "ON":"OFF"));
	}

	fclose(fpi);
	fclose(fpo);

	return 0;
}
