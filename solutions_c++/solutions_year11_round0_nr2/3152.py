#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define NDEBUG

#if defined(NDEBUG)
#define DBG_CODE(cb...)
#else
#define DBG_CODE(cb...) cb
#endif

#define WRITE(x) DBG_CODE(cout << x << endl)
#define WATCH(x) DBG_CODE(cout << #x << "=" << x << endl)

//[a, b) incrementando
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
//(a, b] decrementando
#define FORR(i, a, b) for(typeof(a) i = (a) - 1; i >= (b) && i < (a) ; i--)

#define ALL(x) x.begin(), x.end()
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define FOREACHR(i, c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)

vector<char> solve(
	list<char> &invokes, 
	map<pair<char,char>, char> &combinations, 
	map<char, vector<char> > &oppositions)
{
	vector<char> element_list;
	map<char, int> element_counts;

	FOREACH(element, invokes){
		WATCH(*element);
		element_list.push_back(*element);
		element_counts[*element]++;
	
		if (element_list.size() >= 2){
			char last = element_list[element_list.size()-1];
			char before_last = element_list[element_list.size()-2];
				
			map<pair<char, char>, char >::iterator it = combinations.find(make_pair(last, before_last));

			if ( it != combinations.end()){
				element_counts[last]--;
				element_list.pop_back();
				element_counts[before_last]--;
				element_list.pop_back();
				element_counts[it->second]++;
				element_list.push_back(it->second);
			}
		}

		if (element_list.size() >= 1){
			char last = element_list.back();
			element_counts[last]--;
			bool list_cleared = false;
			FOREACH(opposite, oppositions[last]){
				if (element_counts[*opposite] > 0){
					element_list.clear();
					element_counts.clear();
					list_cleared = true;
					break;
				}
			}
			if (!list_cleared) element_counts[last]++;

		}
	}

	return element_list;
}

int main(){
	//Descomente para acelerar cin
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	FORN(i, 0, T){
		list<char> invokes;
		map<pair<char,char>, char> combinations;
		map<char, vector<char> > oppositions;

		int C;
		cin >> C;
		string s;
		FORN(j, 0, C){
			cin >> s;
			combinations[make_pair(s[0], s[1])] = s[2];
			combinations[make_pair(s[1], s[0])] = s[2];
		}

		int D;
		cin >> D;
		FORN(j, 0, D){
			cin >> s;
			oppositions[s[0]].push_back(s[1]);
			oppositions[s[1]].push_back(s[0]);
		}

		int N;
		cin >> N;
		cin >> s;	
		FORN(j, 0, N){
			invokes.push_back(s[j]);
		}
			
		vector<char> solution = solve(invokes, combinations, oppositions);
		cout << "Case #" << (i+1) << ": [";
		FORN(j, 0, solution.size()){
			cout << solution[j] << (j == solution.size() - 1 ? "" : ", ");
		}
		cout << "]" << endl;

	}
	
}
