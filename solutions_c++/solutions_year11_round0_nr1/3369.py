
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

struct btn
{
	int pos, time;

	btn(int pos=0, int time=0): pos(pos), time(time) {}
};

#define MAX 128

btn ora[MAX], blu[MAX];

int main(void)
{
	int nc;

	scanf("%d", &nc);
	for(int ca=1; ca<=nc; ca++)
	{
		printf("Case #%d: ", ca);
		//--------------------

		int n, no=0, nb=0;

		scanf("%d", &n);
		for(int i=0; i<n; i++)
		{
			char c;
			int x;

			scanf(" %c %d", &c, &x);

			if(c == 'O')
				ora[no++] = btn(x, i);
			else
				blu[nb++] = btn(x, i);
		}

//		for(int i=0; i<no; i++) printf("O pos=%d time=%d\n", ora[i].pos, ora[i].time);
//		for(int i=0; i<nb; i++) printf("B pos=%d time=%d\n", blu[i].pos, blu[i].time);
		fflush(stdout);

		int ap=0, t=0;
		int po=1, pb=1;
		int to=0, tb=0;
		int ns;
		for(ns=0; ap < n; ns++)
		{
			//printf("ap=%d t=%d po=%d pb=%d to=%d tb=%d ns=%d\n", ap,t, po,pb, to,tb, ns);

			int apagora = 0;

			if(to < no)
			{
				if(po < ora[to].pos)
					po++;
				else if(po > ora[to].pos)
					po--;
				else if(ora[to].time == t)
				{
					to++;
					t++;
					ap++;

					apagora = 1;
				}
			}

			if(tb < nb)
			{
				if(pb < blu[tb].pos)
					pb++;
				else if(pb > blu[tb].pos)
					pb--;
				else if(blu[tb].time == t && !apagora)
				{
					tb++;
					t++;
					ap++;
				}
			}
		}

		printf("%d\n", ns);
	}

	return 0;
}
