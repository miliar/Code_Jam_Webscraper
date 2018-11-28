#pragma warning (disable:4786)
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
/*---------------------------------------------------------*/
#define INF 123456789
#define SI(A) ((int)(A).size())
#define ALL(A) A.begin(),A.end()
#define CL(A,v) memset(A, v, sizeof(A))
#define FOR(i,a,b) for ( i = (a); i <= (b); ++i )
#define IFOR(i,a,b) for ( i = (a); i >= (b); --i )
#define REP(i,N) for ( i = 0; i < N; ++i )
#define IREP(i,N) for ( i = N - 1; i >= 0; --i )
#define IT(T,A,i) for ( T::iterator i = (A).begin(); i != (A).end(); ++i )
#define BIT(mask,i) ((mask) & (1 << (i)))
/*---------------------------------------------------------*/
int lowbit(int set) { return (set^(set-1))&set; }
int countbit(int set) { return (set==0)?0:(1+countbit(set-lowbit(set))); }
/*---------------------------------------------------------*/
template<class T> void print(vector<T> A,int n=-1){if(n==-1||n>A.size())n=A.size();cout<<"{";for (int i=0;i<n;i++)cout<<A[i]<<" ";cout<<"}"<<endl;}
template<class T> void print(T A[],int n){cout<<"{";for (int i=0;i<n;i++)cout<<A[i]<<" ";cout<<"}"<<endl;}
/*---------------------------------------------------------*/
typedef vector<int> VI;
typedef vector<string> VS;
typedef double LD;

typedef long long LL;
typedef pair<int, int> TP;
typedef unsigned char ui8;
/*---------------------------------------------------------*/
struct tS
{
	int a, b, c;
};

	bool cmp(const tS& a, const tS& b)
	{
		if ( a.a != b.a ) return a.a < b.a;
		return a.b > b.b;
	}

tS S[323];
int n, cC;

int solve()
{
	sort(S, S + n, cmp);
	int res = 12345678;	
	int a, b, c, i;

	//fprintf(stderr, "S: %d\n", n);	REP(i, n) fprintf(stderr, "%d %d %d\n", S[i].a, S[i].b, S[i].c);

	REP(a, cC) REP(b, a + 1) REP(c, b + 1)
	{			
		int f = 0;
		REP(i, n)
			if ( S[i].c == a || S[i].c == b || S[i].c == c && S[i].b >= 10000 )
			{
				f = 1; break;
			}
		if (!f) continue;
				
		vector<int> s;
		REP(i, n)
			if ( S[i].c == a || S[i].c == b || S[i].c == c )
			{
				//fprintf(stderr, "CCC %d %d %d\n", a, b, c);				print(s);
				if ( s.empty() && S[i].a != 1 ) break;
				if ( !s.empty() && S[s.back()].b < S[i].a - 1 ) break;				
				
				while ( s.size() >= 2 && S[s[SI(s) - 2]].b + 1 >= S[i].a && S[s[SI(s) - 1]].b <= S[i].b ) 
					s.pop_back();
				while ( !s.empty() && S[s.back()].a >= S[i].a && S[s.back()].b <= S[i].b )
					s.pop_back();				
				
				if ( s.empty() || S[s.back()].b < S[i].b ) 				
					s.push_back(i);
				//print(s);
			}		
		if ( !s.empty() && S[s.back()].b >= 10000 )
			res = min((int)s.size(), res);
	}
	return res > n ? -1 : res;
}

int main()
{
    int cT, t;
	int i;
	char s[123];
    
    freopen("c:/gcj/b/2.out", "w", stdout);    
    freopen("c:/gcj/b/2.in", "r", stdin);
    scanf("%d", &cT);
	map<string, int> map;
    REP(t, cT)
    {
        printf("Case #%d: ", t + 1);
		scanf("%d\n", &n);
		cC = 0;
		map.clear();
		REP(i, n) 
		{
			scanf("%s %d%d\n", &s, &S[i].a, &S[i].b);
			if ( map.find(s) == map.end() ) map[s] = cC++;
			S[i].c = map[s];			 
		}

        int res = solve();

        if ( res < 0 ) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
        fprintf(stderr, "%d\n", t);
    }
    fclose(stdout);
    return 0;
}
