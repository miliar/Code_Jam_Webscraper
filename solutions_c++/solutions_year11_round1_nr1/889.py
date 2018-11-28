#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <sstream>
#include <cmath>
#include <algorithm>

#define forp(a,b,i) for (int i = a; i < b; i++)
#define pb push_back
#define mp make_pair

using namespace std;

long gcd(long a, long b)	{
	if (b == 0)
		return a;
	if (a == 0)
		return b;
	return gcd(b, a % b);
}

int main()	{
	int t;
	cin >> t;
	forp(0,t,i)	{
		unsigned long long n,pd,pg;
		cin >> n >> pd >> pg;
		
		long gval = gcd(pd, 100);
		long divguy = 100 / gval;
		bool pos = true;
		
		if (pg == 100 && pd != 100)
			pos = false;
		if (pg == 0 && pd != 0)
			pos = false;
// 		cout << divguy << endl;
		if (divguy <= n && pos)
			cout << "Case #" << (i+1) << ": Possible" << endl;
		else
			cout << "Case #" << (i+1) << ": Broken" << endl;
	}
}