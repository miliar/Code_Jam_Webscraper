#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <string>
#include <cstring>
#include <cctype>
#include <assert.h>

using namespace std;
typedef long long ll;

const double PI=acos(-1.0);
const double eps=1e-11;

#define dump(x) cerr<<#x<<" = "<<(x)<<endl;
#define foreach(c,itr) for (__typeof( (c).begin() ) itr=(c).begin();itr!=(c).end() ;itr++ )


int countbit(int n) {return (n==0)?0:1+countbit(n&(n-1));}
int lowbit(int n) {return n&(n^(n-1));}
string toString(ll v) { ostringstream sout;sout<<v;return sout.str();}
string toString(int v) { ostringstream sout;sout<<v;return sout.str();}
int Rand16(){return rand();}
int Rand32(){return rand()*rand();}
double DRand(){return (double)rand()/RAND_MAX;}
int RandRange(int f,int r){return f+(int)(DRand()*(r-f)+0.5);}

#define two(i) (1<<(i))




int t,cas;
int cost[11][1<<11];
int need[1<<11];

int main()
{
	int i,j,k;
	int p;

	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);

	scanf("%d",&t);
	cas=0;
	while (t--)
	{
		cas++;
		scanf("%d",&p);
		for (i=0;i<two(p);i++)
		{
			scanf("%d",&need[i]);
			need[i]=p-need[i];
		}

		for (i=1;i<=p;i++)
		{
			for (j=0;j<two(p-i);j++)
			{
				scanf("%d",&cost[i][j]);
			}
		}

		int ans=0;
		for (i=p;i>0;i--)
			for (j=0;j<two(p-i);j++)
			{
				for (k=j*two(i);k<j*two(i)+two(i);k++)				
						if (need[k]>0)
							break;
				if (k<j*two(i)+two(i))
				{
					//printf("i=%d,j=%d\n",i,j);
					ans++;
					for (k=j*two(i);k<j*two(i)+two(i);k++)	
							need[k]--;
				}					
			}
					

		printf("Case #%d: ",cas);
		printf("%d\n",ans);
	}
	return 0;
}
