#include <iostream>
#include <fstream>
#include <string>
#include <queue>
using namespace std;

int main () 
{
	int numTests, case_number = 1;
	string line_count;
	int num_rides, capacity, num_groups, euros, size, passengers, groups_in_line;
	string R, k, N, g;
	queue<int> group;

    ifstream inFile("C-small-attempt0.in");
	if (inFile.is_open())
	{
		
		// Get number of lines in input file
		getline(inFile, line_count);
		numTests = atoi(line_count.c_str());
		
		// Open output file
		ofstream outFile;
		outFile.open("ThemePark_Output.txt");
		if (!outFile.is_open())
		{
			cout << "Unable to open output file.\n";
			exit(1);
		}
		
		while (numTests > 0)
		{			
			// Get test case from input, R, k, N, group
			getline (inFile, R, ' ');
			getline (inFile, k, ' ');
			getline (inFile, N);
			num_rides = atoi(R.c_str());
			capacity = atoi(k.c_str());
			num_groups = atoi(N.c_str());
			
			// Place all groups in queue
			for (int i = 1; i <= num_groups; i++)
			{
				if (i < num_groups)
					getline (inFile, g, ' ');
				else
					getline (inFile, g);
				size = atoi(g.c_str());
				group.push(size);
			}

			// Calculate total
			euros = 0;

			for (int r = 0; r < num_rides; r++)
			{
				passengers = 0;
				groups_in_line = num_groups;
				// Group in front gets on the ride, then goes to the back of the line
				
				
				while ((passengers + group.front()) <= capacity &&
						groups_in_line > 0)
				{
					passengers += group.front();
					group.push(group.front());
					group.pop();
					groups_in_line--;
				}

				euros += passengers;
			}

			// Output
			outFile << "Case #" << case_number++ << ": ";
			outFile << euros << endl;
			
			// Empty queue, rides are over for the day
			while (!group.empty())
			{
				group.pop();
			}		
			
			numTests--;
		}
		outFile.close();
		inFile.close();
	}
	else
		cout << "Unable to open input file.\n";
	
	
	
    return 0;
}
	