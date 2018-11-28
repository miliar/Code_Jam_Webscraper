#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable: 4018)
#ifdef NDEBUG
	#define _SECURE_SCL 0
#endif
#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

int NN, TT;

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		long long N, K;
		cin >> N >> K;
		bool Result = (K + 1) % ((long long)1 << N) == 0;
		printf("Case #%d: ", TT);
		if (Result) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}