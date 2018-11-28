#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;
long long w, h;
long long len(long long a, long long b)
{
	return a * a + b * b;
}
long long calc(long long a, long long b, long long c, long long d)
{
	long long res;
	long long first, second;
	if(c == 0)
	{
		first = 1200000000;
	}
	else
	{
		if(c < 0)
			first = a / (-c) + 1;
		else
			first = (w - 1 - a) / c  + 1;
	}
	if(d == 0)
	{
		second = 1200000000;
	}
	else
	{
		if(d < 0)
			second = b / (-d) + 1;
		else
			second = (h - 1 - b) /d  + 1;
	}
	return min(first, second);
}
long long gcd(long long a, long long b)
{
	if(a == 0)
		return b;
	if(b == 0)
		return a;
	if(a < 0)
		a = -a;
	if(b < 0)
		b = -b;
	if(a < b)
		swap(a, b);
	long long x;
	while(b)
	{
		x = a % b;
		a = b;
		b =x;
	}
	return a;
}
long long c, a, b, d;
set<pair<long long, long long> > visited;
void dfs(long long x, long long y)
{
	visited.insert(make_pair(x, y));
	if(x + a >= 0 && x + a < w && y + b >= 0 && y + b < h)
	{
		if(visited.find(make_pair(x + a, y + b)) == visited.end())
			dfs(x + a, y + b);
	}
	if(x + c >= 0 && x + c < w && y + d >= 0 && y + d < h)
	{
		if(visited.find(make_pair(x + c, y + d)) == visited.end())
			dfs(x + c, y + d);
	}
}

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		//long long a, b, c, d;
		
		cin >> w >> h;
		cin >> a >> b >> c >> d;
		long long x, y;
		cin >> x >> y;
		int xe = x, ye = y;
		if(a * d == c * b)
		{
			visited.clear();
			dfs(x, y);
			long long cnt = visited.size();
			cout << cnt << endl;
			continue;
		}
		else
		{
			/*long long cnt = 0;
			while(x >= 0 && x < w && y >= 0 && y < h)
			{
				cnt += calc(x, y, c, d);
				x += a;
				y += b;
			}*/
			visited.clear();
			dfs(x, y);
			long long cnt = visited.size();
			cout << cnt << endl;
			//cout << cnt << endl;
		}

	}
	return 0;
}
