#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define mp make_pair
#define all(x) (x).begin(),(x).end()


ifstream in("input_b.txt");


map< pair<pair<int, bool>,int>, bool> res_map;

void calc()
{
	// for 2-apart mode
	REP(i, 11)
	REP(j, 11)
	REP(k, 11)
	{
		if(abs(i - j) > 2)
			continue;
		if(abs(j - k) > 2)
			continue;
		if(abs(i - k) > 2)
			continue;

		if( !(abs(i - j) == 2 || abs(j - k) == 2 || abs(i - k) > 2) )
			continue;

		REP(p, 11)
		{
			bool res = (i >= p) || (j >= p) || (k >= p);
			res_map[ make_pair( make_pair(i+j+k, true), p ) ] |= res;
		}
	}

	// for 0,1-apart mode
	REP(i, 11)
	REP(j, 11)
	REP(k, 11)
	{
		if(abs(i - j) > 1)
			continue;
		if(abs(j - k) > 1)
			continue;
		if(abs(i - k) > 1)
			continue;

		REP(p, 11)
		{
			bool res = (i >= p) || (j >= p) || (k >= p);
			res_map[ make_pair( make_pair(i+j+k, false), p ) ] |= res;
		}
	}
}


int main(int argc, char **argv)
{
	calc();

	ofstream out("out_b.txt");
	int T;
	in >> T;
	for(int t = 1; t <= T; t++)
	{
		int N, S, P;
		vector<int> t_list;

		in >> N >> S >> P;
		int win_abs = 0, win_cond = 0, win_both = 0;
		REP(i, N)
		{
			int t_val;
			in >> t_val;

			if( res_map[ make_pair(make_pair(t_val, false), P) ])
				win_abs++;
			else if( res_map[ make_pair(make_pair(t_val, true), P) ] )
				win_cond++;
			
			if( res_map[ make_pair(make_pair(t_val, false), P) ] && res_map[ make_pair(make_pair(t_val, true), P) ] )
				win_both++;
		}

		int answer = win_abs + min(S, win_cond);
		if(S > win_cond)
		{
			cout << "S: " << S << endl;
			cout << "win_abs: " << win_abs << endl;
			cout << "win_cond: " << win_cond << endl;
			cout << "win_both: " << win_both << endl;
		}
		cout << "Case #" << t << ": " << answer << endl;
		out << "Case #" << t << ": " << answer << endl;
	}
	return 0;
}
