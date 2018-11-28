#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <stack>
#include <sstream>
#include <cstring>
#include <string>
#include <numeric>
#include <ctime>

using namespace std;

#define pb push_back
#define sz(x) ((int) (x).size())
#define fo(i, n) for (int i = 0; i < (n); i++)
#define rfo(i, n) for (int i = (n) - 1; i >= 0; i--)
#define clr(x, y) memset(x, y, sizeof(x))
#define sqr(x) ((x) * (x))

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef long long ll;
typedef pair<ll,ll> pll;

int main()
{
	int T;

	cin >> T;

	fo(t,T)
	{
		int res = 0;
		int max = 0;
		int onlysur = 0;
		int onlyNsur = 0;
		int Monlysur = 0;
		int MonlyNsur = 0;

		int n,s,p;
		
		cin >> n >> s >> p;

		fo(i,n)
		{
			int temp;
			cin >> temp;

			int o = temp % 3;
			int a;
			switch (o)
			{
			case 0:
				a = temp / 3;

				if (temp == 0)
				{
					if (p == 0)
					{
						max++;
						MonlyNsur++;
					}
				}
				else
				{
					if (a + 1 >= p)
					{
						max++;
						if (a+1 == p)
							Monlysur++;
					}	
				}
				break;
			case 1:
				a = temp / 3;
				if (temp == 1)
				{
					if (p <= 1)
					{
						max++;
						MonlyNsur++;
					}
				}
				else
				{
					if (a + 1 >= p)
					{
						max++;
					}
				}
				break;
			case 2:
				a = temp / 3;
				if (a+2 >= p)
				{
					max++;
					if (a+2 == p)
						Monlysur++;
				}	
				break;

			}


		}
		
		if ( s >= Monlysur )
			res = max;
		else
			res = max - (Monlysur - s);



		cout << "Case #" << t+1 << ": "<< res << endl;


	}

	return 0;
}
