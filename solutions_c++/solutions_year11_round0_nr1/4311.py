
#include <iostream>
#include <vector>
using namespace std;

struct robo_jobs
{
    int index;
	int button_loc;
	int time_req_after_last_j;
};


int main(void)
{
    int num_of_cases;
	cin>>num_of_cases;

	int tc_count = 1;
	while(tc_count <= num_of_cases)
	{
	    int seq_len;
		cin>>seq_len;
		vector < robo_jobs > blue_robo_jobs;
		vector < robo_jobs > orange_robo_jobs;

		for (int i=0; i<seq_len; i++)
		{
			char temp_c;
		    cin>>temp_c;
		    int temp_v;
			cin>>temp_v;
			robo_jobs j;
			j.index = i;
			j.button_loc = temp_v;
			if (temp_c == 'O')
			{
				orange_robo_jobs.push_back(j);
			}
			else
			{
				blue_robo_jobs.push_back(j);
			}
		}/* jobs ready */

		for (int i=0; i<blue_robo_jobs.size(); i++)
		{
			int temp;
			if (i==0)
			{
				temp = blue_robo_jobs[i].button_loc;
			}
			else
			{
			    temp = abs(blue_robo_jobs[i-1].button_loc - blue_robo_jobs[i].button_loc) + 1;
			}
			blue_robo_jobs[i].time_req_after_last_j = temp;
		}

		for (int i=0; i<orange_robo_jobs.size(); i++)
		{
			int temp;
			if (i==0)
			{
				temp = orange_robo_jobs[i].button_loc;
			}
			else
			{
			    temp = abs(orange_robo_jobs[i-1].button_loc - orange_robo_jobs[i].button_loc) + 1;
			}
			orange_robo_jobs[i].time_req_after_last_j = temp;  
		}/* jobs finally ready */

		int l1=0, l2=0;
		int b_wait_time = 0, o_wait_time = 0;
		int ans = 0;
		while ((l1<blue_robo_jobs.size())&&(l2<orange_robo_jobs.size()))
		{
			if (blue_robo_jobs[l1].index<orange_robo_jobs[l2].index)
			{
				if(b_wait_time >= blue_robo_jobs[l1].time_req_after_last_j)
				{
				    ans = ans+1;
					o_wait_time++;
				}
				else
				{
				    ans = ans + blue_robo_jobs[l1].time_req_after_last_j - b_wait_time;
                    o_wait_time = o_wait_time + blue_robo_jobs[l1].time_req_after_last_j - b_wait_time;
				}
			    b_wait_time = 0;
				l1++;
			}
			else
			{
				if(o_wait_time >= orange_robo_jobs[l2].time_req_after_last_j)
				{
				   ans++;
				   b_wait_time++;
				}
				else
				{
				    ans = ans + orange_robo_jobs[l2].time_req_after_last_j - o_wait_time;
                    b_wait_time = b_wait_time + orange_robo_jobs[l2].time_req_after_last_j - o_wait_time;
				}
				o_wait_time = 0;
				l2++;
			}
		}

		while (l1<blue_robo_jobs.size())
		{
			if(b_wait_time >= blue_robo_jobs[l1].time_req_after_last_j)
			{
			    ans = ans+1;
			}
			else
			{
			    ans = ans + blue_robo_jobs[l1].time_req_after_last_j - b_wait_time;
			}
		    b_wait_time = 0;
			l1++;
		}

		while(l2<orange_robo_jobs.size())
		{
			if(o_wait_time >= orange_robo_jobs[l2].time_req_after_last_j)
			{
			   ans++;
			}
			else
			{
			    ans = ans + orange_robo_jobs[l2].time_req_after_last_j - o_wait_time;
			}
			o_wait_time = 0;
			l2++;
		}
		cout<<"Case #"<<tc_count<<": "<< ans<<"\n";
		tc_count++;
	}
}