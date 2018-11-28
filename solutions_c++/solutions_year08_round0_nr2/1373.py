#include <stdio.h>
#include <string.h>
#include <queue>

using namespace std;

class TimeTable 
{
public:
	int dhour, dminute;
	int ahour, aminute;
	int pos, type;

	TimeTable()
	{}
	TimeTable(int h, int m, int at)
	{
		dhour = h;
		dminute = m;
		pos = at;
		type = 0;
	}
	
	TimeTable(int dh, int dm, int ah, int am, int at)
	{
		dhour = dh;
		dminute = dm;
		ahour = ah;
		aminute = am;
		pos = at;
		type = 1;
	}
	
	bool operator< (const TimeTable& ob) const
	{
		return (dhour>ob.dhour) || ((dhour==ob.dhour) && (dminute>ob.dminute))
		       || (dhour==ob.dhour && dminute==ob.dminute && type > ob.type);
	}
};

int main(void)
{
	int N, T, NA, NB;
	int a, b, c, d;
	int dhour, dminute, ahour, aminute;
	int value;
	int avail[2];
	int require[2], pos;

	priority_queue<TimeTable> Q;
	TimeTable k;
	

	scanf("%d", &N);
	
	for(a=1; a<=N; a++)
	{
		avail[0] = avail[1] = 0;
		require[0] = require[1] = 0;

		scanf("%d", &T);
		scanf("%d %d", &NA, &NB);
		for(b=0; b<NA; b++)
		{
			scanf("%d:%d", &dhour, &dminute);
			scanf("%d:%d", &ahour, &aminute);
			Q.push(TimeTable(dhour, dminute, ahour, aminute, 0));
		}
		
		for(b=0; b<NB; b++)
		{
			scanf("%d:%d", &dhour, &dminute);
			scanf("%d:%d", &ahour, &aminute);
			Q.push(TimeTable(dhour, dminute, ahour, aminute, 1));
		}


		while( !Q.empty() )
		{
			k = Q.top();
			Q.pop();

			pos = k.pos;
			if(k.type == 1)	// Depart
			{
				if(avail[pos]>0)
				{
					avail[pos]--;
				}
				else
				{
					require[pos]++;
				}
				ahour = k.ahour;
				aminute = k.aminute+T;
				ahour += aminute/60;
				aminute %= 60;
				Q.push(TimeTable(ahour, aminute, !pos));
			}
			else
			{
				avail[pos]++;
			}
		}
		
		printf("Case #%d: %d %d\n", a, require[0], require[1]);
	}
}

