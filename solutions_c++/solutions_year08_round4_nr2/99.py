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
using namespace std;
long long area(const pair<long long, long long> &p1, const pair<long long, long long> &p2,const pair<long long, long long> &p3)
{
	return p1.first * p2.second + p2.first * p3.second + p3.first * p1.second - p1.second * p2.first - p2.second * p3.first - p3.second * p1.first;
}
int main()
{
	freopen("../../google.in", "r", stdin);
	freopen("../../google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		long long n, m;
		long long u;
		cin >> n >> m >> u; 
		pair<long long, long long> p(0, 0);
		bool b = true;
		for(long long i = 0; i <= n && b; i++)
			for(long long j = 0; j <= m && b; j++)
				for(long long k = 0; k <= n && b; k++)
					for(long long q = 0; q <= m && b; q++)
					{
						if(i == k && j == q)
							continue;
						if(i == 0 && j == 0)
							continue;
						if(0 == k && 0 == q)
							continue;
						pair<long long, long long> p1(i, j), p2(k, q);
						long long ll = area(p, p1, p2);
						if(ll < 0)
							ll = -ll;
						if(ll == u)
						{
							cout << "0 0 " << i << " " << j << " " << k << " " << q << endl;
							b = false;
						}
					}
		if(b)
			cout << "IMPOSSIBLE" << endl;

		

	}
	return 0;
}
