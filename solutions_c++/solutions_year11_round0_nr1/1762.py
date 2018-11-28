#include<iostream>
using namespace std;

class ButtonSeq
{
public: char robot;
		int button;
};

int main()
{
	freopen( "data_in.txt" , "r" , stdin );
	freopen( "data_out.txt" , "w" , stdout );
	int T , N;

	cin >> T;

	for( int t = 1 ; t <= T ; t ++ )
	{
		cout << "Case #" << t << ": ";

		cin >> N;


		ButtonSeq* but_seq = new ButtonSeq[ N ];

		for( int n = 0 ; n < N ; n ++ )
			cin >> but_seq[ n ].robot >> but_seq[ n ].button;
		

		int pre_o_pos = 0 , pre_b_pos = 0;
		int pre_o_time = -1 , pre_b_time = -1;

		int cur_time = but_seq[ 0 ].button;

		if( but_seq[ 0 ].robot == 'O' )
		{
			pre_o_pos = but_seq[ 0 ].button;
			pre_o_time = but_seq[ 0 ].button;
		}
		else
		{
			pre_b_pos = but_seq[ 0 ].button;
			pre_b_time = but_seq[ 0 ].button;
		}

		char pre_robot = but_seq[ 0 ].robot;

		for( int n = 1 ; n < N ; n ++ )
		{
			if( but_seq[ n ].robot == pre_robot )
			{
				cur_time += abs( but_seq[ n ].button - but_seq[ n - 1 ].button ) + 1;
				if( but_seq[ n ].robot == 'O' )
				{
					pre_o_pos = but_seq[ n ].button;
					pre_o_time = cur_time;
				}
				else
				{
					pre_b_pos = but_seq[ n ].button;
					pre_b_time = cur_time;
				}
			}
			else
			{
				
				if( but_seq[ n ].robot == 'O' )
				{
					int d = abs( but_seq[ n ].button - pre_o_pos ) + 1;
					if( cur_time >= d + pre_o_time )
						cur_time ++;
					else
						cur_time = d + pre_o_time;

					pre_o_pos = but_seq[ n ].button;
					pre_o_time = cur_time;
				}
				else
				{
					int d = abs( but_seq[ n ].button - pre_b_pos ) + 1;
					if( cur_time >= d + pre_b_time )
						cur_time ++;
					else
						cur_time = d + pre_b_time;

					pre_b_pos = but_seq[ n ].button;
					pre_b_time = cur_time;
				}
				pre_robot = but_seq[ n ].robot;
			}
		}
		cout << cur_time << "\n";
		cout <<"";

	}

	return 0;
}