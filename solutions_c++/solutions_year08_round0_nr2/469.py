#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int T, count;
int ansA, ansB;

vector<pair<int, char> > trains; // departure in min. and type of the train

// XXX: arrivals should have smaller values than corresponding departures
#define ARR_A 0
#define ARR_B 1
#define DEP_A 2
#define DEP_B 3


void input(void)
{
	char dummy;
	int hours, minutes;
	int NA, NB;
	int i;
	
	trains.clear();
	cin>>T>>NA>>NB;
	
	for(i=0; i<NA; ++i)
	{
		cin>>hours>>dummy>>minutes;
		trains.push_back(make_pair(hours*60+minutes, DEP_A));
		cin>>hours>>dummy>>minutes;
		trains.push_back(make_pair(hours*60+minutes+T, ARR_B));
	}
	
	for(i=0; i<NB; ++i)
	{
		cin>>hours>>dummy>>minutes;
		trains.push_back(make_pair(hours*60+minutes, DEP_B));
		cin>>hours>>dummy>>minutes;
		trains.push_back(make_pair(hours*60+minutes+T, ARR_A));
	}
	
	sort(trains.begin(), trains.end());
}

void calc(void)
{
	int i;
	int tA=0, tB=0;
	
	ansA=0;
	ansB=0;
	
	for(i=0; i<trains.size(); ++i)
	{
		switch(trains[i].second)
		{
			case ARR_A:
				++tA;
				break;
			case ARR_B:
				++tB;
				break;
			case DEP_A:
				if(!tA)
				{
					++ansA;
				}
				else
				{
					--tA;
				}
				break;
			case DEP_B:
				if(!tB)
				{
					++ansB;
				}
				else
				{
					--tB;
				}
				break;
		}
	}
}

int main(void)
{
	int N, i;
	
	cin>>N;
	
	for(i=1; i<=N; ++i)
	{
		input();
		calc();
		cout<<"Case #"<<i<<": "<<ansA<<" "<<ansB<<endl;
	}
	return 0;
}
