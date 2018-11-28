#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
	//char buffer[16392];

	if(argc < 3)
	{
		cout << "provide input and output file names" << endl;
		exit(1);
	}
	
	string ifname(argv[1]);
	string ofname(argv[2]);

	ifstream input_file(ifname.c_str());
	if( input_file.bad() || !input_file.is_open() )
	{
		cout << "failed opening the input file" << endl;
		exit(2);
	}
	ofstream output_file(ofname.c_str());
	if( output_file.bad() || !output_file.is_open() )
	{
		cout << "failed opening the output file" << endl;
		exit(3);
	}

	int T=0;
	int N=0;

	input_file >> T;
	
	for ( int test_case=1;test_case<=T;test_case++ )
	{
		input_file >> N;

		int* values = new int[N];
		bool* trig = new bool[N];

		bool found_sol = false;
		int Sean_max =0;

		// reading values in
		for ( int value_count=0;value_count<N;value_count++ )
		{
			input_file >> values[value_count];
			trig[value_count]=false;
		}

		if ( N > 1 )
		{
			bool any_false = true;
			while ( any_false )
			{
				bool prev_trig_changed_to_false = true;

				int Sean_sum = 0;
				int Sean_sum_by_Patrick=0;
				int Patrick_sum = 0;

				any_false=false;

				for ( int value_index = 0; value_index < N; value_index++ )
				{
					if ( prev_trig_changed_to_false )
					{
						trig[value_index] = ! trig[value_index];
						prev_trig_changed_to_false = ! trig[value_index];
					}
					else
						prev_trig_changed_to_false = false;
					
					if ( trig[value_index] )
						Patrick_sum = Patrick_sum ^ values[value_index];
					else
					{
						Sean_sum = Sean_sum + values[value_index];
						Sean_sum_by_Patrick = Sean_sum_by_Patrick ^ values[value_index];
						any_false = true;
					}
				} 
				if ( Patrick_sum == Sean_sum_by_Patrick )
				{
					found_sol = true;
					Sean_max = (Sean_max<Sean_sum)?Sean_sum:Sean_max;
				}
			} // end of while ( any_false )
		}

		delete [] values;
		delete [] trig;

		if ( found_sol )
		{
			//cout << "Case #" << test_case << ": " << Sean_max << endl;
			output_file << "Case #" << test_case << ": " << Sean_max << endl;
		}
		else
		{
			//cout << "Case #" << test_case << ": NO" << endl;
			output_file << "Case #" << test_case << ": NO" << endl;
		}
	}

	return 0;
}