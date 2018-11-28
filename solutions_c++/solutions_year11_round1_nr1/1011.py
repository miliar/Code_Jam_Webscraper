#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <stack>
#include <iomanip>
#include <list>
#include <string>
#include <sstream>

//#define IN	"in.txt"
//#define OUT	"out.txt"

#define	T1 "A"

#define	T2 "0"
//#define IN	T1"-small-attempt"T2".in"
//#define OUT	T1"-small-attempt"T2".out"

#define IN	T1"-large.in"
#define OUT	T1"-large.out"

using namespace std;

typedef vector<long long int> Vec;

void out(const Vec &v)
{
	for(int i=0; i<v.size(); ++i)
	{
		cout << v[i] << endl;
	}
	cout << endl;
}

void sort(Vec &v)
{
	sort(v.begin(), v.end());
}

void solve_a_case(ifstream &in, bool &r)
{
	// input
	long long int n, pd, pg;
	in >> n >> pd >> pg;

	if (pd == 0 && pg == 0)
	{
		r = true;
		return;
	}
	else if (pd == 0 && pg == 100)	// D>0
	{
		r = false;
		return;
	}
	else if (pd > 0 && pg == 0)
	{
		r = false;
		return;
	}
	else if (pd == 100 && pg == 100)
	{
		r = true;
		return;
	}
	else if (pd < 100 && pg == 100)
	{
		r = false;
		return;
	}


	Vec d;
	for(long long int i=1; i<=n; ++i)
	{
		if (i*pd%100 == 0)
		{
			r = true;
			return;
		}
	}
	//if (d.empty())
	//{
	//	r = false;
	//	return;
	//}
	//else
	//{
	//	r = true;
	//	return;
	//}

	//for(int i=0; i<d.size(); ++i)
	//{
	//	int a = d[i];
	//	int b = a*pd/100;
	//	int c = pg;

	//	int x1 = a*c-100*b;
	//	int x2 = 100-c;
	//	if (x1>=0 && x1%x2 == 0)
	//	{
	//		r = true;
	//		return;
	//	}

	//	//int di = d[i];
	//	//int w = ;
	//	//bool ok1 = 100*w%pg == 0;
	//	//int g = 100*w/pg;
	//	//bool ok2 = g>=di;
	//	//if (ok1 && ok2)
	//	//{
	//	//	r = true;
	//	//	return;
	//	//}
	//}

	//r = false;
}

void solve_all_cases(ifstream &in, ofstream &out)
{
	int case_num = 0;

	in >> case_num;
	for(int i=0; i<case_num; i++)
	{
		bool r = false;
		solve_a_case(in, r);

		out << "Case #" << i+1 << ": ";
		if (r)
			out << "Possible";
		else
			out << "Broken";
		out << endl;
	}
}

int main()
{
	ifstream in(IN);
	ofstream out(OUT);

	solve_all_cases(in, out);

	return 0;
}
