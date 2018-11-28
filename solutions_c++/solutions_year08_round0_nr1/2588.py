#include <vector>
#include <string>
#include <list>
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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(int argc, char *argv[])
{
	int N = 0;
	cin >> N;
	for (int _i = 0; _i < N ; ++_i) 
// for each test case
	{
		set<string> orig_engine, engine;
		int S = 0, Q = 0;
		cin >> S;
//		cout << "S = " << S << endl;
		string str;
		getline(cin,str);
		for (int _j = 0; _j < S ; ++_j )
		{
//			cin >> str;
			getline (cin,str);
			orig_engine.insert(str);
			str.clear();
		}
//		cout << "There are " << orig_engine.size() << " engines" << endl;
//		for ( set<string>::iterator it=orig_engine.begin() ; it != orig_engine.end(); it++ )
//			cout << *it << endl;
		cin >> Q;
//		cout << "Q = " << Q << endl;
		vector<string> query;
		getline(cin,str);
		for (int _j = 0; _j < Q; ++_j )
		{
//			cin >> str;
			getline (cin,str);
			query.push_back(str);
		}
//		for ( int _p = 0; _p < Q; ++_p)
//			cout << query[_p] << endl;

		
		
		int ret = 0;
		engine = orig_engine;
		for (int i = 0; i < Q ; ++i )
		{
			set<string>::iterator found = engine.find(query[i]);
//			cout << *found << endl;
//			cout << query[i] << endl;
			if (found != engine.end())
			{
//				cout << *found << endl;
				engine.erase(*found);
			}
			if (engine.size() == 0)
			{
				ret++;
				engine = orig_engine;
				engine.erase(query[i]);
			}

		}
		cout << "Case #" << _i+1 << ": " << ret << endl;
	}
	return 0;
}
