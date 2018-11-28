#include <functional>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <cstdlib>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <map>
#include <set>

using namespace std;

typedef istringstream ISS;
typedef ostringstream OSS;
#define VT vector
typedef VT<int> VI;
typedef VT<vector<int>> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef VT<VD> VVD;
typedef pair<int,int> PII;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,a,b) for(int i=(int)a;i<=(int)b;++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair





int main()
{

#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

#endif

	int T;
	cin >> T;

	REP(t, T)
	{
		int C;
		cin >> C;

		map<pair<char,char>,char> combines;

		REP(c, C)
		{
			string str;
			cin >> str;
			combines[MP(str[0], str[1])] = str[2];
			combines[MP(str[1], str[0])] = str[2];
		}

		int D;
		cin >> D;

		map<pair<char,char>,char> opposites;

		REP(d, D)
		{
			string str;
			cin >> str;

			opposites[MP(str[0], str[1])];
			opposites[MP(str[1], str[0])];
		}

		int N;
		cin >> N;

		string str;
		cin >> str;

		string buffer;

		REP(i, str.size())
		{
			if (buffer.size()==0)
				buffer.push_back(str[i]);
			else
			{
				char last = buffer[buffer.size()-1];
				if (combines.count(MP(last, str[i])))
				{
					buffer[buffer.size()-1] = combines[MP(last, str[i])];
				}
				else
				{
					bool cleared = 0;
					REP(j, buffer.size())
					{
						if (opposites.count(MP(str[i],buffer[j])))
						{
							buffer.clear();
							cleared = 1;
							break;
						}

					}

					if (cleared)
						continue;

					buffer.push_back(str[i]);

				}
			}

		}


		string res;
		res += "[";
		REP(i, buffer.size())
		{
			if (i)
				res += ", ";

			res += buffer[i];
		}

		res += "]";


		cout << "Case #" << (t+1) << ": " << res << "\n";
	}
}



