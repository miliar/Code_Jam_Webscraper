#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cstring>
#include <string>
#include <queue>

#pragma comment(linker, "/STACK:64000000") 

using namespace std;

typedef long long int64;
typedef pair<int,int> pii;
typedef pair<int64,int64> pii64;
typedef pair<double, int> pdi;
typedef pair<double, double> pdd;
typedef pair<pii, int> piii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;

#define xn _dsfhsdfsj
#define yn _dthsdfshj

#define toMod 1000000007

inline int strToInt(string &s)
{
	int res = 0;
	int l = (int)s.length();
	for (int i = 0; i < l; ++i)
		res = res * 10 + (int)(s[i] - '0');
	return res;
}

inline string intToStr(int x)
{
	string res = "";
	while (x)
	{
		res = (char)(x % 10 + '0') + res;
		x /= 10;
	}
	return res;
}

int nt;
int N;
int L, R;
string S1, S2;
string S, SX;
int FLAG;
int tn;
int was[1 << 22];

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	tn = 0;
	cin >> nt;
	for (;nt--;)
	{
		++tn;
		int64 res = 0;
		cin >> S1 >> S2;
		N = S1.length();
		L = strToInt(S1);
		R = strToInt(S2);
		FLAG = 1;
		memset(was, 0, sizeof was);	
		for (int X = L; X <= R; ++X)
		{
			++FLAG;
			S = intToStr(X);
			for (int it = 0; it < N; ++it)
			{
				if (S[it] == '0') continue;
				SX = S.substr(it, N - it);
				if (it) SX += S.substr(0, it);
				int Y = strToInt(SX);
				if (Y <= X) continue;
				if (Y <= R && Y >= L)
				{
					if (was[Y] == FLAG) continue;
					was[Y] = FLAG;
					++res;
				}
			}
		}
		cout << "Case #" << tn << ": " << res << endl;
	}
	
	return 0;
}