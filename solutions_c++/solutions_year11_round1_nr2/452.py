/*
ID: ahaigh1
PROG: A
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <memory>
#include <set>
#include <stack>
#include <string>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <limits>
#include <map>
#include <bitset>
#include <ctime>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; i++)
#define CL(x) memset(x, 0, sizeof(x))
#define eps (1e-10)
#define inf (1<<30)
#define ll long long
#define MP make_pair

int t, n, m;
char dict[105][12], list[26];
bool seen[26];

bool match(char* target, char* word, int next) { 
	//true if they match on all characters up to next and word contains next
	
	//cout << "&" << target << " " << word << " " << list[next] << endl;
	
	if (strlen(target) != strlen(word)) return false;
	bool flag = false;
	int i = 0; while (target[i]) { 
		if (target[i] != word[i] && (seen[ target[i]-'a' ] || seen[ word[i]-'a' ]) ) return false;
		if (word[i] == list[next]) flag = true;
		i++;
	}
	
	//cout << "yes" << endl;
	
	return flag;
}

int score(char* target, char* list) { 
	//cout << "@@@" << target << endl;

	CL(seen);
	int score = 0;
	REP(i, 26) { 
		bool flag = false;
		REP(j, n) { 
			if (match(target, dict[j], i)) flag = true;
		}
		if (flag) { 
			//he will guess this letter
			
			//cout << list[i] << endl;
		
			bool flag = true;
			int j = 0; while (target[j]) { if (target[j] == list[i]) flag = false; j++; }
			
			//if (flag && !strcmp(target, "afy")) cout << target << " " << list[i] << endl;
			if (flag) score++;
			
		}
		seen[ list[i]-'a' ] = true;
		
		flag = false;
		int j = 0; while (target[j]) { if (!seen[ target[j]-'a' ]) flag = true; j++; }
		//cout << i << endl;
		if (!flag) return score;
	}
	return score;
}

int main() { 
	cin >> t;
	REP(i, t) { 
		cin >> n >> m;
		REP(j, n) cin >> dict[j];
		
		cout << "Case #" << (i+1) << ":";
		REP(j, m) { 
			cin >> list;
			
			int best = -1; char* out;
			REP(k, n) {
				int r = score(dict[k], list);
				//cout << dict[k] << " " << r << endl;
				
				if (r > best) { 
					best = r;
					out = dict[k];
				}
			}
			cout << " " << out;
			
		}
		cout << endl;
	}
}