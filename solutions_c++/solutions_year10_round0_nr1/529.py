//Made by diver_ru, made with love^^
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <iostream>
#include <memory.h>
#include <fstream>

/*/#ifndef ONLINE_JUDGE
FILE *fi = freopen("input.txt", "r", stdin), fo = *freopen("output.txt", "w", stdout);
#endif /**/
using namespace std;

typedef long long int64;

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		int N, K;
		cin >> N >> K;
		cout << "Case #" << i << ": ";
		cout << ((K+1) % (1 << N) == 0 ? "ON" : "OFF");
		cout << endl;
	}

	return 0;
}