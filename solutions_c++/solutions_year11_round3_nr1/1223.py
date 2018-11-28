#include<iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<sstream>
#include<map>
#include<utility>
#include<cmath>

#define REP(i,n) for(i=0; i<n; i++)
#define REPA(i,a,n) for(i=a; i<n; i++)
#define SOR(x) sort(x.begin(), x.end())
#define REV(x) reverse(x.begin(), x.end())
#define FOREACH(iter,var) for(__typeof((var).begin()) iter=(var).begin(); iter!=(var).end(); iter++)

#define PB push_back
#define VI vector<int>
#define SZ size()
#define VS vector<string>
#define MP make_pair
#define VVI vector< vector<int> >
#define INF 2000000000
#define CLR(var,val) memset(var,val,sizeof((var)))
#define S(n) scanf("%d",&n)
#define LL long long
#define LD long double

using namespace std;

int main()
{

	//freopen("test.in", "r", stdin);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
  //freopen("A-small-attempt1.in", stdin, "r"); freopen("A-small-attempt1.out", stdout, "w");
  //freopen("A-small-attempt2.in", stdin, "r"); freopen("A-small-attempt2.out", stdout, "w");

//  freopen("A-large.in", stdin, "r"); freopen("A-large.out", stdout, "w");
	int T;
	cin >> T;
	int count = 1;
	while( count <= T )
	{
		int R, C;
		cin >> R >> C;
		int i, j;
		char map[R][C];
		REP(i, R)
			REP(j, C)
				cin >> map[i][j];

		bool imp = false;
		REP(i, R)
			REP(j, C)
			{
				if( map[i][j] == '#' )
				{
					if( j+1 < C && map[i][j+1] == '#' && i+1 < R && map[i+1][j] == '#' && map[i+1][j+1] == '#' )
					{
						map[i][j] = '/';
						map[i][j+1] = '\\';
						map[i+1][j] = '\\';
						map[i+1][j+1] = '/';
					}
					else
					{
						imp = true;
						break;
					}
				}
			}

		cout << "Case #" << count << ": " << endl;
		if( imp )	cout << "Impossible" << endl;
		else
		{
			REP( i, R )
			{
				REP(j, C)
					cout << map[i][j];
				cout << endl;
			}
		}
		count++;
	}

}
