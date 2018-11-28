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
#define FI first
#define SE second
#define SZ(X) ((int)(X.size()))
#define deb(A) //A
/////////////////

#define MAX_T 200

struct trip
{
	int beginTime, endTime;
	char from;
	trip(){}
	trip(int bt, int et, char w)
	{
		beginTime = bt;
		endTime = et;
		from = w;
	}
};

bool cmp (const trip & AA, const trip & BB)
{
	if(AA.beginTime == BB.beginTime)
		return AA.endTime < BB.endTime;
	return AA.beginTime < BB.beginTime;
}

trip T[MAX_T];

multiset<int> A,B;

int n, na, nb, bt, et, t, it, trainsA, trainsB;

int readTime()
{
	char t[5];
	do
	{
		t[0] = getchar();
	}
	while((t[0] == ' ') || (t[0] == '\n'));
	FUP(x,1,4)
		t[x] = getchar();
	deb(REP(x,5)printf("%c",t[x]);printf("\n"););
	return ((t[0] - '0') * 10 + t[1] - '0') * 60 + (t[3] - '0') * 10 + t[4] - '0';	
}

int main()
{
	scanf("%d",&n);
	REP(i,n)
	{
		scanf("%d%d%d",&t,&na,&nb);
		it = 0;
		REP(j,na)
		{
			bt = readTime();
			et = readTime();
			T[it++] = trip(bt, et + t, 'A');
		}
		REP(j,nb)
		{
			bt = readTime();
			et = readTime();
			T[it++] = trip(bt, et + t, 'B');
		}
		sort(T, T + it, cmp);
		deb(REP(j,it)printf("j = %d (%d, %d) %c\n", j, T[j].beginTime, T[j].endTime, T[j].from););
		trainsA = 0; 
		A.clear();
		trainsB = 0;
		B.clear();
		REP(j,it)
		{
			if(T[j].from == 'A')
			{
				if((A.empty()) || ((*A.begin()) > T[j].beginTime))
				{
					trainsA++;
					A.insert(T[j].beginTime);
				}
				B.insert(T[j].endTime);
				A.erase(A.begin());
			}

			if(T[j].from == 'B')
			{
				if((B.empty()) || ((*B.begin()) > T[j].beginTime))
				{
					trainsB++;
					B.insert(T[j].beginTime);
				}
				A.insert(T[j].endTime);
				B.erase(B.begin());
			}
		}
		printf("Case #%d: %d %d\n", i + 1, trainsA, trainsB);
	}
	return 0;
}
