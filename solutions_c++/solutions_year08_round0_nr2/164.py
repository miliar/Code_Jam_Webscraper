#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <fstream>

using namespace std;

#define _s(x,y) {x+=y;y=x-y;x-=y;}

#define FILE_INPUT

#ifdef FILE_INPUT
	#define is_ file_in
	#define os_ file_out
#else
	#define is_ cin
	#define os_ cout
#endif

#ifdef FILE_INPUT
	ifstream file_in;
	ofstream file_out;
#endif

struct timetalbe
{
	int departure, arrival;
};

int zcnt;

int str_to_time(string str)
{
	int n1,n2;
	for(int i=0; i<str.length(); i++)
		if(str[i]==':')
			str[i] = ' ';
	istringstream iss(str);
	iss>>n1>>n2;
	return n1*60 + n2;
}

void input_data(vector<timetalbe> & vl, int cnt)
{
	string rst;
	timetalbe tt;
	vl.clear();
	for(int i=0; i<cnt; i++)
	{
		is_>>rst;
		tt.departure	= str_to_time(rst);
		is_>>rst;
		tt.arrival		= str_to_time(rst);
		vl.push_back(tt);
	}
}

bool cmp(const timetalbe& c1, const timetalbe& c2)
{
	if(c1.departure < c2.departure)
		return true;
	else if(c1.departure == c2.departure)
	{
		if(c1.arrival < c2.arrival)
			return true;
		else
			return false;
	}else
		return false;
}

vector<timetalbe> alist, blist;
vector<int> va, vb;
int wt;
bool is_swap;
int ansa = 0, ansb = 0;

void check_swap_ab()
{
	sort(alist.begin(), alist.end(), cmp);
	sort(blist.begin(), blist.end(), cmp);

	if(alist.empty())
	{
		alist.swap(blist);
		va.swap(vb);
		is_swap = !is_swap;
		_s(ansa, ansb);
	}
	else if(!blist.empty())
	{
		if(!cmp(alist[0], blist[0]))
		{
			alist.swap(blist);
			va.swap(vb);
			is_swap = !is_swap;
			_s(ansa, ansb);
		}
	}
}

bool move(vector<timetalbe> & src, vector<int> &sv, vector<int> &dv)
{
	if(src.empty())
		return false;

	for(vector<int>::iterator it=sv.begin(); it!=sv.end(); it++)
	{
		if(*it <= src[0].departure)
		{
			sv.erase(it);
			dv.push_back(src[0].arrival+wt);
			src.erase(src.begin());
			return true;
		}
	}
	return false;
}


int main()
{
#ifdef FILE_INPUT
	file_in.open(L"in.txt");
	file_out.open(L"out.txt");
#endif

	is_>>zcnt;

	for(int zi=1; zi<=zcnt; zi++)
	{
		is_swap = false;
		int acnt=0, bcnt=0;
		ansa = 0;
		ansb = 0;
		is_>>wt;
		is_>>acnt>>bcnt;
		input_data(alist, acnt);
		input_data(blist, bcnt);

		va.clear();
		vb.clear();

		check_swap_ab();

		while(!alist.empty() || !blist.empty())
		{
			bool is_moved = false;
			while(move(alist, va, vb))
				is_moved = true;
			while(move(blist, vb, va))
				is_moved = true;
			if(!is_moved)
			{
				check_swap_ab();
				vb.push_back(alist[0].arrival + wt);
				alist.erase(alist.begin());
				ansa++;
			}

		}
		

		if(is_swap)
			os_<<"Case #"<<zi<<": "<<ansb<<" "<<ansa<<endl;
		else
			os_<<"Case #"<<zi<<": "<<ansa<<" "<<ansb<<endl;


	}


#ifdef FILE_INPUT
	file_in.close();
	file_out.close();
#endif
	return 0;
}