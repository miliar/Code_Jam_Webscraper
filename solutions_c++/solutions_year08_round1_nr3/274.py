#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <math.h>


using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FORE(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define CLEAR(x,with) memset(x,with,sizeof(x))  

#define pb push_back
#define all(x) (x).begin(),(x).end()
#define sz(a) int((a).size())

typedef pair<int,int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

int main()
{
	int numCases;
	cin >> numCases;

	vector< vector<int> > ans;

	pair<int, int> ff = make_pair(3, 1);
	pair<int, int> gg = ff;
	for(int i=2; i<=30; i++)
	{
		pair<int, int> hh;
		hh.first = ff.first * gg.first + ff.second * gg.second * 5;
		hh.second = ff.first * gg.second + ff.second * gg.first;
		gg.first = hh.first % 1000;
		gg.second = hh.second % 1000;

		long double num = (long double)gg.first + (long double)gg.second * (long double)sqrt(5.);

		long long num_int = (long long) num;
		num_int %= 1000;

		vector<int> temp;
		long long temp2 = num_int / 100;
		temp.push_back( temp2 );
		num_int -= temp2 * 100;
		temp2 = num_int / 10;
		temp.push_back( temp2 );
		num_int -= temp2 * 10;
		temp.push_back( num_int );

		ans.push_back(temp);

	}

	vector<string> data; // used windows calculator to calculate data
	
data.push_back("027");
data.push_back("143");
data.push_back("751");
data.push_back("935");
data.push_back("607");
data.push_back("903");
data.push_back("991");
data.push_back("335");
data.push_back("047");
data.push_back("943");
data.push_back("471");
data.push_back("055");
data.push_back("447");
data.push_back("463");
data.push_back("991");
data.push_back("095");
data.push_back("607");
data.push_back("263");
data.push_back("151");
data.push_back("855");
data.push_back("527");
data.push_back("743");
data.push_back("351");
data.push_back("135");
data.push_back("407");
data.push_back("903");
data.push_back("791");
data.push_back("135");
data.push_back("647");


	for(int c=1; c<=numCases; c++)
	{
		int exp;
		cin >> exp;

		cout << "Case #" << c << ": ";
		cout << data[exp-2];
		cout << endl;
	}

	return 0;
}
