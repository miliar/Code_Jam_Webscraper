#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <list>
#include <numeric>
#include <bitset>
#include <ext/algorithm>
#include <ext/numeric>
#include <fstream>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
typedef long long LL; using namespace std;

int main(){
	ifstream fin("Bl.in");
	ofstream fout("Bl.out");
	int tests;
	fin >> tests;
	int n, m, kk, a, b;
	FOR (test, tests){
		fin >> n;
		fin >> m;
		vector <pair<int, int> > c[m];
		FOR (i, m)
			c[i].clear();
		int uses[n];
		SET(uses, 255);
		FOR (i, m){
			fin >> kk;
			FOR (j, kk){
				fin >> a >> b;
				a--;
				c[i].pb(make_pair(a, b));
			}
		}
		bool poss = true;
		bool sat[m];
		SET(sat, 0);
		
		bool ch = true;
		while (ch){
			ch = false;
			FOR (i, m){
				if (sat[i])
					continue;
				if (c[i].sz == 1){
					if (uses[c[i][0].first] != -1 && uses[c[i][0].first] != c[i][0].second){
						poss = false;
						break;
					}
					else{
						uses[c[i][0].first] = c[i][0].second;
						sat[i] = true;
						// rearange each user
						FOR (j, m){
							if (sat[j])
								continue;
							vector<pair<int, int> > tmp;
							tmp.clear();
							FOR (k, c[j].sz){
								if (c[j][k].first == c[i][0].first && c[i][0].second == c[j][k].second){
									sat[j] = true;
									break;
								}
								if (c[j][k].first != c[i][0].first)
									tmp.pb(make_pair(c[j][k].first, c[j][k].second));
							}
							c[j] = tmp;
						}
						ch = true;
					}
				}
			}
		}
		FOR (i, m)
			if (!sat[i] && c[i].sz == 0)
				poss = false;
		if (poss){
			fout << "Case #" << (test + 1) << ":";
			FOR (i, n)
				if (uses[i] == -1)
					uses[i] = 0;
			FOR (i, n)
				fout << " " << uses[i];
			fout << endl;
		}
		else
			fout << "Case #" << (test + 1) << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
