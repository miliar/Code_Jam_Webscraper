#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)	for(int i=(a); i<(b); ++i)
#define REP(iter,v) for(typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define MP make_pair
#define PB push_back
#define SZ size()
#define iss istringstream 

#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

typedef long long ll, int64;
typedef vector<int> VI;

int64 INF = 1000*1000*1001;

string s[4];
char won;
int main(void)	{
	int T;
	
	cin >> T;
	FOR (nc, 1, T+1) {
		FOR (i, 0, 4)	cin >> s[i];
		won = 0;
		FOR (i, 0, 4)	{	//check row i
			char ch = 0;
			FOR (j, 0, 4)	if (s[i][j] != '.' && s[i][j] != 'T')	{
				ch = s[i][j];
				break;
			}
			if (ch == 0)	continue;
			int j = 0;
			while (j < 4 && (s[i][j] == ch || s[i][j] == 'T'))	j++;
			if (j == 4)	won = ch;
		}
		FOR (j, 0, 4)	{	//check col j
			char ch = 0;
			FOR (i, 0, 4)	if (s[i][j] != '.' && s[i][j] != 'T')	{
				ch = s[i][j];
				break;
			}
			if (ch == 0)	continue;
			int i = 0;
			while (i < 4 && (s[i][j] == ch || s[i][j] == 'T'))	i++;
			if (i == 4)	won = ch;
		}
		
		//diagonals
		int i = 0;
		while (i < 4 && (s[i][i] == 'X' || s[i][i] == 'T')) i++;
		if (i == 4)	won = s[0][0];
		i = 0;
		while (i < 4 && (s[i][i] == 'O' || s[i][i] == 'T')) i++;
		if (i == 4)	won = s[0][0];
		
		i = 0;
		while (i < 4 && (s[i][3-i] == 'X' || s[i][3-i] == 'T')) i++;
		if (i == 4)	won = s[0][3];
		i = 0;
		while (i < 4 && (s[i][3-i] == 'O' || s[i][3-i] == 'T')) i++;
		if (i == 4)	won = s[0][3];
		
		bool draw = true;
		//empty spot
		FOR (i, 0, 4)	FOR (j, 0, 4)	if (s[i][j] == '.')	draw = false;

		cout << "Case #" << nc << ": ";
		if (won != 0)	cout << won << " won";
		else if (draw)	cout << "Draw";
		else cout << "Game has not completed";
		cout << endl;
	}
}
