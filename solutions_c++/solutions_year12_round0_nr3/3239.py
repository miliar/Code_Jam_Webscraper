#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;

string integerTostring(int v)
{
	string ret = "";
	while (v > 0)
	{
		ret += '0' + v % 10;
		v /= 10;
	}
	if (ret == "") ret = "0";
	reverse(ret.begin(), ret.end());
	return ret;
}

int A, B;

bool check(int v1, int v2)
{
	string s1 = integerTostring(v1);
	string s2 = integerTostring(v2);
	if (s1.length() != s2.length()) return false;
	int L = s1.length();
	if (L == 1) return false;
	for (int i = 0; i < L; i++)
	{
		char ch = s2[L - 1];
		for (int j = L - 1; j > 0; j--)
			s2[j] = s2[j - 1];
		s2[0] = ch;
		if (s1 == s2) return true;
	}
	return false;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("lowesy_C.out", "w", stdout);
	int _, cases = 1;
	scanf("%d", &_);
	while (_--)
	{
		scanf("%d%d", &A, &B);
		int res = 0;
		for (int v1 = A; v1 <= B; v1++)
			for (int v2 = v1 + 1; v2 <= B; v2++)
				if (check(v1, v2)) res++;
		printf("Case #%d: %d\n", cases++, res);
	}
	return 0;
}