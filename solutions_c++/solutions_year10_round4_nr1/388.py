#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cmath>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long Int;

#define FOR(i, a, b) for(int i=a; i<b; ++i)
#define RFOR(i, a, b) for(int i=b-1; i>=a; --i)
#define FILL(a, val) memset(a, val, sizeof(a))

#define all(c) c.begin(), c.end()
#define sz(c) (int)c.size()
#define pb push_back

#define mp make_pair
#define X first
#define Y second

const double PI = acos(-1.0);
const int INF = 1000000000;

PII operator+(const PII & a, const PII & b){return PII(a.X+b.X, a.Y+b.Y);}
PII operator-(const PII & a, const PII & b){return PII(a.X-b.X, a.Y-b.Y);}
int dot_p(const PII & a, const PII & b){return a.X*b.X + a.Y*b.Y;}
int cross_p(const PII & a, const PII & b){return a.X*b.Y - a.Y*b.X;}

int to_int(string s){
	if (s == "")
		return 0;
	istringstream iss(s);
	int n;
	iss >> n;
	return n;
}

string to_str(int n){
	ostringstream oss;
	oss << n;
	return oss.str();
}

//di[120][120];
//char di[120][120];
string di[120];
int n;

bool vali(int x)
{
	return x>=0 && x < n+n-1;
}

bool chack(int x, int y){
	//if ((n+x+y)%2 == 0)
	{
		FOR(i, 0, 2*n-1)
		FOR(j, 0, 2*n-1)
		if ((n+i+j)%2 != 0)
		{
			if (di[i][j] != ' ')
			{
				if (vali(x+x-i) && di[x+x-i][j]!=' ' && di[x+x-i][j] != di[i][j])
					return false;
				if (vali(y+y-j) && di[i][y+y-j]!=' ' && di[i][y+y-j] != di[i][j])
					return false;
			}
		}	
	}
	return true;
}

int kkk(int k)
{
	return k + 2*(int)((k-1)*k/2);
}

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);

	//freopen("A-small-attempt1.in", "r", stdin);
	//freopen("A-small-attempt1.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	FOR(t, 0, T)
	{
		scanf("%d", &n);
		string s;
		getline(cin, s);
		/*FOR(i, 0, n)		
		FOR(j, 0, i+1)
			scanf("%d", &di[i][j]);
		RFOR(i, 0, n-1)		
		FOR(j, 0, i+1)
			scanf("%d", &di[n+i][j]);
		
		int res = inf;

		FOR(i, 0, 2*n-1)
		FOR(j, 0, 2*n-1)
		{
			int r = 0;
		}
		*/

		FOR(i, 0, 2*n-1)
		{
			getline(cin, di[i]);
			di[i].resize(2*n-1, ' ');
		}

		int res = INF;
		FOR(i, 0, 2*n-1)
		FOR(j, 0, 2*n-1)
		{
			if (chack(i, j))
			{
				int r = 0;
				r = max(r, abs(i-0)+abs(j-(n-1)));
				r = max(r, abs(i-(n-1))+abs(j-0));
				r = max(r, abs(i-(n-1))+abs(j-(n+n-2)));
				r = max(r, abs(i-(n+n-2))+abs(j-(n-1)));
				res = min(res, r+1);
			}
		}

		printf("Case #%d: %d", t+1, kkk(res) - kkk(n));		
		if (t != T-1)
			printf("\n");
	}

	return 0;
}