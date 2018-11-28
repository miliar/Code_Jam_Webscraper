#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <stack>
#include <iomanip>
#include <list>
#include <string>
#include <sstream>

using namespace std;

struct Robot
{
	int pos;
	int time;
};

void step(int pos, Robot &i, Robot &y)
{
	if (i.time>=y.time)
	{
		int d_pos = abs(pos-i.pos);
		i.time += d_pos+1;
	}
	else
	{
		int d_time = y.time-i.time;
		int d_pos = abs(pos-i.pos);
		if (d_time<d_pos)
		{
			i.time += d_pos+1;
		}
		else
		{
			i.time = y.time+1;
		}
	}
	i.pos = pos;
}

void solve_a_case(ifstream &in, int &r)
{
	// input
	int num;
	in >> num;

	Robot orange;
	orange.pos = 1;
	orange.time = 0;

	Robot blue;
	blue.pos = 1;
	blue.time = 0;

	for(int i=0; i<num; ++i)
	{
		string color;
		int pos;
		in >> color;
		in >> pos;

		if (color=="O")
		{
			step(pos, orange, blue);
		}
		if (color=="B")
		{
			step(pos, blue, orange);
		}
	}

	r = max(orange.time, blue.time);
}

void solve_all_cases(ifstream &in, ofstream &out)
{
	int case_num = 0;

	in >> case_num;
	for(int i=0; i<case_num; i++)
	{
		int r = -1;
		solve_a_case(in, r);

		out << "Case #" << i+1 << ": " << r << endl;
	}
}

int main()
{
#if 0
	ifstream in("in.txt");
	ofstream out("out.txt");
#elif 0
	ifstream in("A-small-attempt1.in");
	ofstream out("A-small-attempt1.out");
#elif 1
	ifstream in("A-large.in");
	ofstream out("A-large.out");
#endif

	solve_all_cases(in, out);

	return 0;
}
