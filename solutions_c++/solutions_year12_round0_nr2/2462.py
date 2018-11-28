// esta3anna 3al sha2a belAllah ..
#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std ;
#define rep(i,n,m) for( int i = (int) n ; i < (int) m ; ++i )
#define	rrep(i,n,m) for( int i = (int) n ; i >= (int) m ; --i )
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define pb(x) push_back(x)
#define mp make_pair
#define mems(arr,v) memset(arr,v,sizeof arr)
#define setb(x,bit) (x|(1<<bit))
#define resetb(x,bit) (x&(~(1<<bit)))
#define is0(x,bit)((x&(1<<bit))==0)
#define is1(x,bit)((x&(1<<bit))!=0)
#define INT_MAX  2000000000
#define INT_MIN -2000000000
#define debug(x) cout << #x << " : " << x << endl
typedef unsigned long long ll;
typedef long double ld;
#define Read() freopen("input.txt","r",stdin)
#define Write() freopen("output.txt","w",stdout)
int p,n,arr[101],dp[101][101];
int CanBeSurprise[101],CanBeNotSurprise[101];
int yenfa3(int v)
{
	int output = -1;
	rep(i,0,11)
		rep(j,0,11)
	{
		int k = v-i-j;
		if (k<0||k>10)
			continue;
		if ((abs(i-j)==2&&abs(i-k)<=2&&abs(j-k)<=2)||(abs(i-k)==2&&abs(i-j)<=2&&abs(j-k)<=2)||(abs(j-k)==2&&abs(i-k)<=2&&abs(j-i)<=2))
			output =max(output,max(i,max(j,k)));
	}
	return output;
}
int meshlazem(int v)
{
	int output = -1;
	rep(i,0,11)
		rep(j,0,11)
	{
		int k = v-i-j;
		if (k<0||k>10)
			continue;
		if (abs(i-j)<2&&abs(i-k)<2&&abs(j-k)<2)
			output =max(output,max(i,max(j,k)));
	}
	return output;
}
int rec(int indx , int s)
{
	if (indx == n)
		return (!s)?0:INT_MIN;
	if (dp[indx][s]!=-1)
		return dp[indx][s];
	if (s&&CanBeSurprise[indx]!=-1)
		dp[indx][s] = max(rec(indx+1,s),(rec(indx+1,s-1)+(int)(CanBeSurprise[indx]>=p)));
	else
		dp[indx][s] = rec(indx+1,s);
	if(CanBeNotSurprise[indx]>=p)
		dp[indx][s] = max(dp[indx][s],rec(indx+1,s)+1);
	return dp[indx][s];
}
int main ()
{
	Read();
	Write();
	int cases,s;
	cin >> cases;
	rep(C,1,cases+1)
	{
		cin >> n >> s >> p;
		rep(i,0,n){
			cin >> arr[i];
			CanBeSurprise[i] = yenfa3(arr[i]);
			CanBeNotSurprise[i] = meshlazem(arr[i]);
		}
		mems(dp,-1);
		int koko = rec(0,s);
		if (koko<0)
			koko = 0;
		cout << "Case #" << C << ": " << koko << endl ;
	}
}