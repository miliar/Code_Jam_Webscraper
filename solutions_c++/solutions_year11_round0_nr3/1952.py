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
#pragma comment(linker,"/STACK:16777216")
#pragma warning(disable:4786)

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

#define FOR(i,n) for( i = 0 ; i<(n) ; i++)
#define RFOR(i,a,b)  for( i = (a) ; i<(b) ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))

#define all(a) a.begin(),a.end()
#define pb push_back

#define i64 long long
#define pi (2.0*acos(0.0))
#define eps (1e-9)

typedef pair< int , int >  pii;
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.ans","w",stdout);
	int tc, cs = 1, n, i;
	cin >> tc;
	while( tc -- )
	{
		int p, res = 0;
		int mn = 1000000000, sm = 0;
		cin >> n;
		for(i = 0; i < n ; i ++ )
		{
			cin >> p;
			res ^= p;
			if( p < mn ) mn = p;
			sm += p;
		}
		printf("Case #%d: ", cs ++);
		if( res ) cout << "NO"<<endl;
		else cout << sm - mn << endl;
	}

	return 0;
}