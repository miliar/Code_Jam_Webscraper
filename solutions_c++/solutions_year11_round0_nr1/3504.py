#include <cstdio>
using namespace std;

#define max(a, b) ((a) > (b) ? (a) : (b))
#define abs(a) ((a) < 0 ? -(a) : (a))
int main()
{
	int Z, N; scanf("%i", &Z);
	for(int test_case = 1; test_case <= Z; ++test_case)
	{
		scanf("%i", &N);
		int curr_pos_O = 1, curr_pos_B = 1;
		int unused_O = 0, unused_B = 0;
		int res = 0;
		
		char col; int but;
		for(int i = 0; i < N; ++i)
		{
			scanf("%1s %i", &col, &but);
			if(col == 'O')
			{
				int steps = max(0, abs(curr_pos_O - but) - unused_O) + 1;
				unused_B += steps;
				res += steps;
				unused_O = 0;
				curr_pos_O = but;
			}
			else
			{
				int steps = max(0, abs(curr_pos_B - but) - unused_B) + 1;
				unused_O += steps;
				res += steps;
				unused_B = 0;
				curr_pos_B = but;
			}
		}
		printf("Case #%i: %i\n", test_case, res);
	}
	return 0;
}
