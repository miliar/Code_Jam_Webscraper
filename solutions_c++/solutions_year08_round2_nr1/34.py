#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <queue>

using namespace std;

typedef long long LL;
typedef pair <int,int> pii;
typedef vector <int> vi;
typedef vector <double> vd;
typedef vector <string> vs;
typedef vector <LL> vll;
typedef vector <char> vc;

////////////////////


int tc, ntc;

LL px[200000], py[200000];
int n;
LL A,B,C,D,px0,py0,M;

LL num[3][3];

bool ok(int a, int b, int c)
{
	int xa = a/3, ya = a%3;
	int xb = b/3, yb = b%3;
	int xc = c/3, yc = c%3;
	
	if ((xa+xb+xc)%3 != 0) return false;
	if ((ya+yb+yc)%3 != 0) return false;
	return true;	
}

LL calc(int a, int b, int c)
{
	int xa = a/3, ya = a%3;
	int xb = b/3, yb = b%3;
	int xc = c/3, yc = c%3;

	LL na = num[xa][ya];
	LL nb = num[xb][yb];
	LL nc = num[xc][yc];
	
	if (a == b && a == c)
		return na*(na-1)*(na-2) / 6;

	if (a == b)
		return na*(na-1)/2 * nc;

	if (b == c)
		return nb*(nb-1)/2 * na;	
	
	return na*nb*nc;
}

int main()
{
	scanf("%d",&ntc);	
	int i,j,k;
	LL x, y;
	LL res;
	for (tc = 1; tc<=ntc; tc++)
	{
		scanf("%d %lld %lld %lld %lld %lld %lld %lld",&n,&A,&B,&C,&D,&px0,&py0,&M);
		
		x = px0; y = py0;
		px[0] = x; py[0] = y;
		for (i=1; i<n; i++)
		{
			x = (A*x+B) % M;
			y = (C*y+D) % M;
			px[i] = x;
			py[i] = y;
		}
		
		memset(num,0,sizeof(num));
		for (i=0; i<n; i++)
		{
			num[ px[i]%3 ][ py[i]%3 ]++;
		}

		//for (i=0; i<n; i++) printf("%lld %lld\n",px[i],py[i]);
		//printf("\n");
		
				
		res = 0;
		for (i=0; i<9; i++) for (j=i; j<9; j++) for (k=j; k<9; k++) if (ok(i,j,k))
		{
			//printf("%d %d %d : ",i,j,k);
			//printf("%lld %lld %lld ",num[i/3][i%3],num[j/3][j%3],num[k/3][k%3]);
			//printf(": %lld\n",calc(i,j,k));
			
			res += calc(i,j,k);
		}
		
		printf("Case #%d: %lld\n",tc,res);
		
	}
}