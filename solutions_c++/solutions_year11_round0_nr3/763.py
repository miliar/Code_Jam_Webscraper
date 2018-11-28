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

int main()
{
    
    #ifndef ONLINE_JUDGE 
    freopen("c_large.in","r",stdin); 
    freopen("c_large.out","w",stdout); 
    #endif

    int case_n, n, mini, sum, chk, tmp;

    scanf("%d", &case_n);    
    FOR(case_i, 1, case_n)
    {
		sum = chk = 0;
		mini = 1<<30;
		scanf("%d", &n);
		while(n--)
		{
			scanf("%d", &tmp);
			chk^=tmp;
			sum+=tmp;
			mini=min(mini,tmp);
		}
		if(chk) printf("Case #%d: NO\n", case_i);
        else printf("Case #%d: %d\n", case_i, sum-mini);
    }

    #ifndef ONLINE_JUDGE 
    fclose(stdin); 
    fclose(stdout); 
    #endif
    
    return 0;
}
