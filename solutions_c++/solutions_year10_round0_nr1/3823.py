// testlog.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "conio.h"
#include "math.h"

int _tmain(int argc, _TCHAR* argv[])
{
	long unsigned int N,K;
	int T,allOn;

	freopen("A-large.in","r",stdin);
	freopen("Output.out","w",stdout);
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		scanf("%d%d",&N,&K);
		allOn = (pow(2,(double)N) - 1);

		if((int)(K + 1) % (allOn + 1) == 0)
		{
			printf("Case #%d: ON\n",i);
		}
		else
		{
			printf("Case #%d: OFF\n",i);
		}
	}
	

	return 0;
}


