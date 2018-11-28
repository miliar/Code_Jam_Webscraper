#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

vector<long long>	inp;
long long p,q;

typedef vector<int>		dvi;
typedef long long		dll;
typedef istringstream	dios;

// always pass a value (rather than someVecOrString.size()) to these macros. 
// that way optimizer can perform a better job.
#define dsz(i,v)	(i) = (v).size()
#define dsl(i,v)	(i) = (v).length()

#define dfor(i,b,e)	for(int i = (b); i < (e);  i++)
#define drof(i,b,e)	for(int i = (b); i >= (e); i--)
#define dfo(i,n)	for(int i = 0;   i < (n);  i++)
#define dof(i,n)	for(int i = (n); i >= 0;   i--)
#define dfo1(i,n)	for(int i = 1;   i < (n);  i++)
#define dof1(i,n)	for(int i = (n); i >= 1;   i--)

#define dall(c) c.begin(), c.end()
#define dpb push_back


long long process_testcase(string n)
{
	long long rv = 0;

	vector<char> uniq;
	dfo(i, n.size()){
		if(find(uniq.begin(), uniq.end(), n[i]) == uniq.end()){
			uniq.push_back(n[i]);

		}else{
			continue;
		}
	}

	unsigned long long base = uniq.size();
	vector<int> vals;
	vals.push_back(1);
	vals.push_back(0);

	int x = 2;
	dfo(i, uniq.size())
	{
		vals.push_back(x);
		x++;
	}


	vector<int> rvec;
	dfo(i, n.size())
	{
		dfo(j, uniq.size())
		{
			if(n[i] == uniq[j])
			{
				rvec.push_back(vals[j]);
				break;
			}
		}
	}

	if(base == 1)
		base++;

	unsigned long long cur_mult = 1;

	rv = 0;
	drof(i, rvec.size()-1, 0)
	{
		rv += (cur_mult * rvec[i]);
		cur_mult *= base;
	}	

	return rv;
}

void display_output(long long rv)
{
	printf("%04d\n", rv);
}

int main(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
	if(argc == 1)
		is.open("d:\\A-large.in");
	else
		is.open(argv[1]);

	// find total number of testcases
	string s;
	getline(is,s); 
	istringstream iss(s);
	iss >> tc;
	//printf("num tc == %d\n", tc);

	// for every testcase
	for(int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ",i);
		// find number of lines for this testcase
		string ss;
		getline(is,ss); 
		//istringstream iss(ss);
		//iss >> p >> q;

		//printf("<<%d>>--->", n);
		cout << process_testcase(ss) << endl;
	}
	is.close();
	return 0;
}
