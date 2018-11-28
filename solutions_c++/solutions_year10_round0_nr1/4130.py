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

//vector<long long>	inpt;
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

string process_testcase(int n, int k)
{
	string rv = "OFF";
	unsigned long long mask = 0;
	for(unsigned int i = 0; i < n; i++)
	{
		mask <<= 1;
		mask |= 1;
	}
	cout << " n,k == " << n << " ," << k;
	if(mask == (mask & k))
		rv = "ON";

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
		is.open("C:\\Users\\viv.NTDEV\\ipfile.in");
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
		int n;
		int k;
		getline(is,ss); 
		istringstream iss(ss);
		iss >> n >> k;

		cout << process_testcase(n, k) << endl;
	}
	is.close();
	return 0;
}
