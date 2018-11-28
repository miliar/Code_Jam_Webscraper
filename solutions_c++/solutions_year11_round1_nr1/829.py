#include <fstream>

using namespace std;

int main()
{
	ifstream in_file("A-large.in");
	ofstream out_file("A.out");
	
	long long trials;
	in_file >> trials;
	
	for(int i = 0; i < trials; i++)
	{
		long long n; //max games today
		in_file >> n;
		
		long long perc_today;
		in_file >> perc_today;
		
		long long perc_hist;
		in_file >> perc_hist;
		
		//special cases
		if(perc_hist == 0 && perc_today != 0)
		{
			out_file << "Case #" << i + 1 << ": Broken" << endl;
			continue;
		}
		
		else if(perc_hist == 100 && perc_today != 100)
		{
			out_file << "Case #" << i + 1 << ": Broken" << endl;
			continue;
		}
		
		else if(n >= 100)
		{
			out_file << "Case #" << i + 1 << ": Possible" << endl;
			continue;
		}
		
		else
		{
			int n0 = n;
			bool is_possible = false;
			
			for(int i2 = 1; i2 <= n0; i2++)
			{
				if((i2 * perc_today) % 100 == 0)
				{
					out_file << "Case #" << i + 1 << ": Possible" << endl;
					is_possible = true;
					break;
				}
			}
			
			if(!is_possible)
			{
				out_file << "Case #" << i + 1 << ": Broken" << endl;
			}
		}
	}
	
	return 0;
}
