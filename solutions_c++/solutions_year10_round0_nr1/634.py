/*****************************

******************************/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define FOR(i,n) for( i = 0 ; i<n ; i++)
#define RFOR(i,a,b)  for( i = a ; i<b ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
#define i64 __int64
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tc, cs = 1;
	cin >> tc;
	while( tc -- )
	{
		int a, b;
		cin >> a >> b;
		a = 1 << a;
		int	k = b % a;
		if( k == a - 1 )
			cout <<"Case #"<<cs++<<": "<<"ON"<<endl;
		else
			cout <<"Case #"<<cs++<<": "<<"OFF"<<endl;		
	}
	return 0;
}