// CC.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


// D.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	__int64 T;
	scanf("%d",&T);

	unsigned __int64  N;
	unsigned __int64 C[2000];
	unsigned __int64 M;
	unsigned __int64 S;
   unsigned __int64 X;

	for (int t=1; t<=T; t++)
	{
		//INPUT
		scanf("%d",&N);
		M = 9999999;
		S = 0;
		X = 0;
	    for (int i=1; i<=N; i++)
		{
			scanf("%d",&C[i]);
			if (M>C[i]) M = C[i];
			S += C[i];
			X = X ^ C[i];   
		}

		//printf("M = %d\n",M);
		//printf("S = %d\n",S);

		//OUTPUT
		if (X==0) printf("Case #%d: %d\n",t,S-M);
		else printf("Case #%d: NO\n",t);
	 
	}
	return 0;
}

