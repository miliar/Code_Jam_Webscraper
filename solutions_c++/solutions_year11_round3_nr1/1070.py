#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
	ifstream in_file("A-large.in");
	ofstream out_file("A.out");
	
	int trials;
	in_file >> trials;
	
	for(int i = 0; i < trials; i++)
	{
		out_file << "Case #" << i + 1 << ":" << endl;
		
		int lines;
		int chars;
		
		in_file >> lines;
		in_file >> chars;
		
		char pic[lines][chars];
		
		bool is_possible = true;
		
		for(int c = 0; c < lines; c++)
		{
			in_file >> pic[c];
		}
		
		for(int li = 0; li < lines; li++)
		{
			for(int ch = 0; ch < chars; ch++)
			{
				if(pic[li][ch] == '#')
				{
					if(li == (lines - 1))//first check for edge case
					{
						is_possible = false;
						break;
					}
					
					else if(ch == (chars - 1))
					{
						is_possible = false;
						break;
					}
					
					if(pic[li][ch + 1] == '#' && pic[li + 1][ch] == '#' && pic[li + 1][ch + 1] == '#')
					{
						pic[li][ch] = '/';
						pic[li][ch + 1] = '\\';
						pic[li + 1][ch] = '\\';
						pic[li + 1][ch + 1] = '/';
					}
					
					else
					{
						is_possible = false;
						break;
					}
				}
			}
			
			if(!is_possible) //end processing, a fail case was detected
			{
				break;
			}
		}
		
		if(!is_possible)
		{
			out_file << "Impossible" << endl;
		}
		
		else
		{
			for(int li = 0; li < lines; li++)
			{
				for(int ch = 0; ch < chars; ch++)
				{
					out_file << pic[li][ch];
				}
				out_file << endl;
			}
		}
	}
	
	return 0;
}


