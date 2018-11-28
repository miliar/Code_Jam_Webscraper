#include <stdio.h>
#include <functional>
#include <algorithm>
#include <vector>
#include <set>

struct trip
{
	int m_train_num;
	int m_depart;
	int m_arrive;
};

struct depart_pred : public std::less<trip>
{
	bool operator()(const trip& _Left, const trip& _Right) const
	{
		return (_Left.m_depart < _Right.m_depart);
	}
};

typedef std::vector<trip>	t_trips;
typedef std::multiset<int>	t_at_station;

char buff[128];

void get_buff()
{
	buff[0]='\0';
	gets(buff);
//	printf("Got : %s\n",buff);
}

int get_num()
{
	get_buff();
	return atoi(buff);
}

void get_2_nums(int nums[])
{
	get_buff();
	sscanf(buff,"%d %d",nums,nums+1);
}

void get_time(int& start, int& end)
{
	get_buff();
	buff[2]='\0';
	buff[5]='\0';
	buff[8]='\0';

	start=atoi(buff)*60+atoi(buff+3);
	end=atoi(buff+6)*60+atoi(buff+9);
}

int main(int argc, char* argv[])
{
	int n=get_num();

	for (int i=0 ; i<n ; ++i)
	{
		int turn_around=get_num();
		int trip_count[2];
		int trains_needed[2]={0};
		get_2_nums(trip_count);
		t_trips trips;
		t_at_station at_station[2];
		
		for (int train_num=0 ; train_num<2 ; ++train_num)
		{
			for (int j=0 ; j<trip_count[train_num] ; ++j)
			{
				trip t;
				t.m_train_num=train_num;
				get_time(t.m_depart,t.m_arrive);
				trips.push_back(t);
			}
		}
		std::sort(trips.begin(),trips.end(),depart_pred());

		for (size_t j=0, sz=trips.size() ; j<sz ; ++j)
		{
			trip& cur_trip=trips[j];
			t_at_station::iterator first_waiting=at_station[cur_trip.m_train_num].begin();
			
			if (first_waiting!=at_station[cur_trip.m_train_num].end() && *first_waiting+turn_around<=cur_trip.m_depart)
				at_station[cur_trip.m_train_num].erase(first_waiting);
			else
				++trains_needed[cur_trip.m_train_num];
			at_station[1-cur_trip.m_train_num].insert(cur_trip.m_arrive);
		}
		printf("Case #%d: %d %d\n",i+1,trains_needed[0],trains_needed[1]);
	}
	return 0;
}

