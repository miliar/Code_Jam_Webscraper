#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<sstream>
#include<map>
#include<queue>
#include<set>
#define vvi vector<vector<int> >
#define co continue
#define pb push_back
#define vi vector<int>
#define vs vector<string>
#define br break
#define re return
#define ALL(v) v.begin(),v.end() 

#define REP(i,n) for(int i=0;i<(int) n;i++)
#define LL long long
#define SZ size()
#define INF (2<<29)

#define pii pair<int ,int>
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin() ; it!=(c).end() ;it++)

using namespace std;
#define MOD 10007
int R , H , W;
LL memo[101][101];
bool A[101][101];
LL solve(int x , int y)
{
	if(x==H-1 && y==W-1)
	{
		return 1;
	}
	if(x>=H || y>=W) return 0;
	if(A[x][y]==1) return 0;
	LL & res = memo[x][y];
	if(res==-1)
	{
		res = 0;
		res += solve(x+2 , y +1);
		res %= MOD;
		
		res+=solve(x+1 , y+2);
		res %= MOD;
	}
	return res;
}
int main()
{
	int kases;
	cin>>kases;
	for(int kase = 1 ; kase <= kases ; kase++)
	{
		memset(A , false , sizeof(A));
		memset(memo , -1 , sizeof(memo));
		cin>>H>>W>>R;
		REP(i,R)
		{
			int r , c;
			cin>>r>>c;
			A[r-1][c-1] = 1;
		}
		LL res = solve( 0 , 0);
		res %= MOD;
		cout<<"Case #"<<kase<<": "<<res<<endl;
		
	}
	return 0;
}
