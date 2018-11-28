#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define REP(var, start, end) for(int var=(start); var<(end); var++)
#define p printf

int buy[512*10];

int m[1024];

int main()
{
	int T=0;
	scanf("%d", &T);
	REP(caseId, 0, T)
	{
		memset(buy, 0, sizeof(buy));
		int P=0;
		scanf("%d", &P);
		REP(mid, 0, 1<<P)
		{
			scanf("%d", &m[mid]);
			//p("%d ", m[mid]);
		}
		//p("\n");
		int dummy;
		REP(pid, 0, P)
		{
			REP(i, 0, 1<<(P-pid-1))
			{
				scanf("%d", &dummy);
				//p("%d ", dummy);
			}
			//p("\n");
		}
		//p("\n");
		
		#define BUY(round, match) buy[(round)*512 +(match)]
		int cost = 0;
		//while(1)
		{
			REP(mid, 0, 1<<P)
			{
				int may_miss = 0;
				REP(round, 0, P)
				{
					int match = mid>>(round+1);
					//p("mid %5d round %3d match %4d\n", mid, round, match);
					if(BUY(round, match)==0) may_miss++;
				}
				REP(round0, 0, P)
				{
					int round = P-1-round0;
					int match = mid>>(round+1);
					if(may_miss>m[mid] && BUY(round, match)==0)
					{
						BUY(round, match)=1; cost++; may_miss--;
						//p("BUY mid %5d round %3d match %4d\n", mid, round, match);
					}
					if(may_miss==m[mid]) break;
				}
			}
		}
		
		p("Case #%d: %d\n", caseId+1, cost);
	}
}
