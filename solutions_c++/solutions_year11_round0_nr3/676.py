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
int N;
int P[1000];

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		int Mark = 0;
		int Sum = 0;
		cin >> N;
		for (int I = 0; I < N; I++) cin >> P[I];
		for (int I = 0; I < N; I++) Mark ^= P[I];
		for (int I = 0; I < N; I++) Sum += P[I];
		sort(P, P + N);
		printf("Case #%d: ", TT);
		if (Mark != 0) printf("NO");
		else printf("%d", Sum -= P[0]);
		printf("\n");
	}
	return 0;
}
