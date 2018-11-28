#include<stdio.h>
#include<vector>
#include<stdlib.h>
using namespace std;
struct command
{
	char color;
	int switchno;
};
int main()
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for (int test_case=1 ; test_case <= num_test_cases; test_case++)
	{
		int num_entries; 
		int prev_b_pos = 1;
		int prev_o_pos = 1; 
		int last_b_time = 0;
		int last_o_time = 0;
		scanf("%d",&num_entries);
		vector<command> commands;
		for (int i=0 ; i < num_entries; i++)
		{
			command c;
			scanf(" %c%d",&c.color,&c.switchno);
			commands.push_back(c);
		}
		for (int i=0 ; i < num_entries; i++)
		{
				if (commands[i].color == 'B')
				{
					int time = abs(prev_b_pos - commands[i].switchno) + 1;
					last_b_time = max(last_b_time + time, last_o_time +1);
					prev_b_pos = commands[i].switchno;
				}
				else
				{
					int time = abs(prev_o_pos - commands[i].switchno) + 1;
					last_o_time = max(last_o_time + time, last_b_time +1);
					prev_o_pos = commands[i].switchno;
					
				}
		}
		printf("Case #%d: %d\n",test_case, max(last_b_time,last_o_time));		
	}
}
