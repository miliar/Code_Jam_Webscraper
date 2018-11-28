#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <stdio.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(a) a.begin(),a.end()
#define _(a,b) memset((a),b,sizeof(a))
#define sz(a) (int)size()

typedef unsigned long long ull;
typedef long long lint;

const int EPS = 1e-9;;
const int INF = 1000 * 1000 * 1000;

double xx1[1001],xx2[1001],yy1[1001],yy2[1001];
double k[1001],b[1001];

int main()
{
	int n;
	freopen("a_sm.in","r", stdin);
	freopen("a_sm.out", "w", stdout);

	int i,j;
	int t,T;

	cin >> T;
	for (t=1; t<=T; t++)
	{
		cin >> n;
		for (i=0; i<n; i++)
		{
			cin >> yy1[i] >> yy2[i];
			xx1[i] = 0;
			xx2[i] = 100;
			k[i] = (yy2[i] - yy1[i]) / (xx2[i] - xx1[i]);
			b[i] = yy2[i] - k[i] * xx2[i];
		}

		int ans = 0;
		for (i=0; i<n; i++)
			for (j=i+1; j<n; j++)
			if (k[j]!=k[i])
			{
				int xx = (b[i] - b[j]) / (k[j] - k[i]);
				if (xx > 0 && xx < 100)
					ans++;
			}
			printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}