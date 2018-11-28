#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i < int(n); i++)
#define mp(a, b) make_pair(a, b);
#define X first
#define Y second
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;

typedef long long li;
typedef pair<int, int> pt;

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	string s;
	int t;
	cin >> t;
	forn(q, t){
		cout << "Case #" << q + 1 <<": ";  
		cin >> s;
		bool fl = false;
		for(int j = sz(s) - 1; j >= 1; j--){
			if (s[j] > s[j - 1])
				fl = true;
		}
		if (fl){
			fl = false;
			int an = -1;
			char ans = '9' + 1;
			int i;
			for(i = sz(s) - 2; i >= 0 && !fl; i--){
				bool g = true;
				for(int j = i + 1; j < sz(s) && !fl; j++){
					if (s[i] < s[j] && (an == -1 || ans > s[j])){
						ans = s[j];
						an = j;
						g = false;
						
					}
				}
				if (!g)
					break;
			}

				char c = s[i];
				s[i] = s[an];
				s[an] = c;
				for(int i1 = i + 1; i1 < sz(s); i1++)
					for(int j1 = i1 + 1; j1 < sz(s); j1++)
						if (s[i1] > s[j1]){
							char c = s[i1];
							s[i1] = s[j1];
							s[j1] = c;
						}
				cout << s << endl;
				fl = true;
			
		}
		else{
			int j = sz(s) - 1;
			while (j >= 0 && s[j] == '0')
				j--;
			cout << s[j] << '0';
			for(int i = sz(s) - 1; i >= 0; i--)
				if (i != j)
				cout << s[i];
			cout << endl;
		}
	}
	return 0;
}