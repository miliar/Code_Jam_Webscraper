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

inline int cast(char c)
{
	if(c=='O') return 0;
	else return 1;
}

int main()
{
    
    #ifndef ONLINE_JUDGE 
    freopen("A-large.in","r",stdin); 
    freopen("aout.txt","w",stdout); 
    #endif

    int case_n, mov;

    scanf("%d", &case_n);    
    FOR(case_i, 1, case_n)
    {
		int n, p, tmp, res=0, prev[2];
		char c, lastc;
		mov=0;
		prev[0]=prev[1]=1;
		scanf("%d", &n);
		FOR(i,1,n)
		{
			scanf(" %c %d", &c, &p);
			if(i==1) lastc=c;
			if(lastc==c) 
			{
				tmp=abs(p-prev[cast(c)])+1;
				res+=tmp;
				mov+=tmp;
			}
			else
			{
				tmp=max(0, abs(p-prev[cast(c)])-res)+1;
				res=tmp;
				mov+=tmp;
			}
			prev[cast(c)]=p;
			lastc=c;
		}
		
        printf("Case #%d: %d\n", case_i, mov);
    }

    #ifndef ONLINE_JUDGE 
    fclose(stdin); 
    fclose(stdout); 
    #endif
    
    return 0;
}
