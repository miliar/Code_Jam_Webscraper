#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#pragma comment(linker, "/STACK:200000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <complex>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <map>
#include <memory.h>
#include <numeric>
#include <iomanip>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <string>
#include <iomanip>
#include <sstream>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

#define pb push_back
#define mp make_pair
#define mset(mas,val) memset(mas,val,sizeof(mas))
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define fornd(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<int(b); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
	
const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;

int main(){
#ifdef gridnevvvit
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
#endif
	int testcaces;
	int testcount = 1;
	cin >> testcaces;
	while (testcaces--) {
		vector < vector < char > > field(4, vector < char > (4, 0));
		forn(i,4) {
			forn(j, 4) {
				cin >> field[i][j];
			}
		}
		string ans1 = "X won";
		string ans2 = "O won";
		string ans3 = "Draw";
		string ans4 = "Game has not completed";
		bool isans1 = false;
		bool isans2 = false;
		bool hasspace = false;
		forn(i, 4) {
			set < char > tused;
			forn(j, 4) {
				tused.insert(field[i][j]);
			}
			if (tused.size() == 1 && tused.count('X'))
				isans1 = true;
			if (tused.size() == 1 && tused.count('O'))
				isans2 = true;
			if (tused.size() == 2 && tused.count('X') && tused.count('T'))
				isans1 = true;
			if (tused.size() == 2 && tused.count('O') && tused.count('T'))
				isans2 = true;
			if (tused.count('.'))
				hasspace = true;
		}
		forn(i, 4) {
			set < char > tused;
			forn(j, 4) {
				tused.insert(field[j][i]);
			}
			if (tused.size() == 1 && tused.count('X'))
				isans1 = true;
			if (tused.size() == 1 && tused.count('O'))
				isans2 = true;
			if (tused.size() == 2 && tused.count('X') && tused.count('T'))
				isans1 = true;
			if (tused.size() == 2 && tused.count('O') && tused.count('T'))
				isans2 = true;
			if (tused.count('.'))
				hasspace = true;
		}
		set < char > tused;
		forn(j, 4) {
			tused.insert(field[j][j]);
		}
		if (tused.size() == 1 && tused.count('X'))
			isans1 = true;
		if (tused.size() == 1 && tused.count('O'))
			isans2 = true;
		if (tused.size() == 2 && tused.count('X') && tused.count('T'))
			isans1 = true;
		if (tused.size() == 2 && tused.count('O') && tused.count('T'))
			isans2 = true;
		if (tused.count('.'))
			hasspace = true;	
		tused.clear();
		forn(j, 4) {
			tused.insert(field[j][4-j-1]);
		}
		if (tused.size() == 1 && tused.count('X'))
			isans1 = true;
		if (tused.size() == 1 && tused.count('O'))
			isans2 = true;
		if (tused.size() == 2 && tused.count('X') && tused.count('T'))
			isans1 = true;
		if (tused.size() == 2 && tused.count('O') && tused.count('T'))
			isans2 = true;
		if (tused.count('.'))
			hasspace = true;	
		printf("Case #%d: ", testcount++);
		if (isans1) {
			puts(ans1.c_str());
			continue;
		}
		if (isans2) {
			puts(ans2.c_str());
			continue;
		}
		if (hasspace) {
			puts(ans4.c_str());
		} else {
			puts(ans3.c_str());
		}
	}
}