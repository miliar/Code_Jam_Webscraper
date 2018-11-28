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
#include <stack>
#include <set> 

using namespace std; 

typedef vector<int> VI; 
typedef vector<string> VS; 
typedef long long ll; 

#define sz size() 
#define pb push_back 
#define MAX 0x3FFFFFFF 
#define all(x) (x).begin(),(x).end() 
#define For(i,n) for(int i=0, _n=(n);i<_n;++i) 
#define For2(i,a,b) for(int i=(a), _n=(b);i<_n;++i) 

int a[64];
char p[64][64];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int tn;
	int ti=0;
	scanf("%d",&tn);
	while(tn--)
	{
		int n;
		scanf("%d",&n);
		memset(a,0,sizeof(a));
		For(i,n) 
		{
			scanf("%s",p[i]);
			For(j,n) if(p[i][j] == '1') a[i] = j;			
		}
		int ans = 0;
		For(i,n)
		{
			For2(j,i,n) 
				if(a[j] <= i) 
				{
					for(int k = j; k > i; k--)
					{
						char tmp[64];
						strcpy(tmp, p[k]);
						strcpy(p[k], p[k-1]);
						strcpy(p[k-1], tmp);
						swap(a[k], a[k-1]);
						ans++;
					}
					break;
				}
		}
		printf("Case #%d: %d\n", ++ti, ans);
	}
}

/*
3
2
10
11
3
001
100
010
4
1110
1100
1100
1000

*/

