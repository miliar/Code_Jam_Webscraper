#include <iostream>
using namespace std;

string s;
string a = "welcome to code jam";
int memo [505][22];

int calc ( int ind , int len )
{
	if ( len >= 19 )
		return 1;
	if ( ind >= s.size())
		return 0;
	if ( memo [ind][len] != -1 )
		return memo [ind][len];

	int r1 = calc ( ind+1,len);
	int r2 =0;

	if (a[len]==s[ind])
		r2 = calc(ind+1,len+1);

	return memo[ind][len]= ((r1%10000) + (r2%10000) ) % 10000;

}

int main()
{
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);

	int n;
	scanf("%d\n",&n);
	for ( int t = 1 ; t <= n ; t ++)
	{
		getline(cin,s);
		memset(memo,-1,sizeof(memo));
		int res = calc(0,0);
		printf("Case #%d: %04d\n",t,res);
	}

	return 0;
}
