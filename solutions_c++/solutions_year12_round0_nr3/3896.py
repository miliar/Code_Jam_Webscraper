#include <iostream>
#include <fstream>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <cstring>

#define all(x) (x).begin(),(x).end()

using namespace std;

int A,B;

std::string itoa(int v)
{
	std::string res = "";
	while (v)
	{
		res += '0' + v % 10;
		v /= 10;
	}
	reverse(all(res));
	return res;
}

std::string split(std::string s, int shift)
{
	std::string w = "";
	std::string res = "";
	for (int i = 0; i < shift; i ++) w += s[i];
	for (int i = shift; i < s.size(); i ++) res += s[i];
	res += w;
	return res;
};

int gen(int v)
{
	set <int> st;
	string s = itoa(v);
	for (int i = 1; i < s.size(); i ++)
	{
		string q = split(s, i);
		int qn = atoi(q.c_str());
		if (A <= qn && qn <= B && qn > v)
			st.insert(qn);
	}
	return st.size();
};

void solve(int test)
{
	long long ans = 0;
	cin >> A >> B;
	for (int i = A; i <= B; i ++)
		ans += gen(i);
	cout << "Case #" << test << ": " << ans << endl;
};

int main()
{
	int T; cin >> T;
	for (int i = 0; i < T; i ++) solve(i + 1);
	return 0;
};
