#include <iostream>
#include <istream>
#include <ostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <functional>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cstdio>

using namespace std;


/*----------- slack time --------------*/
static int slack_time;


struct TrainTimeUnit{
	int start;
	int end;
	bool   operator < ( const   TrainTimeUnit&   p)   
	{   
		return   start   <  p.start   ||   (start   ==   p.start   &&   end  <  p.end);   
	}   
};

///return the minute count time 
int get_minute(string time)
{
	string::iterator pos = find(time.begin(), time.end(), ':');
	string hour(time.begin(), pos);
	string minute(++pos, time.end());
	return atoi(hour.c_str()) * 60 + atoi(minute.c_str());
}


void simulate(vector<TrainTimeUnit>& a_time, vector<TrainTimeUnit>& b_time, int& a_count, int& b_count)
{
	int i , j;
	priority_queue<int, vector<int>, greater<int>> a_train;
	priority_queue<int, vector<int>, greater<int>> b_train;

	std::sort(a_time.begin(), a_time.end());
	std::sort(b_time.begin(), b_time.end());

	for(i = 0, j = 0, a_count = 0, b_count = 0; i < a_time.size() && j < b_time.size();)
	{
		TrainTimeUnit unit1  =  a_time.at(i);
		TrainTimeUnit unit2  =  b_time.at(j);
		if(unit1 < unit2){
			int time = 0;	///if add a new train, then it could start at any time
			
			if(a_train.size() == 0){
				a_count++;
			}else{
				time = a_train.top();
				if(time > unit1.start){
					a_count++;
				}else{
					a_train.pop();
				}
			}

			b_train.push(unit1.end + slack_time);
			i++;
		}else{	
			int time = 0;
			
			if(b_train.size() == 0){
				b_count++;
			}else{
				time = b_train.top();
				if(time > unit2.start){
					b_count++;
				}else{
					b_train.pop();
				}
			}
			a_train.push(unit2.end + slack_time);
			j++;
		}
	}


	if(i == a_time.size()){
		for( ;j < b_time.size();j++)
		{
			TrainTimeUnit unit = b_time.at(j);
			if(b_train.size() == 0){
				b_count++;
				continue;
			}
			int time = b_train.top();
			if(time > unit.start){
				b_count++;
			}else{
				b_train.pop();
			}
		}
	}else if(j == b_time.size()){
		for( ;i < a_time.size();i++)
		{
			TrainTimeUnit unit = a_time.at(i);
			if(a_train.size() == 0){
				a_count++;
				continue;
			}
			int time = a_train.top();
			if(time > unit.start){
				a_count++;
			}else {
				a_train.pop();
			}
		}
	}

}
//////////////IO

static void read_time(int NA, int NB, vector<TrainTimeUnit>& a_time, vector<TrainTimeUnit>& b_time)
{
	for(int i = 0; i < NA + NB; i++)
	{
		TrainTimeUnit unit;
		string start;
		string end;

		in >> start >> end;
		unit.start = get_minute(start);
		unit.end = get_minute(end);
		if(i < NA) a_time.push_back(unit);
		else b_time.push_back(unit);
	}

}


static void process_one_case2(int num)
{
	int NA, NB;
	vector<TrainTimeUnit> a_time;
	vector<TrainTimeUnit> b_time;

	in >> slack_time;
	in >> NA>> NB;
	read_time(NA, NB, a_time, b_time);

	//////start simulation
	int a_count = 0, b_count = 0;
	simulate(a_time, b_time, a_count, b_count);

	out << "Case #" << num << ": " <<a_count << " " <<b_count<<endl;
}

int main(int argc, char** argv)
{
	int case_num;
	in >> case_num;

	for(int i = 1; i <= case_num; i++)
	{
		process_one_case2(i);
	}

	return 0;

}