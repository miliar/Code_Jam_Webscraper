/*
 * A.cpp
 *
 *  Created on: 2010-6-4
 *      Author: Allie
 */

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <iterator>
#include <numeric>
#include <utility>
#include <complex>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cfloat>
#include <ctime>
#include <cassert>

using namespace std; 

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define SZ(c) ((int) (c).size())

const int INF = 1000000000;

int P;
int M[1024];
int price[10][512];

int minimumCost()
{
	int res = 0;
	for (int i = 0; i < P; ++i) {
		int teams = 1 << (P - i);
		for (int j = 0; j < teams; j += 2) 
			if (min(M[j], M[j + 1]) == 0) {
				++res;
				M[j / 2] = 0;
			} else {
				M[j / 2] = min(M[j], M[j + 1]) - 1;
			}
	}
	return res;
}

int main() 
{
	int T;
	cin >> T;
	for (int icase = 1; icase <= T; ++icase) {
		scanf("%d", &P);
		for (int i = 0; i < (1 << P); ++i)
			scanf("%d", &M[i]);
		for (int i = P - 1; i >= 0; --i) 
			for (int j = 0; j < 1 << i; ++j)
				scanf("%d", &price[i][j]);
		printf("Case #%d: %d\n", icase, minimumCost());
	}
	return 0;
}
