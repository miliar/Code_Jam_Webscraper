#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>

#define INF_MAX 2147483647
#define INF_MIN -2147483648
#define INF (1 << 30)
#define pi acos(-1.0)
#define SIZE 1000000
#define LL long long
#define vi vector<int>
#define vs vector<string>
#define vc vector<char>
#define sz(x) (int)(x).size()
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define ms(x, a) memset((x), (a), sizeof(x))
#define For(i, a, b) for(int i=(a); i<(b); i++)
#define Fors(i, sz) for(size_t i=0; i<sz.size(); i++)

using namespace std;


int main()
{
	#ifndef ONLINE_JUDGE
		freopen("C-small-attempt0.in", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif

	int i, j, k, n, tc, a, b;

	cin >> tc;
	For(cn, 1, tc+1)
	{
		cin >> a >> b;

		int total = 0;
		for(k=a; k<=b; k++)
		{
			if(k < 12) continue;
			if(k < 100)
			{
				if(k%10 != 0)
				{
					i = (k % 10) * 10 + (k / 10);
					if(i>k && i<=b) total++;
				}
			}
			else if(k < 1000)
			{
				if(k%10 != 0)
				{
					i = (k % 10) * 100 + (k / 10);
					if(i>k && i<=b) total++;
				}
				if(k%100 > 9)
				{
					i = (k % 100) * 10 + (k / 100);
					if(i>k && i<=b) total++;
				}
			}
		}

		cout << "Case #" << cn << ": " << total << endl;
	}

	return 0;
}
