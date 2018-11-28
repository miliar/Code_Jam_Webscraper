#include <iostream>
#include <algorithm>
#include <queue>
#define MAXN 1000

using namespace std;

struct Nod 
{
	int timeStart, timeEnd, num;
	Nod () {}
	Nod ( int timeStart, int timeEnd, int num ):
	timeStart(timeStart), timeEnd(timeEnd), num(num) {}
};


bool cmp ( Nod a, Nod b )
{
	if ( a.timeStart == b.timeStart )
		return a.timeEnd < b.timeEnd;
	return a.timeStart < b.timeStart;
}

priority_queue <int,vector<int>,greater<int>> Q[2];

int main (void)
{
	int T, n, i;
	freopen("B-large.in","r",stdin);
	freopen("BB.out","w",stdout);
	scanf ("%d",&T);
	int st1, st2, ed1, ed2;
	Nod Time[MAXN];
	int Start, End;
	int Case = 0;
	while ( T -- )
	{
		Case ++;
		scanf ("%d",&n);
		int k = 0;
		int nA, nB;
		scanf ("%d%d",&nA,&nB);
		for ( i = 0 ; i < nA; i ++ )
		{
			scanf ("%d:%d %d:%d",&st1,&st2,&ed1,&ed2);
			Start = st1*60+st2;
			End = ed1*60+ed2;
			Time[k++] = Nod (Start,End,0);
		}
		for ( i = 0 ; i < nB; i ++ )
		{
			scanf ("%d:%d %d:%d",&st1,&st2,&ed1,&ed2);
			Start = st1*60+st2;
			End = ed1*60+ed2;
			Time[k++] = Nod (Start, End,1);
		}
		sort (&Time[0],&Time[k],cmp);
		while ( !Q[0].empty() )
			Q[0].pop();
		while ( !Q[1].empty() )
			Q[1].pop();
		int num[2] = {0};
		for ( i = 0 ; i < nA + nB; i ++ )
		{
			if ( Q[Time[i].num].empty() )
			{
				num[Time[i].num] ++;
				Q[1-Time[i].num].push(Time[i].timeEnd+n);
			}
			else
			{
				int temp = Q[Time[i].num].top();
				if ( temp <= Time[i].timeStart )
				{
					Q[Time[i].num].pop();
					Q[1-Time[i].num].push(Time[i].timeEnd+n);
				}
				else
				{
					num[Time[i].num] ++;
					Q[1-Time[i].num].push(Time[i].timeEnd+n);
				}
			}
		}
		printf ("Case #%d: %d %d\n",Case,num[0],num[1]);
	}
	return 0;
}