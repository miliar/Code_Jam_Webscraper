#include <iostream>
#include <string>
using namespace std;

#define SMALL_INP 20
#define LARGE_INP 100
enum job_own
{
	NONE, ORANGE, BLUE
};
struct job_seq
{
	job_own own;
	int b_num;
	job_seq():own(NONE),b_num(0){}
};

int main()
{
	int test_num=0;
	cin >> test_num;
	
	std::string outputStr;

	int it_test;
	for(it_test=0; it_test < test_num; it_test++)
	{
		int pair_num = 0;
		cin >> pair_num;
		
		job_seq seq[LARGE_INP];

		//read each pair;
		int it_pair;
		for( it_pair=0; it_pair < pair_num; it_pair++)
		{
			// Read owner
			char robo = '\0';
			cin >> robo;
			switch(robo)
			{
			case 'O':
			case 'o':
				seq[it_pair].own=ORANGE;	
				break;
			case 'B':
			case 'b':
				seq[it_pair].own=BLUE;
				break;
			default:
				{
					cout << "Bad input Test# " << it_test << " Pair# " << it_pair << endl;
					return -1;
				}
			}
			
			// read but num
			cin >> seq[it_pair].b_num;
		}

		// Process jobs. Note number of movements needed. Note locations, and 
		// time on global time line when last job done.
		
		int orange_loc = 1;
		int orange_last_job_tim = 0;
		
		int blue_loc = 1;
		int blue_last_job_tim = 0;
		
		int global_time = 0;
		
		for( it_pair=0; it_pair < pair_num; it_pair++)
		{
			//Job.
			int b_job = seq[it_pair].b_num;
			job_own own_job = seq[it_pair].own;

			// calculate no of movements.
			// local...
			int mv_job = 0;
			if(own_job==ORANGE ) 
				mv_job = abs(orange_loc - b_job );
			else
				mv_job = abs(blue_loc - b_job );

			// global
			if( own_job==ORANGE )
				mv_job = mv_job - (global_time - orange_last_job_tim);
			else
				mv_job = mv_job - (global_time - blue_last_job_tim);
			
			if( mv_job < 0) mv_job = 0;

			// Update all
			global_time += mv_job;
			global_time += 1; // Push Button;
			if(own_job==ORANGE )
			{
				orange_last_job_tim = global_time;
				orange_loc = b_job;
			}
			else
			{
				blue_loc = b_job;
				blue_last_job_tim = global_time;
			}
		}

		
		//cout << "Case #" << it_test+1 << ": " << global_time << endl;
		
		// temp
		char outp[100];
		sprintf( outp, "Case #%d: %d\n", it_test+1, global_time);
			outputStr+= outp;
	}
	//std::cout << "Hellow " << std::endl;
	cout << "Output " << endl << endl;
	cout << outputStr;
	return 0;
}
