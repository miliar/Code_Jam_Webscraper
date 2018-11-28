#define _CRT_SECURE_NO_DEPRECATE
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
		string S;
		cin >> S;
		int Len = (int)S.length();
		int I = Len - 2;
		while (I >= 0 && S[I] >= S[I + 1]) I--;
		if (I >= 0)
		{
			int J = I + 1;
			while (J + 1 < Len && S[J + 1] > S[I]) J++;
			swap(S[I], S[J]);
			sort(S.begin() + I + 1, S.end());
		}
		else
		{
			int I = Len - 1;
			while (S[I] == '0') I--;
			string T;
			T.reserve(Len + 1);
			T += S[I];
			for (int J = 0; J < Len - I; J++) T += '0';
			while (--I >= 0) T += S[I];
			S = T;
		}
		printf("Case #%d: %s\n", TT, S.c_str());
	}
	return 0;
}