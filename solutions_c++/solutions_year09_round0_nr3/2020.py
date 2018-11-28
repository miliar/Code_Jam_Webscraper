#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

string s = "welcome to code jam";
string str;

int memo[501][501];

int calc(int cur,int ind)
{
	int &x = memo[cur][ind];

	if( cur >= s.size() )
		return 1;

	if( ind >= str.size() )
		return 0;

	if( x != -1 )
		return x;

	int res = 0;

	if( s[cur] == str[ind] )
		res = calc(cur+1,ind+1);

	res += calc(cur,ind+1);

	return x = res;
}

int main()
{
	freopen("3.in","rt",stdin);
	freopen("3.out","w",stdout);

	int n;

	cin >> n;
	getline(cin,str);

	for( int tt = 0 ; tt < n ; tt++ )
	{
		getline(cin,str);

		memset(memo,-1,sizeof(memo));

		printf("Case #%d: %04d\n",tt+1,calc(0,0));
	}

	return 0;
}
