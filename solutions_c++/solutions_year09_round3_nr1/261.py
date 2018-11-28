#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
using namespace std;
ifstream in;
ofstream out;


void solve(int test)
{
	string s;
	getline(in, s);
	map<char, int> mp;
	vector<int> v(s.size());
	for(char c='0';c<='9';++c)
		mp[c] = -1;
	for(char c='a';c<='z';++c)
		mp[c] = -1;
	int i, j, k, m, n = s.size();
	set<char> sss;
	for(i=0;i<n;++i)
		sss.insert(s[i]);
	k = sss.size();
	if(k==1) 
	{
		__int64 res = 0, step = 1;
		for(i=0;i<n;++i)
		{
			res += step;
			step *= 2;
		}

		out << "Case #" << test << ": " << res << endl;
		return;
	}
	m = 2;
	v[0] = 1;
	i = 0;
	while(s[i]==s[i+1])
		v[++i] = 1;
	++i;
	mp[s[0]] = 1;
	mp[s[i]] = 0;
	for(;i<n;++i)
	{
		if(mp[s[i]] == -1)
			v[i] = mp[s[i]] = m++;
		else v[i] = mp[s[i]];
	}
	__int64 res = 0;
	__int64 step = 1;
	for(i=n-1;i>=0;--i)
	{
		res += (__int64)(v[i] * step);
		step *= (__int64)k;
	}
	out << "Case #" << test << ": " << res << endl;
}


int main()
{
	in.open("A-small.in");
	out.open("A-small.out");
	int kol, n;
	in >> kol;
	getline(in, string());
	for(n=1;n<=kol;++n)
		solve(n);
	in.close();
	out.close();
}