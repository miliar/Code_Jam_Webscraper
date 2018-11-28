#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <list>
#include <bitset>
#include <cstring>
#include <sys/time.h>
#include <sys/signal.h>
#include <unistd.h>
#include <stack>
#include <cmath>
#include <map>
#include <streambuf>
#include <ctime>

using namespace std;

typedef unsigned long long int uint64;
typedef pair<uint64, uint64> range;
typedef vector<range> rangesVector;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
#define FOR(x,a,e) for( x=a; x<=(e); ++x)
#define FORL(x,a,e) for(int x=a; x<(e); ++x)
#define FORD(x,a,e) for(int x=a; x>=(e); --x)
#define FORDG(x,a,e) for(int x=a; x>(e); --x)
#define REP(x,n) for(int x =0;x<(n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) (c).begin(),(c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i,c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

uint64 to10(vector<string> n, int base)
{
	reverse(ALL(n));
	int p = 0;
	uint64 result = 0;
	FOREACH(it, n)
	{
		stringstream iss(*it);
		int nn;
		iss >> nn;
		result += nn * (uint64)pow((float)base,p++);
	}
	return result;
}


int main()
{
	int N;
	cin >> N;
	int k;

	FOR(k, 1, N)
	{
		string s;
		cin >> s;
		int d = 0;

		map<char, bool> seen;
		FOREACH(it,s)
		{
			if (seen.find(*it) == seen.end())
			{
				++d;
				seen[*it] = true;
			}
		}
		if (d==1) ++d;
		//cout<<d<<endl;

		VI digits;
		digits.PB(1);
		digits.PB(0);
		int i;
		FORL(i, 2, d)
		{
			digits.PB(i);
		}

		map<char, int> relations;
		int c = 0;
		VS iss;
		FOREACH(it,s)
		{
			if (relations.find(*it) != relations.end())
			{
				stringstream ss;
				ss << relations[*it];
				iss.PB(ss.str());
			}
			else
			{
				relations[*it] = digits[c];
				stringstream ss;
				ss << digits[c];
				iss.PB(ss.str());
				++c;
			}
		}

		uint64 result = to10(iss,d);
		cout<<"Case #"<<k<<": "<<result<<endl;
	}
}
