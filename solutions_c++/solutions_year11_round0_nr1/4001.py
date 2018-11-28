// bots.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int N;


int ver(int x)
{
	return x > 0 ? x : 0;
}

int abs(int x)
{
	return x > 0 ? x : -x;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("bots.in","r",stdin);
	freopen("bots.out","w",stdout);
	int nrt;
	scanf("%d\n",&nrt);

	for(int x = 1;x <= nrt;++x)
	{
		int curtime = 0,time1 = 0,time2 = 0,poz1 = 1,poz2 = 1;
		scanf("%d\n",&N);
		for(int i = 0;i < N; ++i)
		{
			char c;
			int p;
			scanf("%c %d\n",&c,&p);
			if (c == 'O')
			{
				curtime += ver(abs(p - poz1) - (curtime - time1)) + 1;
				time1 = curtime;
				poz1 = p;
			}
			if (c == 'B')
			{
				curtime += ver(abs(p - poz2) - (curtime - time2)) + 1;
				time2 = curtime;
				poz2 = p;
			}
		}
		printf("Case #%d: %d\n",x,curtime);
		
	}

	return 0;
}

