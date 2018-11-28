#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define REP(var, start, end) for(int var=(start); var<(end); var++)
#define p printf

int data[1000*1000];
int nextdata[1000*1000];

int main()
{
	int T=0;
	scanf("%d", &T);
	REP(caseId, 0, T)
	{
		memset(data, 0, sizeof(data));
		#define DATA(x, y) data[(y)*1000 + (x)]
		#define NEXTDATA(x, y) nextdata[(y)*1000 + (x)]
		int mx1=100000, my1=100000, mx2=-100000, my2=-100000;
		int K=0;
		scanf("%d", &K);
		REP(k, 0, K)
		{
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			mx1 = x1 < mx1 ? x1 : mx1;
			my1 = y1 < my1 ? y1 : my1;
			mx2 = x2 < mx2 ? mx2 : x2;
			my2 = y2 < my2 ? my2 : y2;
			REP(x, x1, x2+1)
			REP(y, y1, y2+1)
			{
				DATA(x, y) = 1;
			}
		}
		mx2 += 2;
		my2 += 2;
		int count = 0;
		while(1)
		{
			//p("------------------------------\n");
			//p("Count %d\n", count);
			int live = 0;
			memcpy(nextdata, data, sizeof(data));
			REP(y, my1, my2+1)
			{
				REP(x, mx1, mx2+1)
				{
					if(DATA(x, y)==1)
					{
						if(DATA(x-1, y)==0 && DATA(x, y-1)==0) NEXTDATA(x, y) = 0;
						live++;
					}
					else
					{
						if(DATA(x-1, y)==1 && DATA(x, y-1)==1) NEXTDATA(x, y) = 1;
					}
				}
			}
			memcpy(data, nextdata, sizeof(data));
			//REP(y, my1, my2+1)
			//{
			//	REP(x, mx1, mx2+1)
			//	{
			//		p("%d ", DATA(x, y));
			//	}
			//	p("\n");
			//}
			if(live==0) break;
			count++;
		}
		p("Case #%d: %d\n", caseId+1, count);
	}
}
