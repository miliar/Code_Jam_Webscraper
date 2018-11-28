#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <cassert>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(),a.end()
#define _(a,b) memset((a),b,sizeof(a))

typedef unsigned long long ull;
typedef long long lint;

const int INF = 1000 * 1000 * 1000;
const double EPS = 1e-9;
const int base = INF;

int t,T;
int a[5];
lint gg[5];

lint gcd(lint a,lint b)
{
	if (b==0) return a;
	else return gcd(b,a%b);
}

lint lcm(lint a, lint b)
{
	return a / gcd( a, b ) * b;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int j;
	cin >> T;
	for (t=1; t<=T; t++)
	{
		int i,n;
		cin >> n;
		j = 0;
		for (i=0; i<n; i++)
		{
			int k,x;
			cin >> x;
			bool find = false;
			for (k=0; k<j; k++)
				if (a[k]==x)
					find = true;
			if (!find)
			{
				a[j] = x;
				j++;
			}
		}
		n = j;
		int im = abs(a[1] - a[0]);
		for (i=0; i<n; i++)
			for (j=i+1; j<n; j++)
				im = gcd(im,abs(a[j]-a[i]));
		for (i=0; i<n; i++)
		{
			gg[i] = a[i] % im;
			if(gg[i]!=0) gg[i] = im - gg[i];
		}
		lint ans = gg[0];
		for (i=0; i<n; i++)
			ans = min(ans,gg[i]);
		for (i=0; i<n; i++)
			gg[i] -= ans;
		lint add = im;
		for (i=0; i<n; i++)
			if (gg[i]!=0)
				add = lcm(add,gg[i]);
		if (add!=im)
			ans += add;
		cout << "Case #" << t << ": ";
		cout << ans << endl;
	}

	return 0;
}