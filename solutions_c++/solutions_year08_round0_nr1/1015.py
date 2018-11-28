#include <iostream>
#include <string>
#include <set>
#include <list>
#include <algorithm>
#include <vector>
#include <map>
#include <limits.h>

using namespace std;

#define debug if(0) cout

string find_best_fit(list<string>::iterator i, list<string> &querylist,  multimap<int, string> &clashcount)
{
	int maxhops = 0;
	string result;
	for(multimap<int, string>::iterator engine_iter = clashcount.begin();engine_iter != clashcount.end();
		++engine_iter) {
		int hops = 0;
		for(list<string>::iterator j = i;j != querylist.end();j++) {
			if(*j == engine_iter->second)
				break;
			hops++;
		}
		if(hops>maxhops) {
			maxhops = hops;
			result = engine_iter->second;
		}
	}
	return result;
}

int main()
{
	int cases;

//	cases << cin;
	cin >> cases;
	debug << "Number of cases " << cases << endl;

	for(int j = 0;j < cases;j++) {
		set<string> engines;
		multiset<string> queries;
		list<string> querylist;
		
		debug << "Case " << j << endl;
		int cnt;
		cin >> cnt;

		string dumb;
		getline(cin, dumb);

		while(cnt--) {
			string engine;
			getline(cin, engine);
			engines.insert(engine);
		}
		cin >> cnt;
		getline(cin, dumb);
		while(cnt--) {
			string query;
			getline(cin, query);
			queries.insert(query);
			querylist.push_back(query);
		}
		debug << "Engines: ";
		for(set<string>::iterator i = engines.begin();i != engines.end();++i) {
			debug << "\""<<*i << "\" ";
		}
		debug << endl;
		debug << "Queries: ";
		for(list<string>::iterator i = querylist.begin();i != querylist.end() ;++i) {
			debug << "\"" << *i << "\" ";
		}
		debug << endl;

		vector<string> clashing;
		vector<string> notclashing;
		set_intersection(engines.begin(), engines.end(), queries.begin(), queries.end(),

						 inserter(clashing, clashing.begin()));
		set_difference(engines.begin(), engines.end(), queries.begin(), queries.end(),
						 inserter(notclashing, notclashing.begin()));
		multimap<int, string> clashcount;

		if(notclashing.size())
			clashcount.insert(make_pair(0, *notclashing.begin()));

		for(vector<string>::iterator i = clashing.begin();i != clashing.end();++i) {
			debug << "\""<<*i << "\"";
			clashcount.insert(make_pair(queries.count(*i), *i));
			debug << "(" << queries.count(*i) << ") ";
		}
		
		debug << endl;
		for(multimap<int, string>::iterator i = clashcount.begin();i != clashcount.end();++i) {
			debug << "Candidate is " << i->second << "(" << i->first << ")" << endl;

		}
		
		int minswitches = 0;
		
		string engine = find_best_fit(querylist.begin(), querylist, clashcount);
		debug << "First best fit " << engine << endl;
		for(list<string>::iterator i = querylist.begin();i != querylist.end();++i) {
			if(engine == *i) {
				minswitches++;
				engine = find_best_fit(i, querylist, clashcount);
				debug << "Switch to " << engine <<endl;
			}			
		}


		cout << "Case #" << j+1 << ": " << minswitches << endl;

		debug << endl;			




	}

}
