#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <string>
#include <algorithm>
#include <functional>
#include <utility>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define _bpc __builtin_popcount
#define pb push_back
#define MP make_pair
#define For(a,b,c) for(typeof(b)a=(b); a<(c); ++a)
#define ALL(a) a.begin(),a.end()
#define DBG(a) cout << #a << ": " << a << endl
#define FORE(i, v) for(typeof(v.begin()) i = v.begin(); i != v.end(); ++i)

struct HM
{
	void take(string s)
	{
		h = atoi(s.substr(0, 2).c_str());
		m = atoi(s.substr(3, 2).c_str());
	}
	
	HM add(int t)
	{
		HM ret;
		ret.m = m, ret.h = h;
		ret.m += t;
		ret.h += ret.m/60, ret.m %= 60;
		return ret;
	}
	
	bool operator<(const HM& t) const {
		return h < t.h || (h == t.h && m <= t.m);
	}
	
	bool operator<=(const HM& t) const {
		return h < t.h || (h == t.h && m <= t.m);
	}
	int h, m;
};
		vector<pair<pair<HM,HM>,int> > sched;
int main()
{
	ifstream fin("B.in");
	ofstream fout("B.out");
	
	int T;
	fin >> T;
	For (LOL, 1, T+1)
	{
		int wait; fin >> wait;
		int NA, NB; fin >> NA >> NB;
		
sched.clear();
		
		For (i, 0, NA+NB)
		{
			pair<HM,HM> s;
			string t;
			fin >> t; s.first.take(t);
			fin >> t; s.second.take(t);
			sched.pb(MP(s, i>=NA));
		}
	
		sort(ALL(sched));
		
		
		int resA=0, resB=0;
		bool done[2222] = {0};
		
		For (i, 0, sched.size()) {
			if (!done[i]) {if (sched[i].second == 0) resA++; else resB++;}
				For (j, i+1, sched.size())
				{
					if (!done[j] && sched[j].second != sched[i].second && sched[i].first.second.add(wait) <= sched[j].first.first)
					{
						done[j] = true;
						break;
					}
				}
		}
		
		fout << "Case #" << LOL << ": " << resA << " " << resB << endl;
	}
	
	return 0;
}