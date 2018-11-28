#include <stdio.h>

int n;
int pos1, time1, pos2, time2;

int iabs (int a) {return a<0? -a: a;}

int main ()
{
	int t, ct = 0;

	for (scanf ("%d", &t); t > 0; t --)
	{
		pos1 = pos2 = 1;
		time1 = time2 = 0;

		scanf ("%d", &n);
		for (int i = 0; i < n; i ++)
		{
			char who;

			do scanf ("%c", &who);
				while (who <= ' ');

			int pos;

			scanf ("%d", &pos);

			if (who == 'O')
			{
				time1 += iabs (pos - pos1) + 1;
				if (time1 <= time2) time1 = time2 + 1;
				pos1 = pos;
			}
			else
			{
				time2 += iabs (pos - pos2) + 1;
				if (time2 <= time1) time2 = time1 + 1;
				pos2 = pos;
			}
		}

		printf ("Case #%d: %d\n", ++ ct, time1 > time2? time1 : time2);
	}

	return 0;
}
