#include <iostream>
#include <stdio.h>
#include <cstring> //for strlen, memcpy and memset.
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;
#define FOR(i,a,b) for(int i(a), _n(b); i<=_n; i++)
#define FORD(i,a,b) for(int i(a), _n(b); i>=_n; i--)
#define ALL(c) (c).begin(),(c).end()
#define TR(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define PR(c,x) ((c).find(x) != (c).end()) 
#define CP(c,x) (find(all(c),x) != (c).end()) 
#define SZ(a) int((a).size())a
#define X first
#define Y second
#define pb push_back
#define MEMST(a,i) memset(a,i,sizeof(a))
typedef vector<int> VI; 
typedef vector<VI> VVI; 
typedef pair<int,int> PII; 
//#define ONLINE_JUDGE

const int MAXN = 1000+10;

int a[MAXN];
bool visited[MAXN];

int main()
{
    
    #ifndef ONLINE_JUDGE 
    freopen("d_large.in","r",stdin); 
    freopen("d_large.out","w",stdout); 
    #endif

    int case_n, n, sum, tmp, cur;

    scanf("%d", &case_n);
    FOR(case_i, 1, case_n)
    {
		scanf("%d", &n);
		FOR(i, 1, n) scanf("%d", &a[i]);
		MEMST(visited, 0);
		sum = tmp = 0;
		cur = 1;
		while(1)
		{
			if(!visited[cur])
			{
				visited[cur]=1;
				cur=a[cur];
				tmp++;
			}
			else 
			{
				if(tmp==1) tmp = 0;
				sum+=tmp;
				// printf("cur=%d, sum=%d\n", cur, sum);
				tmp=0;
				for(cur=1; cur<=n && visited[cur]; cur++);
				if(cur==n+1) break; 
			}
		}
        printf("Case #%d: %d.000000\n", case_i, sum);
    }

    #ifndef ONLINE_JUDGE 
    fclose(stdin); 
    fclose(stdout); 
    #endif
    
    return 0;
}
