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

int t,T,n;
int m,ans;

void d(int mask, int num)
{
	if (mask==1 || mask==(1<<num-2))
	{
		ans = (ans + 1) % 100003;
		return;
	}
	int i,cnt = 0,m=1;
	for (i=0; i<num; i++)
	{
		if (m & mask) cnt++;
		m = (m << 1);
	}
	if ( (1<<(cnt-2)) & mask )
	{
		for (int j=cnt-1; j<=num-2; j++)
			if (mask & (1<<j))
				mask -= (1<<j);
		d(mask,cnt);
	}
}

int main()
{
	freopen("c_sm.txt", "r", stdin);
	freopen("c_sm.out", "w", stdout);
	cin >> T;
	int i,j,k;
	for (t=0; t<T; t++)
	{
		cin >> n;
		ans = 0;
		for (i=0; i< (1<<(n-2)); i++)
			d(i+(1<<(n-2)),n);
		printf("Case #%d: %d\n",t+1,ans); 
	}

	return 0;
}