// google.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

std::string garbage;

int read_time(std::ifstream & fs)
{
	int hh = 0;
	int mm = 0;
	char ch = 0;
	fs >> hh >> ch >> mm;
	return hh * 60 + mm;
}

// If departures the same, sent first the train with early arrival
static bool less_first(const std::pair<int,int> & a, const std::pair<int,int> & b)
{
	if( a.first != b.first )
		return a.first < b.first;
	return a.second < b.second;
}

int to = 0;

void send_train(int station, const std::pair<int,int> & tr, std::vector<int> * arrived, int * total)
{
	std::cout << station << std::endl;
	int other = 1 - station;
	if( arrived[station].empty() || arrived[station][0] > tr.first ) // No train available
	{
		total[station] += 1;
	}
	else
		arrived[station].erase(arrived[station].begin());
	arrived[other].push_back(tr.second + to);
	std::sort(arrived[other].begin(), arrived[other].end());
}

void solve_case(int cas, std::ifstream & fs, std::ofstream & ofs)
{
	fs >> to;
	std::getline(fs, garbage);

	int n[2] = {0};
	std::vector< std::pair<int,int> > sched[2];
	int pos[2] = {0};

	fs >> n[0];
	fs >> n[1];
	std::getline(fs, garbage);

	for(int st = 0; st != 2; ++st)
	{
		sched[st].resize( n[st] );
		for(int i = 0; i != n[st]; ++i)
		{
			sched[st][i].first = read_time(fs);
			sched[st][i].second = read_time(fs);
			std::getline(fs, garbage);
		}
		std::sort(sched[st].begin(), sched[st].end(), less_first);
	}
	std::vector<int> arrived[2];
	int total[2] = {0, 0};

	while(pos[0] != sched[0].size() && pos[1] != sched[1].size())
	{
		if( less_first(sched[0][pos[0]], sched[1][pos[1]]) )
		{
			send_train(0, sched[0][pos[0]], arrived, total);
			pos[0] += 1;
		}
		else
		{
			send_train(1, sched[1][pos[1]], arrived, total);
			pos[1] += 1;
		}
	}
	while(pos[0] != sched[0].size())
	{
		send_train(0, sched[0][pos[0]], arrived, total);
		pos[0] += 1;
	}
	while(pos[1] != sched[1].size())
	{
		send_train(1, sched[1][pos[1]], arrived, total);
		pos[1] += 1;
	}
	ofs << "Case #" << cas << ": " << total[0] << " " << total[1] << std::endl;
}

int main(int argc, char * argv[])
{
	std::ifstream fs("input.txt");
	std::ofstream ofs("output.txt");
	int n_cases = 0;
	fs >> n_cases;
	std::getline(fs, garbage);
	for(int c = 0; c != n_cases; ++c)
	{
		solve_case(c + 1, fs, ofs);
	}
	return 0;
}
