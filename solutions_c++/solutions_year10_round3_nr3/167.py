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
#define foreach(i,c) for(map<int,int>::iterator i = (c).begin() ; i != (c).end() ; i++)

string hexm[256];
string board[513];
bool v[513][513];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.out", "w", stdout);
#endif

	hexm['0'] = "0000";
	hexm['1'] = "0001";
	hexm['2'] = "0010";
	hexm['3'] = "0011";
	hexm['4'] = "0100";
	hexm['5'] = "0101";
	hexm['6'] = "0110";
	hexm['7'] = "0111";
	hexm['8'] = "1000";
	hexm['9'] = "1001";
	hexm['A'] = "1010";
	hexm['B'] = "1011";
	hexm['C'] = "1100";
	hexm['D'] = "1101";
	hexm['E'] = "1110";
	hexm['F'] = "1111";

	int test,n,m;
	char c[130];

	scanf("%d",&test);

	for( int tt = 0 ; tt < test ; tt++ )
	{
		memset(v,false,sizeof(v));
		map<int,int> res;

		scanf("%d%d",&n,&m);

		for( int i = 0 ; i < n ; i++ )
		{
			scanf("%s",c);
			string row;
			int len = strlen(c);

			for( int j = 0 ; j < len ; j++  )
				row += hexm[toupper(c[j])];

			board[i] = row;
		}

		int cnt = m*n;

		while( cnt )
		{
			int mx = -1,mi,mj;

			for( int i = 0 ; i < n ; i++ )
			{
				for( int j = 0 ; j < m ; j++ )
				{
					if( v[i][j] )
						continue;

					int r = 1;
					for( int k = 1 ; k < min(n,m) ; k++ )
					{
						bool flag = false;

						if( i+k >= n ||
							j+k >= m ||
							i+1 >= n ||
							j+1 >= m ||
							board[i][j+k] == board[i][j+k-1] ||
							board[i+k][j] == board[i+k-1][j] ||
							v[i][j+k] ||
							v[i+k][j])
							break;

						for( int l = i+1 ; l <= i+k ; l++ )
						{
							if( v[l][j+k] || board[l][j+k] == board[l-1][j+k] || board[l][j+k] == board[l][j+k-1] )
							{
								flag = true;
								break;
							}
						}

						for( int l = j+1 ; l <= j+k ; l++ )
						{
							if( v[i+k][l] || board[i+k][l] == board[i+k][l-1] || board[i+k][l] == board[i+k-1][l] )
							{
								flag = true;
								break;
							}
						}

						if( flag )
							break;

						r = k+1;
					}

					if( r > mx )
					{
						mx = r;
						mi = i;
						mj = j;
					}
				}
			}

			for( int i = mi ; i < mi+mx ; i++ )
				for( int j = mj ; j < mj+mx ; j++ )
					v[i][j] = true;

			res[mx]++;
			cnt -= mx*mx;
		}

		printf("Case #%d: %d\n",tt+1,res.size());

		vector<pair<int,int> >v(res.begin(),res.end());

		reverse(v.begin(),v.end());

		for( int i = 0 ; i < v.size() ; i++ )
			printf("%d %d\n",v[i].first,v[i].second);
	}

	return 0;
}
