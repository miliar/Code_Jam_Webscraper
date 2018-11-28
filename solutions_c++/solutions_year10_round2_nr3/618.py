#include <string>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

void func(int casen);

int main()
{
	int cases;
	cin >> cases;

	for(int i=0;i<cases;i++)
	  func(i+1);	
}

map<pair<int, int>, int> m;
map<pair<int, int>, int> mp;

long long p(int pos, int count)
{
	long long res=1;
	int i, j=2;

	if(pos==0)
		return 1;

	if(mp.find(make_pair<int, int>(pos, count))!=mp.end())
		return mp[make_pair<int, int>(pos, count)];

	for(i=0;i<pos;i++)
	{
		res = (res*(count-i))%100003;

		while(j<=pos && res%j==0)
		{
			res /= j;
			j++;
		}
	}

	while(j<=pos)
	{
		res /= j;
		j++;
	}

	mp[make_pair<int, int>(pos, count)] = res;

	return res;
}

long long f(int l, int n)
{
	if(l==1)
		return 1;

	if(m.find(make_pair<int, int>(l, n))!=m.end())
		return m[make_pair<int, int>(l, n)];

	int i;
	long long res=0;

	for(i=1;i<l;i++)
	{
//		cout << l << "-----" << i << "-------" << n << "(" << l-i-1 << "," << n-l-1 << ")" << endl;
		if(n-l-1 >= l-i-1)
			res = (res + (f(i, l) *p(l-i-1, n-l-1))%100003)%100003;
	}

	m[make_pair<int, int>(l, n)] = res;

//	cout << l << "," << n << "->" << res << endl;

	return res;
}

void func(int casen)
{
	int n, i=0;
	
	cin >> n;

	long long res=0;

	for(i=1;i<n;i++)
		res = (res + f(i, n))%100003;
	
	cout << "Case #" << casen << ": " << res << endl;

}