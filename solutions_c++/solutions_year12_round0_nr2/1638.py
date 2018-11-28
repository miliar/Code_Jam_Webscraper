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


int score[2][200];
int already[2][200];
int A[200];

int main()
{
	int tc;
	S(tc);
	for (int cas = 1; cas <= tc; cas += 1)
	{
		int n,p,sp;

		S(n);	S(sp);	S(p);

		for (int i = 0; i < n; i += 1)
			S(A[i]);
		
		for (int i = 0; i < n; i += 1)
		{
			if ( A[i] == 0 )		score[0][i] = 0				, score[1][i] = -1;
			else if ( A[i] == 1 )	score[0][i] = 1				, score[1][i] = -1;
			else if ( A[i]%3 == 0 )	score[0][i] = A[i]/3		, score[1][i] = A[i]/3 + 1;
			else if ( A[i]%3 == 1 )	score[0][i] = A[i]/3 + 1	, score[1][i] = A[i]/3 + 1;
			else if ( A[i]%3 == 2 )	score[0][i] = A[i]/3 + 1	, score[1][i] = A[i]/3 + 2;
			cerr << A[i] << "--> " << score[0][i] <<" "<< score[1][i] << endl;
		}
		cerr<<endl;

		for (int i = 0; i < n; i += 1)
		{
			for (int j = 0; j < n; j += 1)
			{
				if ( i<j && score[1][i] < score[1][j] || (score[1][i] == score[1][j] && score[0][i] < score[0][j]) )
					swap( score[0][i] ,score[0][j] ) , swap( score[1][i] , score[1][j] ); 
			}
		}
		
		int cnt = 0;
		int N = sp;
		for (int i = 0; i < n; i += 1)
		{
			if ( score[0][i] >= p )	cnt ++;
			else if ( score[1][i] >= p && sp ) cnt ++ , sp--;
		}
		
		for (int i = 0; i < n; i += 1)
		{
			if (score[1][i] != -1)
				N--;
		}
		
		if (N>0)	cnt = 0;
		
		printf("Case #%d: %d\n",cas , cnt);		
	}
}












