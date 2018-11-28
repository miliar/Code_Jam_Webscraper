#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Train {
public:
	int stime;
	int etime;
	bool from_a; // true if it is from A to B
	bool is_scheduled; // true if it is already scheduled with a train
	
	bool operator < (const Train comp) const {
		return stime < comp.stime;
	}
};

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int num_datasets, dataset, na, nb;
	int delay;
	string stime, etime;
	int hour, min, cur_time;
	bool now_in_a;
	int i, left_schedule;
	int answer_a, answer_b;
	vector<Train> schedule;
	Train new_train;
	
	fin >> num_datasets;
	for(dataset = 1; dataset <= num_datasets; dataset++)
	{
		fin >> delay;
		fin >> na >> nb;
		for(i = 0; i < na; i++)
		{
			fin >> stime >> etime;
			// stime
			hour = (int)(stime[0] - '0') * 10 + (int)(stime[1] - '0');
			min = (int)(stime[3] - '0') * 10 + (int)(stime[4] - '0');
			new_train.stime = hour * 60 + min;
			// etime
			hour = (int)(etime[0] - '0') * 10 + (int)(etime[1] - '0');
			min = (int)(etime[3] - '0') * 10 + (int)(etime[4] - '0');
			new_train.etime = hour * 60 + min;
			new_train.from_a = true;
			new_train.is_scheduled = false;
			schedule.push_back(new_train);
			//cout << stime << " " << etime << " " << new_train.stime << " " << new_train.etime << endl;
		}

		for(i = 0; i < nb; i++)
		{
			fin >> stime >> etime;
			// stime
			hour = (int)(stime[0] - '0') * 10 + (int)(stime[1] - '0');
			min = (int)(stime[3] - '0') * 10 + (int)(stime[4] - '0');
			new_train.stime = hour * 60 + min;
			// etime
			hour = (int)(etime[0] - '0') * 10 + (int)(etime[1] - '0');
			min = (int)(etime[3] - '0') * 10 + (int)(etime[4] - '0');
			new_train.etime = hour * 60 + min;
			new_train.from_a = false;
			new_train.is_scheduled = false;
			schedule.push_back(new_train);
			//cout << stime << " " << etime << " " << new_train.stime << " " << new_train.etime << endl;
		}
		sort(schedule.begin(), schedule.end());
		
		left_schedule = na + nb;
		answer_a = answer_b = 0;
		while(left_schedule > 0)
		{
			for(i = 0; i < schedule.size(); i++)
			{
				if(!schedule[i].is_scheduled) break;
			}
			
			if(schedule[i].from_a == true) 
			{
				answer_a++;
				now_in_a = false;
			}
			else
			{
				answer_b++;
				now_in_a = true;
			}
			//cout << "schedule#" << i;
			
			schedule[i].is_scheduled = true;
			left_schedule--;
			cur_time = schedule[i].etime + delay;
			
			for(i++ ; i < schedule.size(); i++)
			{
				if(schedule[i].is_scheduled == false &&
					schedule[i].from_a == now_in_a &&
					schedule[i].stime >= cur_time)
				{
					schedule[i].is_scheduled = true;
					left_schedule--;
					cur_time = schedule[i].etime + delay;
					now_in_a = !(now_in_a);
					//cout << " - schedule#" << i;
				}
			}
			//cout << endl;
		}
		fout << "Case #" << dataset << ": " << answer_a << " " << answer_b << endl;
		//cout << "---------- end of dataset#" << dataset <<" --------" << endl;
		schedule.clear();
	}	
	fin.close();
	fout.close();	
	return 0;
}