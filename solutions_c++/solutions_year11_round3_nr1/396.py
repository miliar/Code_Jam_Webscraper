/*
 * A.SquareTiles.cpp
 *
 *  Created on: May 22, 2011
 *      Author: ahmed
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <cstring>
typedef long long ll;
using namespace std;

#define pb push_back
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<pii> > adjL;
int oo = (int) 1e9;

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("b.txt", "wt", stdout);

	int t;scanf("%d", &t);
	for (int ii = 0; ii < t; ++ii) {
		int r, c;
		scanf("%d%d", &r, &c);
		vector<string >vs;
		string str;
		for (int i = 0; i < r; ++i) {
			cin>>str;
			vs.pb(str);
		}

		int f = 1;
		while(f) {
			f = 0;
			for (int i = 0; i < r; ++i) {
				for (int j = 0; j < c; ++j) {
					if( i < r -1 && j < c - 1 && vs[i][j] == '#' &&
							vs[i][j+1] == '#' && vs[i+1][j] == '#' &&
							vs[i+1][j+1] == '#')
						vs[i][j] = vs[i+1][j+1] = '/', vs[i+1][j] = vs[i][j+1] = '\\', f = 1;
				}
			}
		}
		f = 0;
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				if(vs[i][j] == '#')
					f = 1;
			}
		}
		printf("Case #%d:\n", ii+1);
		if(f)
			printf("Impossible\n");
		else
		{
			for (int i = 0; i < r; ++i) {
				cout<<vs[i]<<endl;
			}
		}
	}
	return 0;
}

/*
3
2 3
###
###
1 1
.
4 5
.##..
.####
.####
.##..
 */
