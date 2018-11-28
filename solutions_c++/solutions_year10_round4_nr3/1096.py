#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<sstream>
#include<deque>
#include<stack>
#include<string>
#include<cstring>

using namespace std;

#define eps 1e-12
#define oo (int)1e9
#define foreach(i,c) for(__typeof((c).begin()) i = (c).begin() ; i != (c).end() ; i++)

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.txt", "w", stdout);
	#endif

	int test,r,x1,x2,y1,y2;

	scanf("%d",&test);

	for( int tt = 1 ; tt <= test ; tt++ )
	{
		vector<string> v(401,string(401,'0'));
		scanf("%d",&r);

		int cells = 0;

		for( int i = 0 ; i < r ; i++ )
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);

			for( int j = x1 ; j <= x2 ; j++ )
			{
				for( int k = y1 ; k <= y2 ; k++ )
				{
					v[j][k] = '1';
				}
			}
		}

		int cnt = 0;
		bool flag = true;

		while( flag )
		{
			vector<string> nv(401,string(401,'0'));
			flag = false;

			for( int i = 1 ; i < 401 ; i++ )
			{
				for( int j = 1 ; j < 401 ; j++ )
				{
					if( v[i-1][j] == '1' && v[i][j-1] == '1' )
						flag=true,nv[i][j] = '1';
					if( v[i][j]=='1'&&(v[i-1][j] == '1'|| v[i][j-1] == '1') )
						flag=true,nv[i][j] = '1';
				}
			}

			v = nv;
			cnt++;
		}

		printf("Case #%d: %d\n",tt,cnt);
	}

	return 0;
}
