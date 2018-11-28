#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>


using namespace std;

int main()
{
	ifstream in_file("C-small-attempt0.in");
	ofstream out_file("C.out");
	
	int trials;
	in_file >> trials;
	
	for(int i = 0; i < trials; i++)
	{
		out_file << "Case #" << i + 1 << ": ";
		
		int num_play;
		in_file >> num_play;
		
		int low_note;
		in_file >> low_note;
		
		int high_note;
		in_file >> high_note;
		
		//get other notes
		int others[num_play];
		for(int c = 0; c < num_play; c++)
		{
			in_file >> others[c];
		}
		
		bool can_play = false;
		
		for(int c = low_note; c <= high_note; c++)
		{
			
			
			bool tester = true;
			for(int c1 = 0; c1 < num_play; c1++)
			{
				if(tester)
				{
					if(others[c1] % c != 0 && c % others[c1] != 0)
					{
						tester = false;
					}
				}
			}
			
			if(tester == true)
			{
				out_file << c;
				can_play = true;
				break;
			}
		}
		
		if(!can_play)
		{
			out_file << "NO";
		}
		
		out_file << endl;
	}
	
	
	return 0;
}


