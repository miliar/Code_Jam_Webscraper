#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <fstream>
#include <cstdio>

using namespace std;

ifstream inf;
ofstream outf;

int cc;

int time_conv(string str)
{
	int h,m;
	sscanf(str.c_str(), "%d:%d", &h, &m);
	return h*60 + m;
}

void read(vector<pair<int, int> > & vp, int cnt)
{
	string rst;
	pair<int, int> tt;
	vp.clear();
	for(int i=0; i<cnt; i++)
	{
		inf>>rst;
		tt.first	= time_conv(rst);
		inf>>rst;
		tt.second	= time_conv(rst);
		vp.push_back(tt);
	}
}

bool operator<(const pair<int, int> & c1, const pair<int, int> & c2)
{
	if(c1.first < c2.first)
		return true;
	else if(c1.first == c2.first)
	{
		if(c1.second < c2.second)
			return true;
		else
			return false;
	}else
		return false;
}

vector< pair<int, int> > train_a, train_b;
vector<int> ready_a, ready_b;
int wait_time;
bool infswap;
int a_count = 0, b_count = 0;

void optimal()
{
	sort(train_a.begin(), train_a.end());
	sort(train_b.begin(), train_b.end());

	if(train_a.empty())
	{
		train_a.swap(train_b);
		ready_a.swap(ready_b);
		infswap = !infswap;
		double tt=a_count;
		a_count = b_count;
		b_count = tt;
	}
	else if(!train_b.empty())
	{
		if(!(train_a[0]<train_b[0]))
		{
			train_a.swap(train_b);
			ready_a.swap(ready_b);
			infswap = !infswap;
			double tt=a_count;
			a_count = b_count;
			b_count = tt;
		}
	}
}

bool train_leave(vector< pair<int, int> > & src, vector<int> &sv, vector<int> &dv)
{
	if(src.empty())
		return false;

	for(vector<int>::iterator it=sv.begin(); it!=sv.end(); it++)
	{
		if(*it <= src[0].first)
		{
			sv.erase(it);
			dv.push_back(src[0].second+wait_time);
			src.erase(src.begin());
			return true;
		}
	}
	return false;
}


void get_answer()
{
		optimal();

		while(true)
		{
			bool inftrain_leaved = false;
			while(train_leave(train_a, ready_a, ready_b))
				inftrain_leaved = true;
			while(train_leave(train_b, ready_b, ready_a))
				inftrain_leaved = true;
			if(!inftrain_leaved)
			{
				optimal();
				ready_b.push_back(train_a[0].second + wait_time);
				train_a.erase(train_a.begin());
				a_count++;
			}
			if(train_a.empty() && train_b.empty())
				break;
		}
}

int main()
{
	inf.open(L"Train Timetable.in");
	outf.open(L"Train Timetable.txt");

	inf>>cc;

	for(int case_i=1; case_i<=cc; case_i++)
	{
		infswap = false;
		int acnt=0, bcnt=0;
		a_count = 0;
		b_count = 0;
		inf>>wait_time;
		inf>>acnt>>bcnt;
		read(train_a, acnt);
		read(train_b, bcnt);

		ready_a.clear();
		ready_b.clear();
		
		get_answer();

		if(infswap)
			outf<<"Case #"<<case_i<<": "<<b_count<<" "<<a_count<<endl;
		else
			outf<<"Case #"<<case_i<<": "<<a_count<<" "<<b_count<<endl;


	}

	inf.close();
	outf.close();
	return 0;
}