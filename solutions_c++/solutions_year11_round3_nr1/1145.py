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
	
	FORUP(test,1,T+1)
	{
		int N, M;
		char board[55][55];
		
		scanf("%d%d", &N, &M);
		
		FORUP(i,0,N)
			scanf("%s", board[i]);
			
		bool bisa=true;
		
		FORUP(i,0,N)
		{
			FORUP(j,0,M)
				if (board[i][j]=='#')
				{
					if (i+1>=N || j+1>=M) {bisa=false;}
					else if (board[i][j+1]=='#' && board[i+1][j+1]=='#' && board[i+1][j]=='#')
					{
						board[i][j]='/';
						board[i][j+1]='\\';
						board[i+1][j]='\\';
						board[i+1][j+1]='/';
					}
					else bisa=false;
				}
		}
		
		printf("Case #%d:\n", test);
		if (!bisa)
			printf("Impossible\n");
		else
		{
			FORUP(i,0,N)
				printf("%s\n", board[i]);
		}
	}
	return 0;
}
