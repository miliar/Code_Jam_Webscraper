/*
 * C.cpp
 *
 *  Created on: 2010-5-22
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
#include <cassert>

using namespace std; 

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define SZ(c) ((int) (c).size())

const int INF = 1000000000;

bool winning(int A, int B)
{
	if (A < B)
		return winning(B, A);
	else {
		if (B == 0)
			return true;
		else {
			int cnt = A / B;
			if (cnt == 1)
				return !winning(B, A - B);
			else
				return true;
		}
	}
}

ll howMany(int A1, int A2, int B1, int B2)
{
//	ll res = 0;
//	for (int A = A1; A <= A2; ++A)
//		for (int B = B1; B <= B2; ++B)
//			if (winning(A, B))
//				++res;
//	return res;
	if (A2 - A1 > B2 - B1) {
		swap(A1, B1);
		swap(A2, B2);
	}
	ll res = 0;
	for (int i = A1; i <= A2; ++i) {
		int left1 = 0;
		int right1 = i;
		while (right1 - left1 > 1) {
			int middle = (left1 + right1) / 2;
			if (winning(i, middle))
				left1 = middle;
			else
				right1 = middle;
		}
		int left2 = i;
		int right2 = B2 + 1;
		while (right2 - left2 > 1) {
			int middle = (left2 + right2) / 2;
			if (winning(i, middle))
				right2 = middle;
			else
				left2 = middle;
		}
		res += max(min(right1, B2 + 1) - B1, 0) + max(B2 + 1 - max(B1, right2), 0);
	}
	return res;
}

int main() 
{
	int T;
	cin >> T;
	for (int icase = 1; icase <= T; ++icase) {
		int A1;
		int A2;
		int B1;
		int B2;
		cin >> A1 >> A2 >> B1 >> B2;
		printf("Case #%d: %lld\n", icase, howMany(A1, A2, B1, B2));
	}
	return 0;
}
