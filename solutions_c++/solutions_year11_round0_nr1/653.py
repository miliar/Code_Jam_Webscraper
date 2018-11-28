#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int T;
	cin >> T;
	int case_num = 1;
	while(T>0)
	{
	  int N;  cin >> N;
		vector<char> robot(N); vector<int> button(N);
		for(int i=0;i<N;i++) cin >> robot[i] >> button[i];
		int o_pos = 1, b_pos = 1;
		int o_time = 0, b_time = 0;
		int total = 0;
		for(int i=0;i<N;i++)
		{
		  if(robot[i] == 'O')
			{
			  int travel_time;
				int needed_travel_time = abs(o_pos - button[i]);
				if(o_time >= needed_travel_time) travel_time = 0;
				else travel_time = needed_travel_time - o_time;
				int total_time = travel_time + 1;
				o_time = 0; o_pos = button[i];
				b_time += total_time;
				total += total_time;
			}
			else
			{
			  int travel_time;
				int needed_travel_time = abs(b_pos - button[i]);
				if(b_time >= needed_travel_time) travel_time = 0;
				else travel_time = needed_travel_time - b_time;
				int total_time = travel_time + 1;
				b_time = 0; b_pos = button[i];
				o_time += total_time;
				total += total_time;
			}
		}
		cout << "Case #" << case_num << ": " << total << endl;
	
	  T--; case_num++;
	}

  return 0;
}
