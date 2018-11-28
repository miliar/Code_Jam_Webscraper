#include <fstream>
#include <cmath>

using namespace std;

int main()
{
	ifstream in_file("A-large.in");
	ofstream out_file("A-large.out");

	int cases;
	in_file >> cases;
	
	for(int i = 0; i < cases; i++)
	{
		int orange_loc = 1;
		int blue_loc = 1;

		int time_elapsed = 0;
		int recent_time = 0;
		char recent_bot = 'z';
		
		int buttons;
		in_file >> buttons;
		
		char next_bot;
		int next_loc;
		
		for(int c = 0; c < buttons; c++)
		{
			in_file >> next_bot;
			in_file >> next_loc;
			
			
			
			if(next_bot == 'O')
			{
				int cur_time = abs(orange_loc - next_loc) + 1;
				
				if(recent_bot == 'O')
				{
					time_elapsed += cur_time;
					recent_time += cur_time;
				}

				else if((cur_time - 1) < recent_time)
				{
					time_elapsed++;
					recent_time = 1;
				}
				
				else
				{
					time_elapsed += cur_time - recent_time;
					recent_time = cur_time - recent_time;
				}
				
				recent_bot = 'O';
				orange_loc = next_loc;
			}
			
			else
			{
				int cur_time = abs(blue_loc - next_loc) + 1;
				
				if(recent_bot == 'B')
				{
					time_elapsed += cur_time;
					recent_time += cur_time;
				}

				else if((cur_time - 1) < recent_time)
				{
					time_elapsed++;
					recent_time = 1;
				}
				
				else
				{
					time_elapsed += cur_time - recent_time;
					recent_time = cur_time - recent_time;
				}
				
				recent_bot = 'B';
				blue_loc = next_loc;
			}
		}
		
		out_file << "Case #" << i + 1 << ": " << time_elapsed << endl;
	}

	return 0;
}
