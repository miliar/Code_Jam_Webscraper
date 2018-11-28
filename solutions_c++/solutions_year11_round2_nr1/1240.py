#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <iomanip>
#include <sstream>
#include <set>
#include <deque>
#include <climits>
 
using namespace std;
 
#define EPS 1e-11
#define PI acos(-1.0)
 
#define DEBUG(n) cout << "->" << #n << " -> " << n << '\n'
#define FILL(arr,n) memset(arr,n,sizeof(arr))
#define FORUP(i,m,n) for(int i=(m),_n=(n); i<_n; i++)
#define FORDOWN(i,m,n) for(int i=(m)-1,_n=(n); i >= _n; i--)
#define FOREACH(iter,n) for(__typeof ((n).begin()) iter=(n).begin(); iter!=(n).end(); iter++)
#define ALL(n) (n).begin(),(n).end()
#define ALLSIZE(n,jum) (n),(n)+(jum)
#define FS first
#define SC second
#define SQR(x) ((x)*(x))
#define MP make_pair

//====== ilcapt ====

int main()
{
	int T;
	scanf("%d", &T);
	
	int N;
	double WP[105], OWP[105], OOWP[105];
	double WT[105];
	char board[105][105];
	
	FORUP(test,1,T+1)
	{
		scanf("%d", &N);
		FORUP(i,0,N)
			scanf("%s", board[i]);
			
		FORUP(i,0,N)
		{
			int jum = 0, play=0;
			FORUP(j,0,N)
			{
				if (board[i][j]=='1') jum++;
				if (board[i][j]!='.') play++;
			}
			WP[i] = jum*1.0/play;

		}
		
		FORUP(i,0,N)
		{
			double jum = 0.0;
			int play=0, win=0;
			FORUP(j,0,N)
			{
				if (board[i][j]=='.') continue;
				int x=0, y=0;
				FORUP(k,0,N)
				{
					if (k==i) continue;
					if (board[j][k]=='1') x++;
					if (board[j][k]!='.') y++;
				}
				WT[j] = x*1.0/y;
				jum += WT[j];
				play++;
			}
			OWP[i] = jum/play;
		}
		
		FORUP(i,0,N)
		{
			double jum = 0.0;
			int play=0;
			double temp=0.0;
			FORUP(j,0,N)
			{
				if (board[i][j]!='.')
				{
					jum += OWP[j];
					play++;
				}
			}

			OOWP[i] = jum/play;
		}
		
		printf("Case #%d:\n", test);
		FORUP(i,0,N)
			printf("%lf\n", (0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]));
	}
	return 0;
}
