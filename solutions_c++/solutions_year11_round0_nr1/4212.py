#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

typedef pair< unsigned, unsigned > btn_t;

typedef vector< pair<unsigned, unsigned > > sequence_t;

#define ORANGE 0
#define BLUE 1

#define ORANGE_C 'O'
#define BLUE_C 	 'B'
#ifdef KDEBUG
#define DPRINT(x) printf("%s", x )
#define VAL(x) cout << "value " << #x << " = " << x << endl;
#else
#define DPRINT(x) ;
#define VAL(x) ;
#endif


void solve( unsigned case_no, sequence_t &so, sequence_t &sb)
{
	int vpos_o=0;
	int vpos_b=0;
	int pos_o = 1;
	int pos_b = 1;
	int result = 0;

	bool blue_out = false;
	bool orange_out = false;
/*
	for (int i = 0;i < so.size();++i)
	{
		printf("[ %d %d]", so[i].first, so[i].second);
	}
	printf("\n");

	for (int i = 0;i < sb.size();++i)
	{
		printf("[ %d %d]", sb[i].first, sb[i].second);
	}
	printf("\n");
*/
	if (vpos_o >= so.size()) orange_out = true;
	if (vpos_b >= sb.size()) blue_out = true;

	while ( !blue_out || !orange_out)
	{
		// FIRST, determine next target
		int target = -1;
		if (orange_out) target = BLUE;
		else if (blue_out) target = ORANGE;
		else
			if ( so[vpos_o].first < sb[vpos_b].first) 
				target = ORANGE;
			else {
				target = BLUE;
			}

		int steps = 0; // number of steps done while reaching this target

		switch(target)
		{
			case	ORANGE:
			{
				DPRINT("ORANGE TARGET");
				// we have to reach orange, in the meantime we 
				// will shorten distance to blue
				steps = pos_o - so[vpos_o].second; // go to the button
				if (steps < 0 ) steps*=-1;
				++steps; // hit the button
				VAL(pos_o);
				VAL(so[vpos_o].second);
				VAL(vpos_o);

				VAL(steps);

				pos_o = so[vpos_o].second; // update robot position
				vpos_o++;  // increase vector pos
				
				// now we have to deal with Blue 
				if (!blue_out)
				{
					int blue_distance = sb[vpos_b].second - pos_b;
					int sign = 1;
					if (blue_distance < 0 )  {
						sign = -1;
						blue_distance *= -1;
					}
					if (blue_distance > steps ) 
					{
						pos_b += steps * sign;
						VAL(pos_b);

					}
					else pos_b = sb[vpos_b].second;
				}
			}
			break;
			case	BLUE:
			{
		// we have to reach orange, in the meantime we 
				// will shorten distance to blue
				DPRINT("BLUE TARGET");
				steps = pos_b - sb[vpos_b].second; // go to the button
				VAL(pos_b);
				VAL(sb[vpos_b].second);
				VAL(vpos_b);
				if (steps < 0 ) steps*=-1;
				++steps; // hit the button
				VAL(steps);

				pos_b = sb[vpos_b].second; // update robot position
				vpos_b++;  // increase vector pos
				
				// now we have to deal with Blue 
				if (!orange_out)
				{
					int orange_distance = so[vpos_o].second - pos_o;
					int sign = 1;
					if (orange_distance < 0 )  {
						sign = -1;
						orange_distance *= -1;
					}
					if (orange_distance > steps ) 
					{

						pos_o += steps * sign;
						VAL(pos_o);

					}
					else pos_o = so[vpos_o].second;
				}

			}
			break;
			default:
			printf("ERROR");
		}

		result+= steps;
		//at the end 
		if (vpos_o >= so.size()) orange_out = true;
		if (vpos_b >= sb.size()) blue_out = true;
	}
	printf("Case #%d: %d\n", case_no, result );
}

int main()
{
	unsigned _tc;
	scanf("%d", &_tc );
	for (unsigned _tc_it= 0; _tc_it < _tc; ++_tc_it)
	{
		unsigned _seq_cnt;
		scanf("%d", &_seq_cnt);
		sequence_t so, sb;
		for (unsigned i = 0;i < _seq_cnt; ++i)
		{
			char robo;
			unsigned btn = 0;
			char buff[0x10];
			scanf("%s", buff);
			robo = buff[0];
			scanf("%d", &btn);
			if (robo == ORANGE_C) so.push_back( btn_t(i+1, btn));
			else sb.push_back( btn_t(i+1, btn));
		}

		solve( _tc_it + 1, so, sb);
	}
};
