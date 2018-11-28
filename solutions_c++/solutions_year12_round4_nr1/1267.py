#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define FOR(i, a, b) for(int i(a); i<b; i++)
#define REP(i, n) FOR(i, 0, n)
#define ALL(a) a.begin(), a.end()
#define CLEAR(a, b) memset(a, b, sizeof(x))

#define mp make_pair
#define pb push_back

void solve();

int T;

int main()
{
	freopen("R2AL.in", "r", stdin);
	freopen("R2A.out", "w", stdout);

	std::ios_base::sync_with_stdio(0);
	
	cin>>T;
	REP(t, T)
	{
		cout<<"Case #"<<t+1<<": ";
		solve();
		cout<<endl;
	}

	fclose(stdout);
}

int N;
int d[10000], l[10000];
//int dp[10000];
int D;

void solve()
{
	cin>>N;
	REP(i, N)
	{
		cin>>d[i]>>l[i];
	}
	cin>>D;
	l[0]=d[0];//max(d[0], l[0]);
	FOR(i, 1, N)
	{
		int tt=-1;
		REP(j, i)
		{
			if (l[j]>=(d[i]-d[j]))
				tt=max(tt, min(l[i], d[i]-d[j]));
		}
		tt=max(tt, 0);
		l[i]=tt;
	}
	REP(i, N)
	{
		if(l[i]>=D-d[i])
		{
			cout<<"YES";
			return;
		}
	}
	cout<<"NO";
}