// b-trains.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <algorithm>

using namespace std;

unsigned int min(list<unsigned int> &l)
{
	unsigned int m = (-1);
	for(list<unsigned int>::iterator it = l.begin(); it != l.end(); it++)
	{
		if ((*it)<m)
			m = (*it);
	}
	return m;
}

unsigned int t_t_m(char* s)
{
	s[2]=0;
	int h = atoi(s);
	int m = atoi(&s[3]);
	return (h*60+m);
}

class TrainTrip
{
public:
	TrainTrip(FILE* f, int t)
	{
		char b[6];
		fscanf(f,"%s",b);
		td = t_t_m(b);
		fscanf(f,"%s",b);
		ta = t_t_m(b)+t;
	}
	unsigned int td;
	unsigned int ta;
};
class TOrder
{
public:
bool operator()(TrainTrip *a, TrainTrip *b)
{
	return (a->td>b->td);
}
};

class TOrder2
{
public:
	bool operator()(TrainTrip *a, TrainTrip *b)
	{
		return (a->ta>b->ta);
	}
};

class Case
{
public:
	Case(FILE* f) : t_i_a(0),t_i_b(0),n_t_i_a(0),n_t_i_b(0)
	{
		fscanf(f,"%d %d %d",&t,&na,&nb);
		//printf("%d %d %d",t,na,nb);
		for(int i=0;i<na;i++)
		{
			TrainTrip* tmp = new TrainTrip(f,t);
			t_f_a.push_back(tmp);
		}
		TOrder as;
		sort(t_f_a.begin(),t_f_a.end(),as);
		for(int i=0;i<nb;i++)
		{
			TrainTrip* tmp = new TrainTrip(f,t);
			t_f_b.push_back(tmp);
		}
		sort(t_f_b.begin(),t_f_b.end(),as);
	}

	void Simulate()
	{
		TOrder2 ord;
		while(!(t_f_a.empty()&&t_f_b.empty()))
		{
			//Check next event time;
			std::list<unsigned int> times;
			if(!t_f_a.empty())
				times.push_back(t_f_a.back()->td);
			if(!t_f_b.empty())
				times.push_back(t_f_b.back()->td);
			if(!t_t_a.empty())
				times.push_back(t_t_a.back()->ta);
			if(!t_t_b.empty())
				times.push_back(t_t_b.back()->ta);
			CurrentTime = min(times);
			if(!t_t_a.empty())
			{
				if(t_t_a.back()->ta==CurrentTime)
				{
					t_t_a.pop_back();
					t_i_a++;
				}
			}
			if(!t_t_b.empty())
			{
				if(t_t_b.back()->ta==CurrentTime)
				{
					t_t_b.pop_back();
					t_i_b++;
				}
			}
			if(!t_f_a.empty())
			{
				if(t_f_a.back()->td==CurrentTime)
				{
					getTrainFromA();
					t_t_b.push_back(t_f_a.back());
					sort(t_t_b.begin(),t_t_b.end(),ord);
					t_f_a.pop_back();
				}
			}
			if(!t_f_b.empty())
			{
				if(t_f_b.back()->td==CurrentTime)
				{
					getTrainFromB();
					t_t_a.push_back(t_f_b.back());
					sort(t_t_a.begin(),t_t_a.end(),ord);
					t_f_b.pop_back();
				}
			}

		}
		cout << n_t_i_a << " " << n_t_i_b << endl;
	}

private:

	unsigned int CurrentTime;

	void getTrainFromA()
	{
		if(t_i_a>0)
			t_i_a--;
		else
			n_t_i_a++;
	}
	void getTrainFromB()
	{
		if(t_i_b>0)
			t_i_b--;
		else
			n_t_i_b++;
	}

	

	unsigned int t;
	unsigned int na;
	unsigned int nb;
	vector<TrainTrip*> t_f_a;
	vector<TrainTrip*> t_f_b;
	vector<TrainTrip*> t_t_a;
	vector<TrainTrip*> t_t_b;
	unsigned int t_i_a;
	unsigned int t_i_b;
	unsigned int n_t_i_a;
	unsigned int n_t_i_b;
};

int _tmain(int argc, _TCHAR* argv[])
{
	if(argc!=2)
		return 1;
	FILE* f = fopen(argv[1],"r");
	unsigned int total;
	fscanf(f,"%d",&total);
	for(int i=0;i<total;i++)
	{
		Case c(f);
		cout << "Case #" << (i+1) << ": ";
		c.Simulate();
	}
	return 0;
}

