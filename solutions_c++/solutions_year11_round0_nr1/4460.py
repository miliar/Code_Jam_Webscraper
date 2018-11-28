#include <iostream>
#include <cmath>

using namespace std;

struct bot_move
{
	char robot;
	int button;
};

int main()
{
	int n;
	cin >> n;

	for( int i = 0; i < n; i++ )
	{
		int count;
		cin >> count;
		bot_move *moves = new bot_move[count];
		
		for( int j = 0; j < count; j++ )
		{
			cin >> moves[j].robot;
			cin >> moves[j].button;
		}

		long position_o, position_b;
		long last_move_time_o, last_move_time_b;
		last_move_time_o = last_move_time_b = 0;
		position_o = position_b = 1;
		long seconds = 0;

		for( int j = 0; j < count; j++ )
		{
			if(moves[j].robot == 'O')
			{
				if( fabs(moves[j].button - position_o) > (seconds - last_move_time_o) )
				{
					seconds += fabs(moves[j].button - position_o) - (seconds - last_move_time_o) + 1;
				}
				else
				{
					seconds += 1;
				}
				position_o = moves[j].button;
				last_move_time_o = seconds;
			}
			else
			{
				if( fabs(moves[j].button - position_b) > (seconds - last_move_time_b) )
				{
					seconds += fabs(moves[j].button - position_b) - (seconds - last_move_time_b) + 1;
				}
				else
				{
					seconds += 1;
				}
				position_b = moves[j].button;
				last_move_time_b = seconds;

			}
		}

		cout << "Case #" << i + 1 << ": " << seconds << endl;
//		for( int j = 0; j < count; j++ )
//		{
//			cout << moves[j].robot << " " << moves[j].button << endl;
//		}

		delete []moves;	
	}

	return 0;
}
