// t1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <assert.h>

using namespace std;

struct train_record
{
	int time;
	int count;
	bool operator<(const train_record &r) 
	{
		if (time<r.time) return true;
		else if (time==r.time) return count>r.count;//if count=+1 then it must be higher than with -1 value
		else return false;
		//or just (time<r.time) || (time==r.time?count>r.count:false)
	}
	train_record(int t,int c):time(t),count(c) {}
} ;
typedef vector<train_record> trains_vector;

int read_time(istream &in)
{
	string tmp;
	in>>tmp;
	int hr=(tmp[0]-'0')*10+(tmp[1]-'0');
	assert(tmp[2]==':');
	int min=(tmp[3]-'0')*10+(tmp[4]-'0');
	//std::cout<<"dbg:read_time hr*100,not hr*60!!\n";
	return hr*60+min;
}

void read_timetable(istream &in,int record_count,int turnaround_time,trains_vector &from,trains_vector &to)
{
	string tmp;
	for (int i=0;i<record_count;++i)
	{
		int time_from=read_time(in);
		int time_to=read_time(in);		
		from.push_back(train_record(time_from,-1));
		to.push_back(train_record(time_to+turnaround_time,+1));		
	}
}

int calc_trains(const trains_vector &traffic)
{
	int c=0,cmin=0;
	for (trains_vector::const_iterator it=traffic.begin();it<traffic.end();++it)
	{
		c+=it->count;
		cmin=min(cmin,c);
	}
	return -cmin;
}

trains_vector traffic_A,traffic_B;
int main(int argc, _TCHAR* argv[])
{
	traffic_A.reserve(200);
	traffic_B.reserve(200); 
	
	int N;
	//1
	//ifstream fin("d:/fun/qr/TrainTimetable/B-small-attempt0.in");
	//ofstream fout("d:/fun/qr/TrainTimetable/B-small.output");
	//2
	ifstream fin("d:/fun/qr/TrainTimetable/B-large.in");
	ofstream fout("d:/fun/qr/TrainTimetable/B-large.output");

	fin>>N;
	assert(fin.good());
	assert(fout.good());

	int turnaround_time;
	string tmp;

	for(int i_case=1;i_case<=N;++i_case)
	{		
		cout<<i_case<<"\n";
		traffic_A.clear();
		traffic_B.clear();
		fin>>turnaround_time;
		int NA,NB;
		fin>>NA>>NB;
		getline(fin,tmp);
		assert(tmp.empty());
		read_timetable(fin,NA,turnaround_time,traffic_A,traffic_B);
		read_timetable(fin,NB,turnaround_time,traffic_B,traffic_A);
		sort(traffic_A.begin(),traffic_A.end());
		sort(traffic_B.begin(),traffic_B.end());
		int trains_A=calc_trains(traffic_A);
		int trains_B=calc_trains(traffic_B);
		fout<<"Case #"<<i_case<<": "<<trains_A<<" "<<trains_B<<"\n";
	}
	fout.close();
	assert(fout.good());
	assert(fin.good() || fin.eof());

	std::cout<<"\7Done\n";
	int k;std::cin>>k;
	return 0;
}

