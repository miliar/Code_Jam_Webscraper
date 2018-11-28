#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<limits.h>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std ;
typedef vector<int> vi;
typedef vector<bool> vb;
#define rep(i,n,m) for( int i = (int)(n), _m = (int)(m) ; i < _m ; ++i )
#define	rrep(i,n,m) for( int i = (int)(n), _m = (int)(m) ; i >= _m ; --i )
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define pb(x) push_back(x)
#define mp make_pair
#define mems(arr, v) memset(arr, v, sizeof arr)
#define setb(mask, bit) ((mask)|((1LL)<<(bit)))
#define resetb(mask, bit) ((mask)&(~((1LL)<<(bit))))
#define is0(mask, bit)(((mask)&((1LL)<<(bit)))==0)
#define is1(mask, bit)(((mask)&((1LL)<<(bit)))!=0)
#define INT_MAX  2000000000
#define INT_MIN -INT_MAX
#define EPS 1e-1
#define debug(x) cout << #x << " : " << x << endl
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
#define Read() freopen("in.in","r",stdin)
#define Write() freopen("out.txt","w",stdout)

char a[4][4];
bool ok(char c, char koko)
{
	return koko == c || koko == 'T';
}

bool isWin(char c)
{//horizontal
	rep(j,0,4)
	{
		bool win = true;
		rep(i,0,4)
		{
			if(!ok(c,a[j][i]))
			{
				win = false;
				break;
			}
		}
		if(win)
			return true;
	}
	//vertical
	rep(j,0,4)
	{
		bool win = true;
		rep(i,0,4)
		{
			if(!ok(c, a[i][j]))
			{
				win = false;
				break;
			}
		}
		if(win)
			return true;
	}

	//diagonal
		bool win = true;
		rep(i,0,4)
		{
			if(!ok(c, a[i][i]))
			{
				win = false;
				break;
			}
		}
		if(win)
			return true;
	//diagonal  /
		bool iwin = true;
		rep(i,0,4)
		{
			if(!ok(c, a[i][4-i-1]))
			{
				iwin = false;
				break;
			}
		}
		if(iwin)
			return true;
	return false;
}
string result()
{
	if(isWin('X'))
		return "X won";
	if(isWin('O'))
		return "O won";
	rep(i,0,4)
		rep(j,0,4)
			if(a[i][j]=='.')
				return "Game has not completed";
	return "Draw";
}
int main()
{
	Read();
	Write();
	int t;
	cin>>t;
	rep(test, 1, t+1)
	{
		rep(i,0,4)
			rep(j,0,4)
				cin>>a[i][j];
		cout<<"Case #"<<test<<": "<<result()<<endl;
	}
}