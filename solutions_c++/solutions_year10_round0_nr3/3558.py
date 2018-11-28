/*
	evilrus
	Uladzimir Karneyenka
	Theme Park

	Microsoft Visual Studio 2008 Pro

*/

//#define BRUTEFORCE
#define ALTERNATIVE
//#define GENERATEINPUT
//#define RANDSMALLSET
//#define ENABLE_TIMER

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

#ifdef GENERATEINPUT

#include <ctime>
#include <cstdlib>


#endif

#ifdef ENABLE_TIMER

#include <ctime>
#include <iomanip>

#endif

using namespace std;

typedef struct invariant
{
	long index;
	long cost;
	bool repetition;
} invariant;

int main(int argc, char** argv)
{

#ifdef GENERATEINPUT
randominputgen:
	{	
		argc = 2;
		argv = new char*[2];
		argv[1] = "random_data.in";
		
		ofstream random_data_file(argv[1]);
		
		srand((unsigned int)time(NULL));

#ifdef RANDSMALLSET
		int R_MAXVAL = 1000;
		int k_MAXVAL = 100;
		int N_MAXVAL = 10;
		int gi_MAXVAL = 10;
#else
		
		int R_MAXVAL = 100000000;
		int k_MAXVAL = 1000000000;
		int N_MAXVAL = 1000;
		int gi_MAXVAL = 10000000;
		/*
		int R_MAXVAL = 1000000;
		int k_MAXVAL = 100000;
		int N_MAXVAL = 1000;
		int gi_MAXVAL = 10000;
		*/

#endif

		int T = 50;

		int R = 0;
		int k = 0;
		int N = 0;
		int gi = 0;
		
		random_data_file << T << endl;

		for(int i=0; i < T; i++)
		{
			// Generate R <= R_MAXVAL - rounds
			R = rand() % R_MAXVAL + 1;
			if( RAND_MAX < R_MAXVAL )
			{
				R = ( (rand() % 2) == 1 )? (R * (rand()+1)) : R ;
				if(R > R_MAXVAL)
					R = R_MAXVAL - rand();
			}
			// Generate k <= k_MAXVAL - capacity
			k = rand() % k_MAXVAL + 1;
			if( RAND_MAX < k_MAXVAL )
			{
				k = ( (rand() % 2) == 1 )? (k * (rand()+1)) : k ;
				if(k > k_MAXVAL)
					k = k_MAXVAL - rand();
			}
			// Generate N <= N_MAXVAL - number of groups
			N = rand() % N_MAXVAL + 1;
			if( RAND_MAX < N_MAXVAL )
			{
				N = ( (rand() % 2) == 1 )? (N * (rand()+1)) : N ;
				if(N > N_MAXVAL)
					N = N_MAXVAL - rand();
			}

			random_data_file << R << " " << k << " " << N << endl;

			// Generate groups(i.e. gi's)
			for(int group = 1; group <= N; group++)
			{
				// Generate gi <= k <= gi_MAXVAL

				int gi_local_limit = (gi_MAXVAL >= k)? k: gi_MAXVAL;
				gi = rand() % gi_local_limit + 1;
				if( RAND_MAX < gi_local_limit )
				{
					gi = ( (rand() % 2) == 1 )? (gi * (rand()+1)) : gi ;
					if(gi > gi_local_limit)
						gi = gi_local_limit - rand();
				}

				random_data_file << gi;
				if(group < N)
					random_data_file << " ";
				else
					random_data_file << endl;
			}
		}

		random_data_file.close();
	}
#endif


	if(argc < 2)
	{
		cout << "input file name is not provided" << endl;
		return 1;
	}

	string ifname(argv[1]);
	string ofname("");

	if(argc == 2)
	{
		int file_extension_pos = ifname.find_last_of(".");
		if( file_extension_pos == string::npos )
			ofname = ifname;
		else
			ofname = ifname.substr( 0, file_extension_pos );
		ofname += ".out";
	}
	else
		ofname = argv[2];
	
	cout << "input file: " << ifname << endl;
	cout << "output file: " << ofname << endl;

	ifstream input_file(ifname.c_str());
	if( input_file.bad() || !input_file.is_open() )
	{
		cout << "failed opening the input file" << endl;
		return 1; 
	}
	ofstream output_file(ofname.c_str());
	if( output_file.bad() || !output_file.is_open() )
	{
		cout << "failed opening the output file" << endl;
		return 1;
	}


	
	int T = 0;
	unsigned long R = 0;
	unsigned long k = 0;
	unsigned long N = 0;
	unsigned long gi = 0;


#ifdef BRUTEFORCE

#ifdef ENABLE_TIMER
	clock_t brute_force_start, brute_force_time_diff;
	brute_force_start = clock();
#endif
	input_file >> T; // get T
	//cout << "Number of cases: " << T << endl;

	for(int case_count = 1; case_count <= T; case_count++ )
	{
		cout << "\rCase #" << case_count;
		
		input_file >> R >> k >> N;

		unsigned long* groups = new (nothrow) unsigned long[N];
		if(groups == 0)
		{
			cout << "Failed to alloc mem(groups)." << endl;
			return 1;
		}
		
		bool* groups_on_the_ride = new (nothrow) bool[N];
		if(groups == 0)
		{
			cout << "Failed to alloc mem(groups_on_the_ride)." << endl;
			delete[]groups;
			return 1;
		}

		for(unsigned long i = 0; i < N; i++)
			input_file >> groups[i];

		unsigned long euros = 0;
		
		unsigned long group_idx = 0;

		while(R > 0)
		{
			unsigned long crowd = 0; // those who are getting on the ride

			for(unsigned long gor_idx = 0; gor_idx < N; gor_idx++)
				groups_on_the_ride[gor_idx] = false;

			bool load = true;

			while(load)
			{
				unsigned long temp = crowd + groups[group_idx];
				if(  temp <= k && !groups_on_the_ride[group_idx] )
				{
					crowd = temp;
					groups_on_the_ride[group_idx] = true;
					group_idx = (group_idx + 1) % N;
				}
				else
				{
					euros += crowd;
					load = false;
				}
			}

			R--;
		}
		
		// OUTPUT
		output_file << "Case #" << case_count << ": " << euros << endl ;

		delete[]groups;
		delete[]groups_on_the_ride;

	}
	
	input_file.seekg(0, ios_base::beg);

	cout << endl;

#ifdef ENABLE_TIMER
	brute_force_time_diff = clock() - brute_force_start;
	cout << "exec. time: " << brute_force_time_diff << " tics." << endl;
#endif

#endif

#ifdef ALTERNATIVE

#ifdef ENABLE_TIMER
	clock_t alternative_start, alternative_time_diff;
	alternative_start = clock();
#endif

	input_file >> T; // get T
	//cout << "Number of cases: " << T << endl;

	for(int case_count = 1; case_count <= T; case_count++ )
	{
		cout << "\rCase #" << case_count;
		
		input_file >> R >> k >> N;

		unsigned long* groups = new (nothrow) unsigned long[N];
		if(groups == 0)
		{
			cout << "Failed to alloc mem." << endl;
			return 1;
		}
		bool* groups_on_the_ride = new (nothrow) bool[N];
		if(groups == 0)
		{
			cout << "Failed to alloc mem(groups_on_the_ride)." << endl;
			delete[]groups;
			return 1;
		}

		unsigned long group_idx = 0;
		for(; group_idx < N; group_idx++)
			input_file >> groups[group_idx];

		
		vector<invariant*> invariants;

		group_idx = 0;

		unsigned long rounds_countdown = R;

		while(rounds_countdown > 0)
		{
			
			rounds_countdown--;
		
			unsigned long crowd = 0;

			for(unsigned long gor_idx = 0; gor_idx < N; gor_idx++)
				groups_on_the_ride[gor_idx] = false;

			bool load = true;
			
			unsigned long round_start_group_idx = group_idx;

			while(load)
			{
				unsigned long temp = crowd + groups[group_idx];
				if( temp <= k  && !groups_on_the_ride[group_idx] )
				{
					crowd = temp;
					groups_on_the_ride[group_idx] = true;
					group_idx = (group_idx + 1) % N;
				}
				else
					load = false;
			}
			
			
			bool invariant_found = false;
			for( unsigned long i = 0; i < invariants.size(); i++ )
				if( invariants[i]->index == round_start_group_idx )
				{
					invariants[i]->repetition = true;
					invariant_found = true;
					break;
				}

			if( !invariant_found )
			{
				invariant* temp_inv = new invariant;
				temp_inv->index = round_start_group_idx;
				temp_inv->cost = crowd;
				temp_inv->repetition = false;
				
				invariants.push_back(temp_inv);
			}
			else
				rounds_countdown = 0;

		} // done going through rounds


		unsigned long euros = 0;
		unsigned long euros_invariants_cost = 0;
		unsigned long euros_repetions_cost = 0;
		unsigned long euros_remainder_cost = 0;

		unsigned long rounds_not_accounted_yet = R;
		unsigned long repetitive_invariants_counter = 0;

		for( unsigned long i = 0; i < invariants.size(); i++ )
		{
			if( invariants[i]->repetition )
			{
				repetitive_invariants_counter++;
				euros_invariants_cost += invariants[i]->cost;
				if( i+1 < invariants.size() )
					invariants[(i+1)]->repetition = true;
			}
			else
			{
				euros += invariants[i]->cost;
				rounds_not_accounted_yet --;
			}
		}
		
		if( repetitive_invariants_counter > 0 )
		{
			unsigned long repetitions_count = rounds_not_accounted_yet / repetitive_invariants_counter;
			unsigned long remainder = rounds_not_accounted_yet % repetitive_invariants_counter;

			euros_repetions_cost = repetitions_count * euros_invariants_cost;
			for( unsigned long i = 0; i < invariants.size(); i++ )
				if( invariants[i]->repetition && (remainder > 0))
				{
					remainder --;
					euros_remainder_cost += invariants[i]->cost;
				}
		}
		
		euros +=  euros_repetions_cost + euros_remainder_cost;

		// OUTPUT
		/*
		output_file << "Case #" << case_count << ": " << euros << "; Invariants found: " << invariants.size() << "; Repetitive invariants found: " <<  repetitive_invariants_counter  << endl ;
		*/
		output_file << "Case #" << case_count << ": " << euros << endl;

		for( unsigned long i = 0; i < invariants.size(); i++ )
			delete invariants[i];
		invariants.empty();
		delete[]groups;
		delete[]groups_on_the_ride;

	}

	cout << endl;

#ifdef ENABLE_TIMER
	alternative_time_diff = clock() - alternative_start;
	cout << "exec. time: " << alternative_time_diff << " tics." << endl;
#endif

#endif

	cout << "Done" << endl;

	return 0;

}