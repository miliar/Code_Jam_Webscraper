#include <iostream>
#include <cassert>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <memory.h>
#include <sstream>
#include <cmath>
#include <iomanip>
#include <cstdio>
using namespace std;

#define mp make_pair

template <typename T>
string str(T x)
{
	stringstream s;
	s << fixed << setprecision(20);
	s << x;
	return s.str();
}

typedef string answer_type;

void precalc()
{
	cerr << "Precalc finished" << endl;
}

typedef long long llong;

string bin(llong x)
{
	string ret;
	for (int i = 0; x > 0; i++)
		ret.push_back('0' + (x & (1LL))), x >>= 1;
	reverse(ret.begin(), ret.end());
	return ret;
}

answer_type solve()
{
	string s;
	cin >> s;
	int n = s.size();
	llong msk = 0, num = 0, hnum = 0;
	for (int i = 0; i < n; i++)
	{
		if (s[n - i - 1] != '?')
			num |= (s[n - i - 1] - '0') * (1LL << i), msk |= (1LL << i);
		else
			hnum |= (1LL << i);
	}
	llong low = (llong)sqrt((double)num) - 2;
	llong up = (llong)sqrt((double)(num | hnum)) + 2;
	llong ans = 0;
	for (llong t = max(0LL, low); t <= min(up, 1LL << 30); t++)
	{
		if (((t * t) & msk) == num)
		{
			ans = t * t;
			goto answ;
		}
	}
	assert(false);
	answ:;
	return bin(ans);
	
}

int main()
{
	precalc();
	int T;
	cin >> T;
	cout << fixed << setprecision(10);
	cerr << fixed << setprecision(10);
	answer_type ans;
	for (int i = 1; i <= T; i++)
		ans = solve(),
		cout << "Case #" << i << ": " << ans << endl,
		cerr << "Case #" << i << ": " << ans << endl;
}
