#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctype.h>
#include <bitset>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef istringstream iss;
typedef ostringstream oss;

#define d2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a))) 
#define cl(a, val) memset(a, val, sizeof(a))
#define deb(x) cout<<#x<<" = "<<(x)<<endl
#define FG(a, b) for((a) = (b); (a) >= 0; (a)--)
#define FD(a, b) for((a) = 0; (a) < (b); (a)++)
#define all(a) (a).begin(),(a).end() 
#define sz(a) int((a).size())
#define PB push_back
#define INF 0x3fffffff
#define Y second
#define X first

char in[] = "D-small-attempt0.in";
char out[] = "D-small-attempt0.out";

int n, m;

int size(string s)
{
	int res = 0;
	for(int i = 1; i < sz(s); i++)
		if( s[i] != s[i-1] ) res++;
	return res + 1;
}

int main()
{
	freopen(in, "rt", stdin);
	freopen(out, "wt", stdout);

	int i, j, k;
	int T, t, res;
	scanf("%d", &T);

	for(t = 1; t <= T; t++)
	{
		char s1[10000];
		int mn = INF;
		scanf("%d\n%s", &k, s1);
		string s(s1);
		vi p(k);
		FD(i, k) p[i] = i + 1;

		do
		{
			string t(s);
			for(i = 0; i < sz(s); i++)
				t[i] = s[k*(i/k)+p[i%k]-1];
		
			if( mn > size(t) )
				mn = size(t);
		}
		while( next_permutation(all(p)) );
		

		printf("Case #%d: %d\n", t, mn);
	}


	return 0;
}