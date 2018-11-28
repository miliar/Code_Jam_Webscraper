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
		freopen("B-small-attempt1.in", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif

	int i, j, k, n, tc, s, p, t, msc;

	cin >> tc;
	For(cn, 1, tc+1)
	{
		cin >> n >> s >> p;

		int total = 0;
		while(n--)
		{
			cin >> t;
			msc = (t/3) + (t%3); //cerr<<msc<<endl;
			if(t%3==2) msc--;
			if(msc >= p) { total++; continue; }
			if(s)
			{
				if(t%3==0)
				{
					if(t >= 6) msc += 2;
					else if(t >= 2) msc ++;
				}
				else if(t >= 1) msc += 1;

				if(msc >= p) { total++; s--; }
			}
		}

		cout << "Case #" << cn << ": " << total << endl;
	}

	return 0;
}
