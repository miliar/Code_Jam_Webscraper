// initializing C++
#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <deque>

using namespace std;

// declaring function prototypes
int get_variables(ifstream &iFile, int &r_rc_runs, int &k_capacity, int &N_groups);
int get_groups(ifstream &iFile, deque<int> &g_groups, int &N_groups);
unsigned __int64 calculate_money( int &r_rc_runs, int &k_capacity, int &N_groups, deque<int> &g_groups);

int main ()
{
	int no_test_cases;
	ifstream iFile("input.txt");        // input.txt has integers, one per line
	ofstream oFile("output.txt");

	//Acquire initial variables
	iFile >> no_test_cases ;
	//cout << "Number of test cases: " << no_test_cases << endl;

	for(int i=0; i<no_test_cases ; i++)
	{
		int r_rc_runs=0, k_capacity=0, N_groups=0;

		get_variables(iFile, r_rc_runs, k_capacity, N_groups);
		//cout << "r_rc_runs: " << r_rc_runs << endl;
		//cout << "k_capacity: " << k_capacity << endl;
		//cout << "N_groups: " << N_groups << endl;

		deque<int> g_groups;
		get_groups(iFile, g_groups, N_groups);

		unsigned __int64 result = 0;
		result = calculate_money(r_rc_runs, k_capacity, N_groups,g_groups);

		//cout << "Case #" << i+1 << ": " << result << endl;
		oFile << "Case #" << i+1 << ": " << result << endl;
	}

	//cin.ignore( 80, '\n' );
	return 0;
}

unsigned __int64 calculate_money( int &r_rc_runs, int &k_capacity, int &N_groups, deque<int> &g_groups)
{
	unsigned __int64 total_income = 0, run_income = 0;
	int current_group = 0;

	//optimizations
	unsigned __int64 total_people = 0;
	for( int k =0; k < N_groups; k++ )
	{
		total_people += g_groups[k];
	}

	if(total_people/k_capacity < 1)
	{
		total_income = r_rc_runs * total_people;
		return total_income;
	}

	// Define mega groups
	deque<unsigned __int64> g_groups_4;
	deque<unsigned __int64> g_groups_20;
	deque<unsigned __int64> g_groups_100;
	deque<unsigned __int64> g_groups_500;

	unsigned __int64 partial_people4 = 0;
	unsigned __int64 partial_people20 = 0;
	unsigned __int64 partial_people100 = 0;
	unsigned __int64 partial_people500 = 0;

	for (int k=0; k < N_groups; )
	{
		partial_people4   += g_groups[k];
		partial_people20  += g_groups[k];
		partial_people100 += g_groups[k];
		partial_people500 += g_groups[k];
		
		k++;
		if (k%4==0)
		{
			g_groups_4.push_back(partial_people4);
			partial_people4 = 0;
		}
		if (k%20==0)
		{
			g_groups_20.push_back(partial_people20);
			partial_people20 = 0;
		}
		if (k%100==0)
		{
			g_groups_100.push_back(partial_people100);
			partial_people100 = 0;
		}
		if (k%500==0)
		{
			g_groups_500.push_back(partial_people500);
			partial_people500 = 0;
		}
	}
	g_groups_4.push_back(partial_people4);
	g_groups_20.push_back(partial_people20);
	g_groups_100.push_back(partial_people100);
	g_groups_500.push_back(partial_people500);

	//find pattern
	deque<int> patterns; 
	int flag_pattern=0;
	unsigned __int64 pattern_income=0;
	int pattern_runs=0;
	//find pattern--

	for(int i=0; i<r_rc_runs; i++) //all runs
	{
		run_income = 0;
		while ( 1 )
		{
			if(current_group >= N_groups)
				current_group = 0;

			if (current_group % 500==0) //try a 500
			{
				int mega_group = current_group/500;
				if (run_income + g_groups_500[mega_group] <= k_capacity)
				{
					run_income += g_groups_500[mega_group];
					current_group += 500;
					continue;
				}
			}
			if(current_group % 100==0)
			{
				int mega_group = current_group/100;
				if (run_income + g_groups_100[mega_group] <= k_capacity)
				{
					run_income += g_groups_100[mega_group];
					current_group += 100;
					continue;
				}
			}
			if(current_group % 20==0)
			{
				int mega_group = current_group/20;
				if (run_income + g_groups_20[mega_group] <= k_capacity)
				{
					run_income += g_groups_20[mega_group];
					current_group += 20;
					continue;
				}
			}
			if(current_group % 4==0)
			{
				int mega_group = current_group/4;
				if (run_income + g_groups_4[mega_group] <= k_capacity)
				{
					run_income += g_groups_4[mega_group];
					current_group += 4;
					continue;
				}
			}

			if (run_income + g_groups[current_group] <= k_capacity)
			{
				run_income += g_groups[current_group];
				current_group++;
			}
			else
				break;
		}
		total_income += run_income;

		//find a pattern
		if(flag_pattern == 0)
		{
			for( unsigned int m = 0; m < patterns.size(); m++)
			{
				if (current_group == patterns[m])
				{ //Found a pattern
					flag_pattern = current_group;
					break;
				}
			}
			patterns.push_back(current_group);
		}
		else if(flag_pattern > 0)
		{
			//enquanto nao surgir outra vez o padrão, contar o numero de elementos num padrão e a quantidade de dinheiro gerada
			pattern_income += run_income;
			pattern_runs ++;
			if (flag_pattern == current_group) //pattern has ended
			{
				int patterns_to_go = (r_rc_runs - i)/pattern_runs - 1;
				i += pattern_runs*patterns_to_go;
				total_income += pattern_income*patterns_to_go;
				flag_pattern = -1; //Done!
			}
		}
		//--
	}
	return total_income;
}

int get_groups(ifstream &iFile, deque<int> &g_groups, int &N_groups)
{
	int temp_int;
	for(int i=0; i<N_groups && iFile >> temp_int ; i++)
	{
		g_groups.push_back(temp_int);
	}
	return 0;
}

int get_variables(ifstream &iFile, int &r_rc_runs, int &k_capacity, int &N_groups)
{
	int temp_int;
	for(int i=0; i<3 && iFile >> temp_int ; i++)
	{
		switch(i)
		{
		case 0:
			r_rc_runs = temp_int;
			//cout << "r_rc_runs: " << r_rc_runs << endl;
			break;
		case 1:
			k_capacity = temp_int;
			//cout << "k_capacity: " << k_capacity << endl;
			break;
		case 2:
			N_groups = temp_int;
			//cout << "N_groups: " << N_groups << endl;
			break;
		}
	}
	return 0;
}

