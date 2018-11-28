#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define pb push_back
#define mp make_pair
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define CLR(a,v) memset((a),(v),sizeof(a))
#define CPY(a,b) memcpy((a),(b),sizeof(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)<(0)?-(a):(a))

VI a[64];
int n;

char ch[1024];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int TTT; scanf("%d",&TTT);
	int CASE=0;
	while(TTT--)
	{
		++CASE;
		scanf("%d",&n);
		FOR(i,0,n) a[i]=VI(n,0);
		FOR(i,0,n) 
		{
			scanf("%s",ch);
			FOR(j,0,n) a[i][j]=ch[j]-'0';
		}
		int r=0;
		FOR(i,0,n)
		{
			int use=-1;
			FOR(j,i,n)
			{
				int ok=1;
				FOR(k,i+1,n) if (a[j][k]) ok=0;
				if (ok) {use=j; break;}
			}
			int t=use;
			while(t!=i)
			{
				swap(a[t],a[t-1]);
				--t;
				++r;
			}
		}
		printf("Case #%d: %d\n",CASE,r);
	}
	


	return 0;
}