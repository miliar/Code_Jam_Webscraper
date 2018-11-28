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

int fact(int n)
{
	if (n==0 || n ==1)
		return 1;
	return n*fact(n-1);
}

int main()
{
	bool *v = new bool[2000001];
	memset(v,false,2000001);

	int t;

	cin >> t;

	fo(i,t)
	{
		memset(v,false,2000001);
		int res = 0;
		char s[20],r[20];

		int a,b;
		cin >> a >> b;

		for(int j = a; j <= b; j ++)
			if ( v[j] == false )
			{
				int z = 1;

				itoa(j,s,10);

				int l = strlen(s);

				fo(k,l - 1)
				{
					strncpy(r,s+l-k-1,k+1);
					strncpy(r+k+1,s,l-k-1);
					r[l] = 0;
					int rev = atoi(r);
					if (((l == 1) || ( l > 1 && (r[0] != 0)) ) && rev >= a && rev <=b && v[rev] == false && j != rev )
					{
						z++;
						v[rev] = true;
					}

				}
				v[j] = true;

				if(z > 1)
					res += fact(z)/fact(2)/fact(z-2);
			}

		cout << "Case #" << i+1 << ": "<< res << endl;


	}

	return 0;
}
