#include<iostream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<string>
#include<algorithm>
#include<functional>
#include<iomanip>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<cassert>
using namespace std;


#define REP(i,n)		for(int i=0;i<(n);++i)
#define FOR(i,a,b)		for(int i=(a);i<=(b);++i)
#define FOREACH(i,c)	for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define ALL(x)			(x).begin(),(x).end()
//#define S(n)			scanf("%d",&n)
#define SS(a)			scanf("%s",a)

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UINT;

/*======================================IO OPTIMISED FUNCTIONS===================================*/
int sign;
int ch;
inline void S( int &x )
{
			x=0;
			while((ch<'0' || ch>'9') && ch!='-' && ch!=EOF)	ch=getchar_unlocked();
			if (ch=='-')
				sign=-1 , ch=getchar_unlocked();
			else
				sign=1;
			
			do
				x=(x<<3)+(x<<1)+ch-'0';
			while((ch=getchar_unlocked())>='0' && ch<='9');
			x*=sign;
}
/*===============================================================================================*/




int main()
{
	int tc;
	S(tc);
	for (int cas = 0; cas < tc; cas += 1)
	{
		int A,B;
		S(A);  S(B);
		
		int cnt = 0;
		for (int i = A; i <= B; i += 1)
		{
			map<int,int> M;
			int pwr = 1;
			int x = i;
			
			int len = 0;
			
			while(x)
				x/=10 , pwr *= 10 , len++;
			
			pwr/=10;
			
			x = i;
			for (int j = 0; j < len-1; j += 1)
			{
				x = (x%10) * pwr + (x/10);
				if (x>=A && x<=B && x>i && x/pwr && M[x]==0)
					cnt ++ , M[x]=1;
			}			
		}
		printf("Case #%d: %d\n",cas+1 , cnt);
	}
}












