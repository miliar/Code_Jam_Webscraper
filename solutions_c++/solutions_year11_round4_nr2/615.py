#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define PB push_back
#define MP(X,Y) make_pair(X,Y)
#define SZ(X) ((int)(X.size()))
#define ALL(x)   (x).begin(),(x).end()
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define F first
#define S second
#define CLEAR(A, V) memset(A, V, sizeof(A))

typedef  long long   ll;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;

template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T gcd(T a, T b){ return b?gcd(b, a%b):a;}
const double EPS = 1e-6;
const double PI = acos(-1.0);

int board[15][15],R,C;

bool sum (int x, int y, int length)
{
	
	if(x+length>R) return false;
	if(y+length>C) return false;
	int lrx = x+length-1, lry = y+length-1;
	double sumax = 0, sumay = 0;
	double centerx = double(x)+double(length-1)/2.;
	double centery = double(y)+double(length-1)/2.;
	for(int i = x; i <= lrx; i++) 
	for(int j = y; j <= lry; j++)
	{
		if(i == x and j == y) continue;
		if(i == lrx and j == lry) continue;
		if(i == lrx and j == y) continue;
		if(i == x and j == lry) continue;
		sumax += (double(i)-centerx)*double(board[i][j]);
		sumay += (double(j)-centery)*double(board[i][j]);
	}
	if(fabs(sumax)<EPS and fabs(sumay)<EPS) return true;
	return false;
}

int main(){
	int T;
	cin >> T;
	for(int caso = 1; caso <= T; caso++)
	{
		int D;
		cin >> R >> C >> D;
		for(int i = 0; i < R; i++)
		{
			string s;
			cin >> s;
			for(int j = 0; j < C; j++)
				board[i][j] = s[j]-'0'+D;
		}
/*		for(int i = 0; i < R; i++){
		for(int j = 0; j < C; j++)
		{
		cout << board[i][j];
		}
		cout << endl;
		}*/
		int best = -1;
		for(int i = 0; i < R; i++)
		for(int j = 0; j < C; j++)
		{
			for(int z = max(best,3); z <= min(R,C); z++)
			{
				if(sum(i,j,z))
				{
					best = max(z,best);
				}
			}
		}
		if(best != -1)
			printf("Case #%d: %d\n", caso, best);
		else
			printf("Case #%d: IMPOSSIBLE\n", caso);
	}
	return 0;
}

