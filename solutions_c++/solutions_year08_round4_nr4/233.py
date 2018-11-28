#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <fstream>
#include <vector>
#include <set>
#include <complex>
#include <map>
#include <algorithm>
#include <functional>
#include <cstdlib>
#include <cmath>
#include <string>
using namespace std;

ifstream fin("D.in");
ofstream fout("D.out");
const double EPS = 1e-10;
vector<int> perm;
int k;

string apply_perm(const string& s)
{
	if (s.empty()) return s;
	string res = s.substr(0, k);
	for (int i = 0; i < k; i++)
	{
		res[perm[i]] = s[i];
	}
	return res + apply_perm(s.substr(k));
}

int count_size(const string& s)
{
	char prev = 0;
	int res = 0;
	for (unsigned i = 0; i < s.length(); i++)
	{
		if (s[i]!=prev)
		{
			prev = s[i];
			res++;
		}
	}
	return res;
}

int main(void)
{
	int num_test_cases;
	fin >> num_test_cases;
	for (int tc = 1; tc <= num_test_cases; tc++)
	{
		fout << "Case #" << tc << ": ";
		string str;
		fin >> k >> str;
		perm.resize(k);
		for (int i = 0; i < k; i++)
		{
			perm[i] = i;
		}
		int res = count_size(str);
		while (next_permutation(perm.begin(), perm.end()))
		{
			res = min(res, count_size(apply_perm(str)));
		}
		fout << res << endl;
	}
	return 0;
}
