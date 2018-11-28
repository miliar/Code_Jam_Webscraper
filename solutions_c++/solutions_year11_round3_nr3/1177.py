#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <bitset>
#include <set>


#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < n; i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define inp(x) rep(i, sz(x)) cin >> (x)[i];
#define out(x) rep(i, sz(x)) cout << (x)[i];
#define sqr(x) ((x) * (x))

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

int main(int argc, char **argv)
{
	//Small  C-small-attempt0.in
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w+", stdout);

	//freopen("C-small.in", "r", stdin);

/*
	//Large
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w+", stdout);
*/
	int tt;
	cin >> tt;
	for(int t=1; t<=tt; t++)
	{
		printf("Case #%d: ", t);
		int n;
		ll l, h;
		cin >> n >> l >> h;
		ll* x=new ll[n];
		rep(i, n)
		{
			cin >> x[i];
		}
		
		ll k;
		bool ok;
		for(k=l; k<=h; k++)
		{
			ok=true;
			rep(i, n)
			{
				if(x[i]%k && k%x[i])
				{
					ok=false;
					break;
				}
			}
			if(ok) break;
		}
		if(ok) cout << k << endl;
		else cout << "NO\n";
	}
	return 0;
}
