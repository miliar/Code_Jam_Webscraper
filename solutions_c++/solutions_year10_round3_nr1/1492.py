#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)

//vector<int> v;
//for(vector<int>::iterator it = v.begin(), end = v.end(); it != end; ++it)
//{
//}


bool intersect(int x1, int x2, int y1, int y2)
{
	vector<int> v;
	v.push_back(x1);
	v.push_back(x2);
	v.push_back(y1);
	v.push_back(y2);

	sort(v.begin(), v.end());

	return !((v.front()==x1 && v.back()==y2) || (v.front()==x2 && v.back()==y1) || (v.front()==y1 && v.back()==x2) || (v.front()==y2 && v.back()==x1));
}

int main(int argc, char* argv[])
{
	std::ifstream input_file("in");
	std::ofstream output_file("out");

	size_t count_tests = 0;
	input_file >> count_tests;

	REP (t, count_tests)
	{
		int n = 0;
		input_file >> n;
		////

		vector<pair<int, int>> v;
		REP (i, n)
		{
			int x=0,y=0;
			input_file>>x>>y;
			v.push_back(pair<int,int>(x,y));
		}

		int cnt = 0;

		REP (i, n-1)
		{
			FOR (j, i+1, n)
				if (intersect(v[i].first, v[i].second, v[j].first, v[j].second)) ++cnt;
		}

		////
		output_file << "Case #" << t+1 << ": ";
		output_file << cnt << std::endl;	
	}

	input_file.close();
	output_file.close();

	return 0;
}