#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FORE(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define CLEAR(x,with) memset(x,with,sizeof(x))  

#define pb push_back
#define all(x) (x).begin(),(x).end()
#define sz(a) int((a).size())
#define MOD 10007

typedef pair<int,int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;


int main()
{
	int numCases;
	cin >> numCases;

	for(int c=1; c<=numCases; c++)
	{
		int H, W, R;

		cin >> H >> W >> R;

		int data[101][101];
		int rook[101][101];
		for(int i=0; i<H; i++) for(int j=0; j<W; j++){ data[i][j] = 0; rook[i][j] = 0; }
		data[0][0] = 1;

		for(int i=0; i<R; i++)
		{
			int x, y;
			cin >> x >> y;
			rook[x-1][y-1] = 1;
		}

		for(int i=0; i<H; i++)
		{
			for(int j=0; j<W; j++)
			{
				if(rook[i][j] == 1) continue;
				if( i-1 >= 0 && j-2 >= 0)
					data[i][j] += data[i-1][j-2];
				if( i-2 >= 0 && j-1 >= 0)
					data[i][j] += data[i-2][j-1];
				data[i][j] %= MOD;
			}
		}



		int ans = 0;
		cout << "Case #" << c << ": " << data[H-1][W-1] << endl;
	}

	return 0;
}
