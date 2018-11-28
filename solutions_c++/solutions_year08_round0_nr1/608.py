//#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include <memory.h>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef double DD;
typedef long double LD;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define VAR(V,init) __typeof(init) V=(init)
#define FUP(I,A,B) for(int I=(A);I<=(B);I++)
#define FDN(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define FALL(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define ALL(X) (X).begin(),(X).end()
#define CLE(a,b) memset(a,b,sizeof(a))
#define MINN(a,b) ((a)>(b)?(b):(a))
#define MAXX(a,b) ((a)<(b)?(b):(a))
#define PB push_back
#define PF push_front
#define CB pop_back
#define CF pop_front
#define MP make_pair
#define SZ(X) ((int)(X.size()))
#define deb(A) A
/////////////////

#define MAX_S 100
#define MAX_Q 1000
#define MAX_L 102

struct engine
{
	char name[MAX_L];
};

bool operator == (const engine & A, const engine & B)
{
	if(strlen(A.name) != strlen(B.name))
		return false;
	REP(l,(int)strlen(A.name))
		if(A.name[l] != B.name[l])
			return false;
	return true;
}

engine SE[MAX_S],QE;

int n, s, q, moves, found, number;
bool exist[MAX_S];

int main()
{
	scanf("%d",&n);
	REP(i,n)
	{
		scanf("%d\n",&s);
		REP(j,s)
			gets(SE[j].name);
		scanf("%d\n",&q);
		moves = 0;
		found = 0;
		REP(j,s)
			exist[j] = false;
		REP(j,q)
		{
			gets(QE.name);
			REP(k,s)
				if(QE == SE[k])
				{
					number = k;
					break;
				}
			if(((found + 1) == s) && (!exist[number]))
			{
				moves++;
				REP(k,s)
					exist[k] = false;
				exist[number] = true;
				found = 1;
			}
			else
				if(!exist[number])
				{
					found++;
					exist[number] = true;
				}
		}
		printf("Case #%d: %d\n",i + 1, moves);
	}
	return 0;
}
