

#include "stdafx.h"
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <map>
#include <vector>
#include <queue>
using namespace std;


int ms[1050];

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t,n,k;
	int p;
	scanf("%d",&t);
	for(int x=1;x<=t;++x)
	{
		scanf("%d",&p);
		int num = (1<<p);
		for(int i=0;i<num;++i)
			scanf("%d",&ms[i]);
		for(int i=0;i<num;++i)
			ms[i] = p-ms[i];
		int tp;
		for(int i=0;i<num-1;++i)
			scanf("%d",&tp);
		int out = 0;
		for(int i=1;i<=p;++i)
		{
			int duan = num/((int)pow(2.0,i-1));
			for(int bb = 0;bb<num;bb+=duan)
			{
				bool don = false;
				for(int f = bb;f<bb+duan;++f)
				{
					if(ms[f] > 0)
					{
						don = true; break;
					}
				}
				if(don)
				{
					out++;
					for(int f = bb;f<bb+duan;++f)
					{
						if(ms[f] > 0)
						{
							ms[f] --;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n",x,out);
	}
	return 0;
}

