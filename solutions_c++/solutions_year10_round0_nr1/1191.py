/*
 * a.cpp
 *
 *  Created on: 2010-5-8
 *      Author: Allie
 */
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <complex>
#include <cassert>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define SZ(c) ((int) (c).size())

const int INF = 1000000000;

bool lightOn(int N, int K)
{
	return K % (1 << N) == (1 << N) - 1;
}

int main()
{
	int T;
	cin >> T;
	for (int icase = 1; icase <= T; ++icase) {
		int N;
		int K;
		cin >> N >> K;
		printf("Case #%d: ", icase);
		if (lightOn(N, K))
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}

