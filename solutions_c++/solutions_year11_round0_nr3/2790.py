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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

ifstream in;
ofstream out;
long long ans;
bool work();
int main()
{
	int t;
	in.open("small.in");
	out.open("out.out");
	in>>t;
	for (int i = 0; i < t; i++)
	{
		out<<"Case #"<<i + 1<<": ";
		if (work())
			out<<ans<<endl;
		else
			out<<"NO"<<endl;
	}
	return 0;
}

bool work()
{
	long long n,tmp, sum = 0, alt = 0;;
	in>>n;
	vector<int> v;
	for (int i = 0; i < n; i++)
	{
		in>>tmp;
		v.push_back(tmp);
		sum += tmp;
		alt ^= tmp;
	}
	if (alt != 0) 
		return false;
	sort(v.begin(), v.end());
	ans = sum - v[0];
	return true;
	
}
