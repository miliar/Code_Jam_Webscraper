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

typedef vector<int> Vec;

void solve_a_case(ifstream &in, int &r)
{
	// input
	int num;
	in >> num;

	Vec vec;
	for(int i=0; i<num; ++i)
	{
		int t;
		in >> t;
		vec.push_back(t);
	}
	sort(vec.begin(), vec.end());

	int t = 0x0;
	for(int i=0; i<vec.size(); ++i)
	{
		t ^= vec[i];
	}

	r = 0;
	if (t!=0)
	{
		r = -1;
	}
	else
	{
		for(int i=1; i<vec.size(); ++i)
		{
			r += vec[i];
		}
	}
}

void solve_all_cases(ifstream &in, ofstream &out)
{
	int case_num = 0;

	in >> case_num;
	for(int i=0; i<case_num; i++)
	{
		int r = -1;
		solve_a_case(in, r);

		out << "Case #" << i+1 << ": ";
		if (r==-1)
			out << "NO";
		else
			out << r;
		out << endl;
	}
}

int main()
{
#if 0
	ifstream in("in.txt");
	ofstream out("out.txt");
#elif 0
	ifstream in("C-small-attempt0.in");
	ofstream out("C-small-attempt0.out");
#elif 1
	ifstream in("C-large.in");
	ofstream out("C-large.out");
#endif

	solve_all_cases(in, out);

	return 0;
}
