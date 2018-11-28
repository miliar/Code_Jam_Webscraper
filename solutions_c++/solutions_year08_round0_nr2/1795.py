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

int main()
{
#ifdef FILE_INPUT
	file_in.open(L"in.txt");
	file_out.open(L"out.txt");
#endif

	is_>>zcnt;

	for(int zi=1; zi<=zcnt; zi++)
	{
		bool is_swap=false;
		vector<timetalbe> alist, blist;
		int acnt, bcnt;
		int wt;
		int ansa = 0, ansb = 0;
		is_>>wt;
		is_>>acnt>>bcnt;
		input_data(alist, acnt);
		input_data(blist, bcnt);

		sort(alist.begin(), alist.end(), cmp);
		sort(blist.begin(), blist.end(), cmp);

		if(alist.empty())
		{
			alist.swap(blist);
			is_swap = true;
		}
		else if(!blist.empty())
		{
			if(!cmp(alist[0], blist[0]))
			{
				alist.swap(blist);
				is_swap = true;
			}
		}

		vector<int> va, vb;
		int curn = 0;
		while(!alist.empty() || !blist.empty())
		{
			bool is_find = false;
			curn++;
			if(curn % 2)	// A -> B
			{
				if(alist.empty())
					continue;
				for(vector<int>::iterator it=va.begin(); it!=va.end(); it++)
				{
					if(*it <= alist[0].departure)
					{
						is_find = true;
						va.erase(it);
						break;
					}
				}
				vb.push_back(alist[0].arrival+wt);
				alist.erase(alist.begin());
				if(!is_find)
					ansa++;
				
			}else			// B -> A
			{
				if(blist.empty())
					continue;
				for(vector<int>::iterator it=vb.begin(); it!=vb.end(); it++)
				{
					if(*it <= blist[0].departure)
					{
						is_find = true;
						vb.erase(it);
						break;
					}
				}
				va.push_back(blist[0].arrival+wt);
				blist.erase(blist.begin());
				if(!is_find)
					ansb++;
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