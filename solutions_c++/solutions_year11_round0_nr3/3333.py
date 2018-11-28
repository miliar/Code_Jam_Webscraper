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


bool add_one(vector<bool> &v){
	bool last_number = true;
	FORR(i, v.size(), 0){
		if (v[i] == true){
			v[i] = false;
		} else {
			v[i] = true;
			last_number = false;
			break;
		}
	}
	return not last_number;
}


int main(){
	/*	
	vector<bool> tst(4, false);
	do{
		FORN(i, 0, tst.size()){
			cout << (int)tst[i];
		}
		cout << endl;
	} while(add_one(tst));
	*/

	//Descomente para acelerar cin
	ios::sync_with_stdio(false);
	
	int T;
	cin >> T;
	FORN(i, 0, T){
		int sum_big = 0;
		int sum_small = 0;

		/*
		map<int, int> buckets;
		int N;
		cin >> N;
		FORN(j, 0, N){
			int k;
			cin >> k;
			buckets[k]++;
		}
		map<int, int>::iterator it = buckets.begin(), next;
		while(it != buckets.end()){
			next = it;
			next++;

			if (it->second % 2 == 0){
				sum_big += it->second*it->first;
				buckets.erase(it);
			} else {
				sum_big += (it->second - 1) * it->first;
				it->second = 1;
			}

			it = next;
		}
		vector<int> values;
		FOREACH(p, buckets){
			values.push_back(p->first);
		}
		*/

		vector<int> values;
		int N; cin >> N;
		FORN(i, 0, N){
			int tmp; cin >> tmp;
			values.push_back(tmp);
		}
			
		vector<bool> members(values.size(), false);
		WATCH(members.size());

		int best_big = -1, best_small = -1;
		do{
			int partial_big = 0, partial_small = 0;
			int xor_big = 0, xor_small = 0;
			FORN(j, 0u, members.size()){
				if (members[j]){
					partial_big += values[j];
					xor_big = xor_big ^ values[j];
				} else {
					partial_small += values[j];
					xor_small = xor_small ^ values[j];
				}
			}

			if (xor_small == xor_big and partial_small > 0){
				if (partial_big > best_big){
					best_big = partial_big;
					best_small = partial_small;
				}
			}
			
		} while(add_one(members));

		cout << "Case #" << (i+1) << ": ";
		if (best_big == -1){
			cout << "NO" << endl;
		} else {
			cout << (best_big + sum_big) << endl;
		}	

	}


}
