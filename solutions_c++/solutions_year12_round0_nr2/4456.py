/*
 * DancingWithGooglers.cpp
 *
 *  Created on: Apr 14, 2012
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
/*#include <hash_map>
using namespace __gnu_cxx;*/
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
	freopen("B-large.in", "rt", stdin);
	freopen("b.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for (int ii = 0; ii < t; ++ii) {
		int n, s, p, cur, res = 0;
		scanf("%d%d%d", &n, &s, &p);

		for (int i = 0; i < n; ++i) {

			scanf("%d", &cur);
			int d = cur/3;
			int dif = cur - d*3;
//			cout<<cur<<" "<<d<<" "<<dif<<endl;
			if(d>=p)
				res++;
			else if(dif >=1 && d+1>=p)
				res++;
			else if(dif>=2 && d+2>=p && s>0)
				res++, s--;
			else if(dif == 0 && s > 0 && d+1>=p && cur>=3)
				res++, s--;
		}
		printf("Case #%d: %d\n", ii+1, res);
	}
	return 0;
}
/*
4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21
 */
