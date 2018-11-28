#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <cstdio>
#include <set>
#include <algorithm>
#include <complex>
#include <iterator>
#include <set>
#include <bitset>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
typedef long long int LL;
typedef unsigned int uint;
const uint K = 100000000, N = 30;
bool check(uint n, uint k)
{
	if(k == 0)
		return false;
	if((k | (uint(1) << (n)) - 1) == k)
		return true;
	return false;

}
int main()
{
	int t, k, n;
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase)
	{
		cin >> n >> k;
		cout << "Case #" << testCase << ": " << (check(n, k) ? "ON" : "OFF") << endl;
	}
}
