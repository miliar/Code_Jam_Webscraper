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

const int MXN = 100+10;

char str[MXN], comb[9][9], oppo[9][9];

inline int cast(char c)
{
	switch(c)
	{
		case 'Q': return 0;
		case 'W': return 1;
		case 'E': return 2;
		case 'R': return 3;
		case 'A': return 4;
		case 'S': return 5;
		case 'D': return 6;
		case 'F': return 7;
		default: return 8;
	}
}

int main()
{
    
    #ifndef ONLINE_JUDGE 
    freopen("b_large.in","r",stdin); 
    freopen("b_large.out","w",stdout); 
    #endif

    int case_n, n;

    scanf("%d", &case_n);
    FOR(case_i, 1, case_n)
    {
		MEMST(oppo, 0);
		MEMST(comb, 0);
		
		char s[4];
		int u, v;
		
		scanf("%d", &n);
		FOR(i,1,n) 
		{
			scanf("%s", &s);
			// printf("%s\n", s);
			u=cast(s[0]);
			v=cast(s[1]);
			comb[u][v] = comb[v][u] = s[2];
			// printf("comb[%d][%d]=%c\n", u, v, comb[u][v]);
		}
		
		scanf("%d", &n);
		FOR(i,1,n) 
		{
			scanf("%s", &s);
			// printf("%s\n", s);
			u=cast(s[0]);
			v=cast(s[1]);
			oppo[u][v] = oppo[v][u] = 1;
			// printf("oppo[%d][%d]=%d\n", u, v, oppo[u][v]);
		}
		
		scanf("%d", &n);
		scanf("%s", &str);
		// printf("%s\n", str);
		// inputing finished
		
		int start = 0; // last idx; start idx
		char opstat[9]; 
		FOR(i,0,n-1)
		{
			if(start == i) // in case for the previous clearing
			{
				FOR(j,0,8) opstat[j]=oppo[cast(str[start])][j]; // intialize
				// FOR(j,0,8) printf("%d ", opstat[j]); printf(" is init opstate\n");
				continue;
			}
			u = cast(str[i]), v = cast(str[i-1]);
			if(comb[u][v] != 0) // see if the last 2 is matched
			{
				str[i] = comb[u][v];
				str[i-1] = 'o'; // omitting symbol
				// printf("str[%d] become: %c\n", i, str[i]);
				FOR(j,0,7) opstat[j]-=oppo[v][j]; // update the opposite state
				// FOR(j,0,8) printf("%d ", opstat[j]); printf(" is -1 opstate\n");
			}
			else // see if the opposed pair exists
			{
				if( opstat[u]!= 0) // opposed pair exists
				{
					start = i+1;
					MEMST(opstat, 0);
					// FOR(j,0,8) printf("%d ", opstat[j]); printf(" is clear opstate\n");
					// printf("start=%d\n", start);
				}
				else 
				{
					FOR(j,0,7) opstat[j]+=oppo[u][j]; // counting
					// FOR(j,0,8) printf("%d ", opstat[j]); printf(" is +1 opstate\n");
				}
			}
		}
		
        printf("Case #%d: [", case_i);
        u = 0;
		FOR(i,start,n-1)
        {
			if(str[i]=='o') continue;
			if(u==0)
			{
				printf("%c", str[i]);
				u = 1;
			}
			else printf(", %c", str[i]);
		}
		printf("]\n");
    }

    #ifndef ONLINE_JUDGE
    fclose(stdin); 
    fclose(stdout); 
    #endif
    
    return 0;
}
