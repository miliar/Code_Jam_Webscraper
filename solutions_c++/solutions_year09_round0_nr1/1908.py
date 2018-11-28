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
#include <boost/regex.hpp>

using namespace std;

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


void find_and_replace( string &source, const string find, string replace ) {
 
	size_t j;
	for ( ; (j = source.find( find )) != string::npos ; ) {
		source.replace( j, find.length(), replace );
	}
}

int main()
{
	int L , D , N;
	int i;
	cin >> L;
	cin >> D;
	cin >> N;

	vector<string> words;
	FORL(i,0,D)
	{
		string tmp;
		cin >> tmp;
		words.PB(tmp);
	}

	FORL(i,0,N)
	{
		//cout<<"Case no "<<i+1<<endl;
		int res = 0;
		string data;
		cin >> data;

		find_and_replace(data, "(" , "[");
		find_and_replace(data, ")" , "]");

		//cout<<"Regex = "<<data<<endl;
		FOREACH(it, words)
		{
			boost::regex regexp(data);
			boost::smatch what;

			//cout<<"Matching with "<<*it<<endl;
			if(boost::regex_match(*it, what, regexp))
			{
				++res;
			}
			//else
			//	cout<<"Not matching...\n";
		}
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
}
