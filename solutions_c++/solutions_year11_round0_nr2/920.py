#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
#define FOR(i, n) for(int i = 0; i < (int)(n); ++i)


typedef pair<char, char> PCC;
void Go(){

	map<PCC, char> combine;
	set<PCC> opposed;
	set<char> base;
	const string _base = "QWERASDF";
	base.insert(_base.begin(), _base.end());

	int n;
	string t;
	scanf("%d", &n);
	FOR(i, n){
		cin >> t;
		combine[PCC(t[0], t[1])] = t[2];
		combine[PCC(t[1], t[0])] = t[2];
	}
	scanf("%d", &n);
	FOR(i, n){
		cin >> t;
		opposed.insert(PCC(t[0], t[1]));
		opposed.insert(PCC(t[1], t[0]));
	}
	scanf("%d", &n);
	cin >> t;
	map<char, int> used;
	vector<char> list;
	FOR(i, n){
		list.push_back(t[i]);		
		used[list.back()]++;

		bool combined = false;
		if (list.size() >= 2){
			PCC last = PCC(list[list.size() - 2], list[list.size() - 1]);
			if (combine[last] != 0){
				used[list[list.size() - 1]]--;
				list.pop_back();
				used[list[list.size() - 1]]--;
				list.pop_back();

				list.push_back(combine[last]);
				used[list.back()]++;
				combined = true;
			}
		}
		if (!combined){
			for (map<char, int>::iterator it = used.begin(); it != used.end(); ++it){
				if (it->second > 0 && opposed.count(PCC(list.back(), it->first))){
					list.clear();
					used.clear();
					break;
				}
			}
		}
	}
	printf("[");
	FOR(i, list.size()){
		if (i)
			printf(", ");
		printf("%c", list[i]);
	}
	printf("]");
}

int main(){
	const string task = "B";
	const int attempt = -1;
	const bool dbg = false;


	if (dbg){
		freopen("inp.txt", "r", stdin);
	}
	else{
		stringstream ss;
		ss << "gcj/2011/qual/";
		if (attempt < 0)
			ss << task << "-large";
		else
			ss << task << "-small-attempt" << attempt;
		freopen((ss.str() + ".in").c_str(), "r", stdin);
		freopen((ss.str() + ".out").c_str(), "w", stdout);
	}


	int t;
	scanf("%d", &t);
	FOR(i, t){
		printf("Case #%d: ", i + 1);
		Go();
		printf("\n");
	}
	return 0;
}