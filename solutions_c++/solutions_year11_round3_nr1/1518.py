

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <list>
#include <set>

#define FOR(a,b,c) for(int a = (b); a < (c); ++a)
#define FORI(a,b) for((a)::iterator b = (a).begin(); b < (a).end(); ++b)
#define REP(a,b) for(int a = 0; a < (b); ++a)

using std::cin;
using std::cout;
using std::endl;

using std::vector;
using std::string;
using std::pair;
using std::list;
using std::set;

using std::make_pair;


bool still_contains_blue(vector<vector<int>> &v)
{
	REP(i,v.size())
		REP(j,v[i].size())
		{
			if (v[i][j] == 1)
				return true;
		}
	return false;
}

void test_case(int case_num)
{
	int x, y;
	cin >> y >> x;
	vector<vector<int>> pic;
	pic.resize(y);
	bool contains_blue = false;

	REP(j,y)
	{
		pic[j].resize(x);
		REP(i,x)
		{
			char c;
			cin >> c;
			if (c == '.')
				pic[j][i] = 0;
			else if (c == '#')
			{
				pic[j][i] = 1;
				contains_blue = true;
			}
		}
	}

	cout << "Case #" << case_num + 1 << ":" << endl;

	if (contains_blue)
	{
		REP(j,y - 1)
			REP(i,x - 1)
			{
				if (pic[j][i] == 1 && pic[j][i+1] == 1 && pic[j+1][i] == 1 && pic[j+1][i+1] == 1)
				{
					pic[j][i] = 2; pic[j][i+1] = 3; pic[j+1][i] = 4; pic[j+1][i+1] = 5;
				}
			}

		if (still_contains_blue(pic))
		{
			cout << "Impossible" << endl;
			return;
		}
	}

	REP(j,y)
	{
		REP(i,x)
		{
			int x = pic[j][i];
			switch (x) {
			case 0:cout << ".";break;
			case 1:cout << "X";break;
			case 2:cout << "/";break;
			case 3:cout << "\\";break;
			case 4:cout << "\\";break;
			case 5:cout << "/";break;
			default:cout << "Z";break;
			}
		}
		cout << endl;
	}
}

int main(int argc, char* argv[])
{
	int t; cin >> t;
	REP(i,t) test_case(i);
}

