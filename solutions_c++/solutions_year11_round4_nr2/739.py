#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include<sstream>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<cassert>
using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef long long ll;

#define I ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i = a ; i <= b ; i++)
#define REV(i,a,b) for(int i = a ; i >= b ; i--)
#define REP(i,n) for(int i = 0 ; i < n ; i++)

#define INF 1000000000
#define MAXN 505

int cas;
int R , C , D ; 

int wt[MAXN][MAXN];

bool check(int i, int j, int k)
{
	if(i + k - 1 >= R || j + k - 1 >= C) return false;
	if( k % 2 == 1 )
	{
		int dx , dy;
		dx = dy = 0;
		int cx = i + (k-1) / 2;
		int cy = j + (k-1) / 2;
		FOR(l,i,i+k-1)
			FOR(m,j,j+k-1)
			{
				if( (l == i && m == j) || (l == i && m == j+k-1) || (l == i+k-1 && m == j) || (l == i+k-1 && m == j+k-1) ) continue;
				dx += (l - cx) * wt[l][m];
				dy += (m - cy) * wt[l][m];
			}
		if( dx == 0 && dy == 0 ) 
		{
			//cout<<i<<" "<<j<<" "<<k<<endl;
			return true;
		}
		return false;
	}
	else
	{
		int dx, dy;
		dx = dy = 0;
		FOR(l,i,i+k-1)
			FOR(m,j,j+k-1)
			{
				if( (l == i && m == j) || (l == i && m == j+k-1) || (l == i+k-1 && m == j) || (l == i+k-1 && m == j+k-1) ) continue;
				dx += (k - 2*(l-i) - 1) * wt[l][m];
				dy += (k - 2*(m-j) - 1) * wt[l][m];
			}
		if( dx == 0 && dy == 0 ) 
		{
			//cout<<i<<" "<<j<<" "<<k<<endl;
			return true;
		}
		return false;

	}
	return false;
}

void solve()
{
	R = I ; C = I ; D = I ;
	REP(i,R) 
	{
		string s;
		cin>>s;
		REP(j,C) wt[i][j] = (s[j]-'0');
	}

	int best = -1;
	for(int i = 0 ; i < R ; i++)
		for(int j = 0 ; j < C ; j++)
			for(int k = 3 ; k <= 12 ; k++)
				if(check(i,j,k))
						best = max(best,k);
	if(best !=  -1)
		cout<<"Case #"<<cas<<": "<<best<<endl;
	else
		cout<<"Case #"<<cas<<": "<<"IMPOSSIBLE"<<endl;
}

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		cas++;
		solve();
	}


	return 0;
}
