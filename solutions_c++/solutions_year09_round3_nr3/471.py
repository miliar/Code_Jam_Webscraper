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

long long process(int pp, vector<int> &seq)
{
	long long rv = 0;

	vector<int> jail;

	dfo(i, pp+1)
		jail.push_back(1);

	dfo(i, seq.size())
	{
		jail[seq[i]] = 0;
		dfor(j, seq[i]+1, jail.size())
		{
			if(jail[j] == 0)
				break;
			else
				rv++;
		}
		drof(j, seq[i]-1, 1)
		{
			if(jail[j] == 0)
				break;
			else
				rv++;
		}
	}

	return rv;
}

long long process_testcase(vector<int> &priz)
{
	long long rv = 0x0FFFFFFFFFFFFLL;

	sort(priz.begin(), priz.end());

	do{
		long long cur_min = process(p, priz);
		if(cur_min < rv)
		{
			rv = cur_min;
		}
	}while(next_permutation(priz.begin(), priz.end()));

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
		is.open("d:\\ipfile.in");
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
		istringstream iss(ss);
		iss >> p >> q;

		string zz;
		getline(is,zz); 
		istringstream izz(zz);
		//printf("<<%d>>--->", n);
		vector<int> priz;
		dfo(j, q)
		{
			int pris;
			izz>>pris;
			//cout << pris <<endl;
			priz.push_back(pris);
		}
		cout << process_testcase(priz) << endl;
	}
	is.close();
	return 0;
}
