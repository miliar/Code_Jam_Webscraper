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
#include <ctime>

using namespace std;
 
#define EPS 1e-11
#define PI acos(-1.0)

typedef pair<int,int> pii;
typedef pair<int, pii> piii;
 
#define DEBUG(n) cout << "->" << #n << " -> " << n << '\n'
#define FILL(arr,n) memset(arr,n,sizeof(arr))
#define FORUP(i,m,n) for(int i=(m),_n=(n); i<_n; i++)
#define FORDOWN(i,m,n) for(int i=(m)-1,_n=(n); i >= _n; i--)
#define FOREACH(iter,n) for(__typeof ((n).begin()) iter=(n).begin(); iter!=(n).end(); iter++)
#define ALL(n) (n).begin(),(n).end()
#define ALLSIZE(n,jum) (n),(n)+(jum)
#define FS first
#define SC second
#define MP make_pair
#define SQR(x) ((x)*(x))

//====== ilcapt ====

int main()
{
	int T, N, S, p;
	scanf("%d", &T);
	
	FORUP(test,1,T+1)
	{
		int ans = 0;
		int temp = 0, x;
		scanf("%d%d%d", &N, &S, &p);
		
		FORUP(i,0,N)
		{
			scanf("%d", &x);
			x -= p;
			if (x > 0)
			{
				if (x/2 >= (p-1)) ans++;
				else if (x/2 == (p-2)) temp++;
			}
			else if (x == 0)
			{
				if (p == 2) temp++;
				if (p < 2) ans++;
			}
		}
		
		ans += min(temp,S);
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}
