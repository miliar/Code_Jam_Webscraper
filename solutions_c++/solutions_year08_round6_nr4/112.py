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

int a[32][32], b[32][2], c[32];

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int ti = 0, tn;
	scanf("%d",&tn);
	while(tn--)
	{
		int n, m;
		scanf("%d",&n);
		memset(a, 0, sizeof(a));
		For(i,n-1)
		{
			int t1, t2;
			scanf("%d %d",&t1,&t2);
			a[t1-1][t2-1] = a[t2-1][t1-1] = 1;
		}
		scanf("%d",&m);
		For(i,m-1)
		{
			scanf("%d %d", &b[i][0], &b[i][1]);
			b[i][0]--; b[i][1]--;
		}
		For(i,n) c[i] = i;
		do
		{
			For(i,m-1)
				if(!a[c[b[i][0]]][c[b[i][1]]]) goto aa;
			goto yes;
aa:;
		} while(next_permutation(c,c+n));
		printf("Case #%d: NO\n", ++ti);
		continue;
yes:;
		printf("Case #%d: YES\n", ++ti);
	}
}
