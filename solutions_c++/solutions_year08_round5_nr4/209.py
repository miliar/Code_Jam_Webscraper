#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <cstring> 
#include <cstdlib> 
#include <cstdio> 
#include <vector> 
#include <string> 
#include <cmath> 
#include <queue> 
#include <map> 
#include <set> 

using namespace std; 

typedef vector<int> VI; 
typedef vector<string> VS; 
typedef long long ll; 

#define sz size() 
#define pb push_back 
#define MAX 0xFFFFFFF 
#define all(x) (x).begin(),(x).end() 
#define For(i,n) for(int i=0, _n=(n);i<_n;++i) 
#define For2(i,a,b) for(int i=(a), _n=(b);i<_n;++i) 
#define Forit(it,x) for(typeof((x).begin()) it=(x).begin(), ed=(x).end();it!=ed;++it) 

int a[256][256];

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int ti = 0, tn;
	scanf("%d",&tn);
	while(tn--)
	{
		int n, m, nn;
		scanf("%d %d %d",&n,&m,&nn);
		memset(a, 0, sizeof(a));
		For(i,nn) 
		{
			int x, y;
			scanf("%d %d",&x,&y);
			a[x-1][y-1] = -1;
		}
		a[0][0] = 1;
		For(i,n) For(j,m) if(a[i][j] > 0)
		{
			if(a[i+2][j+1] >= 0) a[i+2][j+1] = (a[i+2][j+1] + a[i][j]) % 10007;
			if(a[i+1][j+2] >= 0) a[i+1][j+2] = (a[i+1][j+2] + a[i][j]) % 10007;
		}
		printf("Case #%d: %d\n", ++ti, a[n-1][m-1]);
	}
}
