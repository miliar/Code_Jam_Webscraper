#include <fstream>
#include <iostream>
#include <string>
#include <set>
#include <list>
#include <vector>
#include <iomanip>
using namespace std;

string readline(istream & cin, int nmax = 1024)
{
	char *c = new char[nmax];
	cin.getline(c,nmax);
	string s(c);
	delete c;
	return s;
}

struct time
{
	int h, m;
	int value()
	{
		return h*60 + m;
	}
};

struct time_interval
{
	time start, end;
	pair<int,int> value()
	{
		return make_pair(start.value(),end.value());
	}
};

struct Station
{
	int start_trains;
	multiset<int> available_trains;

	Station():start_trains(0)
	{
		
	}
};


const int A = 0;
const int B = 1;

typedef multiset< pair<pair< int,int >, int> > Schedule;
typedef Schedule::iterator Train;

void testcase(istream &fin, int& a, int &b)
{
	int t_a;
	int n_a, n_b;
	int i;

	fin >> t_a;
	fin >> n_a >> n_b;

	Schedule sched;

	readline(fin);

	time_interval t_i;

	for(i=0;i<n_a;++i)
	{
		sscanf(readline(fin).c_str(),"%2d:%2d %2d:%2d", &t_i.start.h, &t_i.start.m, &t_i.end.h, &t_i.end.m);
		sched.insert( make_pair(t_i.value(), A));
	}

	for(i=0;i<n_b;++i)
	{
		sscanf(readline(fin).c_str(),"%2d:%2d %2d:%2d", &t_i.start.h, &t_i.start.m, &t_i.end.h, &t_i.end.m);
		sched.insert( make_pair(t_i.value(), B));
	}

	
	vector<Station> s_vec(2);

	for (Train sch = sched.begin(); sch != sched.end(); ++sch)
	{
		Station &s = s_vec[0+sch->second];
		Station &o = s_vec[1-sch->second];

		int now = sch->first.first;
		
		multiset<int>::iterator it = s.available_trains.begin();
		if(it == s.available_trains.end() || *it > now )
		{
			s.start_trains++;
		}
		else
		{
			s.available_trains.erase(s.available_trains.begin());
		}
		o.available_trains.insert(sch->first.second + t_a);
	}

	a = s_vec[A].start_trains;
	b = s_vec[B].start_trains;

}



int main(int argc, char* argv[])
{
	if (argc < 2) return -1;

	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	int n;

	fin >> n;

	for (int i = 1; i <= n; ++i)
	{
		int a,b;
		testcase(fin,a,b);		
		fout << "Case #" << i <<": "<< a << " " << b << "\n";
	}
	return 0;
}

