#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
using namespace std;

int main()
{
	int T,ca;
	cin >> T;
	for(ca=1; ca <= T; ca++)
	{
		int count;
		cin >> count;
		int step;
		int last_side, pos[2];
		pos[0] = pos[1] = 1;
		last_side = -1;
		int total = 0;
		int last = 0;
		for(step=0; step < count; step++)
		{
			char a; int side;
			int target;
			cin >> a >> target;
			if (a == 'O') side = 0; else side=1;
			int move_time = abs(target - pos[side]);
			pos[side] = target;
			int realtime = 0;
			if (side != last_side)
			{
				realtime = move_time - min(move_time, last);
				last = 0; last_side = side;
			}
			else
				realtime = move_time;
			realtime++;
			total += realtime;
			last += realtime;
		}
		printf("Case #%d: %d\n", ca, total);
	}
}
