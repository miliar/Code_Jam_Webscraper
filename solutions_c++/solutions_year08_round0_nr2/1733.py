#ifndef CODEJAM_H
#define CODEJAM_H

#include <iostream>
#include <string>
#include <stack>
#include <fstream>
#include <math.h>
#include <map>
#include <algorithm>
#include <vector>
#include <crtdbg.h>
using namespace std;

#define FOR0(i,b)	for(int i=0,_b=(int)(b);i<_b;i++)
#define FOR1(i,b)	for(int i=1,_b=(int)(b);i<=_b;i++)
#define LOG(s,ss)	cout<<s<<""<<ss<<endl;
#define FORE(e,c,Ty) for(vector<Ty*>::iterator e=(c).begin();e!=(c).end();e++)

// functions declaraion
void tt(ifstream &input);
#endif

enum DI{DAB, DBA};
int T, NA, NB;
enum STATUS{SA, SB, SAB, SBA};

struct TimeTableItem
{
	TimeTableItem(int s, int e, DI di)
		:st(s),ed(e),d(di){}
	int st;
	int ed;
	DI d;
};

class Train
{
public:
	Train(TimeTableItem* t):m_time(t){m_st=(t->d==DAB)?SAB:SBA;}
	STATUS checkStatus(int curTime)
	{
		if (!m_time) return m_st;
		if (curTime >= m_time->ed+T)
		{
			if (m_time->d == DAB) m_st = SB;
			else m_st = SA;
			m_time = 0;
		}
		return m_st;
	}
	void go(TimeTableItem* t)
	{
		_ASSERT(t);
		_ASSERT(!m_time);
		_ASSERT((t->d==DAB && m_st==SA)||(t->d==DBA && m_st==SB));
		m_time = t;
		m_st=(t->d==DAB)?SAB:SBA;
	}
private:
	TimeTableItem* m_time;
	STATUS m_st;
};

class Station
{
public:
	Station():m_A(0),m_B(0){}
	~Station(){clear();}
	void dispatch(TimeTableItem *tti);
	void report(int &a, int &b){a=m_A;b=m_B;}
	void clear()
	{
		FOR0(n,trList.size())delete trList[n];
		m_A = m_B = 0;
		trList.clear();
	}
private:
	vector<Train*> trList;
	int m_A;
	int m_B;
};

void Station::dispatch(TimeTableItem *tti)
{
	_ASSERT(tti);
	FORE(e,trList,Train)
	{
		STATUS sta = (*e)->checkStatus(tti->st);
		if ((tti->d==DAB && sta==SA) ||
			(tti->d==DBA && sta==SB))
		{
			(*e)->go(tti); break;
		}
	}
	if (e == trList.end())
	{
		trList.push_back(new Train(tti));
		if (tti->d==DAB)m_A++;
		else m_B++;
	}
}

class TimeTable
{
public:
	TimeTable() {}
	~TimeTable() {clear();}
	void run(int &a, int &b);
	void clear()
	{
		FOR0(n,tt.size()) delete tt.at(n);
		tt.clear();
		s.clear();
	}
	void setTime(char* time, DI d)
	{
		char sh[3]={0},sm[3]={0};
		char eh[3]={0},em[3]={0};
		strncpy(sh, time, 2);
		strncpy(sm, time+3, 2);
		strncpy(eh, time+6, 2);
		strncpy(em, time+9, 2);
		int s = atoi(sh)*60+atoi(sm);
		int e = atoi(eh)*60+atoi(em);
		tt.push_back(new TimeTableItem(s,e,d));
	}
private:
	Station s;
	vector<TimeTableItem*> tt;
};

bool cmp(TimeTableItem *a, TimeTableItem *b)
{
	return (a->st < b->st);
}

void TimeTable::run(int &a, int &b)
{
	if (tt.empty()) {a = b = 0; return;}
	sort(tt.begin(), tt.end(), cmp);
	//FORE(e,tt,TimeTableItem)LOG("TIME_TABLE:", (*e)->st);
	FOR0(n,tt.size()) s.dispatch(tt[n]);
	s.report(a, b);
}

void tt(ifstream &input)
{
	int cases;
	char time[64] = {0};
	int A=-1, B=-1;
	input >> cases;
	TimeTable t;
	FOR1(z,cases)
	{
		t.clear();
		input >> T >> NA >> NB; input.getline(time,64);
		FOR1(i,NA) {input.getline(time,64); t.setTime(time,DAB);}
		FOR1(j,NB) {input.getline(time,64); t.setTime(time,DBA);}
		t.run(A, B);
		cout << "Case #" << z << ": " << A << " " << B << "\n";
	}
	cout.flush();
}
int main(int argc, char *argv[])
{

	char filename[64] = {0};
	if (argc > 1)
		strcpy(filename, argv[1]);
	else
		strcpy(filename, "input.jam");

	std::ifstream input(filename);

	if (!input.is_open())
	{
		cout << "Warning: unable to open input file -- " << filename << endl;
		return 1;
	}

	
	tt(input);
	return 0;
}