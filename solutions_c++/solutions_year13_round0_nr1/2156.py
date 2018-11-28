# include <iostream>
# include <fstream>
# include <sstream>
# include <algorithm>
# include <cstdio>
# include <cmath>
# include <numeric>
# include <cstdlib>
# include <cstring>
# include <vector>
# include <list>
# include <set>
# include <map>
# include <stack>
# include <queue>
# include <cctype>
# include <climits>
# include <complex>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,PII> TRI;
typedef vector<string> VS;

#define GI ({int t;scanf("%d",&t);t;})
#define REP(i,a,b) for(int i=a;i<b;i++)
#define FOR(i,n) REP(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define bitcount(x) __builtin_popcount(x)
#define pb push_back
#define mp make_pair
#define mt(a,b,c) mp(a,mp(b,c))
#define EPS (double)(1e-9)
#define INF 1000000000
#define MOD 1000000007
#define PI (double)(3.141592653589793)

inline int ni()
{
	register int r=0,c;
	for(c=getchar_unlocked();c<=32;c=getchar_unlocked());
	if(c=='-')
		return -ni();
	for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar_unlocked());
	return r;
}

bool check(VS &s, char ch)
{
	int cnt1, cnt2;

	REP(i,0,4)
	{
		cnt1 = cnt2 = 0;
		REP(j,0,4)
		{
			cnt1 += (s[i][j] == ch);
			cnt2 += (s[i][j] == 'T');
		}
		if(cnt1 >= 3 && cnt1 + cnt2 == 4)
			return true;

		cnt1 = cnt2 = 0;
		REP(j,0,4)
		{
			cnt1 += (s[j][i] == ch);
			cnt2 += (s[j][i] == 'T');
		}
		if(cnt1 >= 3 && cnt1 + cnt2 == 4)
			return true;
	}

	cnt1 = (s[0][0] == ch) + (s[1][1] == ch) + (s[2][2] == ch) + (s[3][3] == ch);
	cnt2 = (s[0][0] == 'T') + (s[1][1] == 'T') + (s[2][2] == 'T') + (s[3][3] == 'T');
	if(cnt1 >= 3 && cnt1 + cnt2 == 4)
			return true;

	cnt1 = (s[3][0] == ch) + (s[2][1] == ch) + (s[1][2] == ch) + (s[0][3] == ch);
	cnt2 = (s[3][0] == 'T') + (s[2][1] == 'T') + (s[1][2] == 'T') + (s[0][3] == 'T');
	if(cnt1 >= 3 && cnt1 + cnt2 == 4)
			return true;

	return false;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	VS s(4);
	bool full, x, y;

	t = GI;

	REP(tcase,1,t+1)
	{
		full = true;

		REP(i,0,4)
		{
			cin>>s[i];
			REP(j,0,4)
				if(s[i][j] == '.')
					{full = false; break;}
		}

		x = check(s,'X');
		y = check(s,'O');

		if(x && y)
			printf("Case #%d: Draw\n",tcase);
		else if(x)
			printf("Case #%d: X won\n",tcase);
		else if(y)
			printf("Case #%d: O won\n",tcase);
		else if(full)
			printf("Case #%d: Draw\n",tcase);
		else
			printf("Case #%d: Game has not completed\n",tcase);
	}
		
	return 0;
}

