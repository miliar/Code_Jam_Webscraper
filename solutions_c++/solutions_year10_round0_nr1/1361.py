#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

void OpenSmall(string leter)
{
	string inName = leter + "-small.in";
	string outName = leter + "-small.out";
	freopen(inName.c_str(), "r", stdin);
	freopen(outName.c_str(), "w", stdout);
}

void OpenLarge(string leter)
{
	string inName = leter + "-large.in";
	string outName = leter + "-large.out";
	freopen(inName.c_str(), "r", stdin);
	freopen(outName.c_str(), "w", stdout);
}

int pow2(int n)
{
	int ans = 1;
	for(int i = 0; i < n; ++i)
		ans <<= 1;
	return ans;
}

int main()
{
	OpenLarge("A");
	int tc;
	cin>>tc;
	char *outp[] = {"OFF", "ON"};
	for(int Case = 0; Case < tc; Case++)
	{
		int n, k;
		cin >> n >> k;
		cout<<"Case #"<<Case+1<<": ";
		int ans = 0;
		if( k != 0 && (k + 1)%pow2(n) == 0 )
			ans = 1;
		cout << outp[ans] << endl;
	}

	return 0;
}