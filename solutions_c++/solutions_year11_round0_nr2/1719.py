#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

//#define debug

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long long lint;

const int inf = 0x7fffffff;
const int white = 0, gray = 1, black = 2;

const int Size = 20000;

char buffer[Size];

int solution(int nTest) {
	int n;
	scanf("%d", &n);
	map<pii, char> base;
	For(i, 0, n) {
		getchar();
		char f1 = getchar();
		char f2 = getchar();
		char t = getchar();
		base[mp(f1,f2)] = t;
		base[mp(f2, f1)] = t;
	}
	scanf("%d", &n);
	
	set<pii> op;
	For(i, 0, n) {
		getchar();
		char f1 = getchar();
		char f2 = getchar();
		op.insert(mp(f1, f2));
		op.insert(mp(f2, f1));
	}

	scanf("%d", &n);
	vector<char> res;
	getchar();
	gets(buffer);
	string s = buffer;
	For(i, 0, sz(s)) {
		char t = s[i];
		res.pb(t);
		while(sz(res) > 1) {
			pii p = mp(res[sz(res) -1], res[sz(res) - 2]);
			if(base.count(p)) {
				res.pop_back();
				res.pop_back();
				res.pb(base[p]);
			}
			else {
				break;
			}
		}
		For(i, 0, sz(res)) {
			For(j, i + 1, sz(res)) {
				if(op.count(mp(res[i], res[j]))) {
					res.clear();
					break;
				}
			}
		}
	}
	
	printf("Case #%d: ", nTest + 1);
	printf("[");
	if(sz(res))
		printf("%c", res.front());
	For(i, 1, sz(res)) {
		printf(", %c", res[i]);
	}
	printf("]\n");




	return 1;
}

int main() {
	freopen("input.txt", "r", stdin);
#ifndef debug
	freopen("output.txt", "w", stdout);
#endif

	int i = 0, n = 999999;
	scanf("%d", &n);

	while(i < n && solution(i))
		i++;

	return 0;
}

