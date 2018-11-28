#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <string>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<string> VS;
const double pi=3.1415926535897932384626433832795;
const double eps=1e-8;

#define pb push_back
#define mp make_pair
#define sz size()
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define CLR(a,v) memset((a),(v),sizeof(a))
#define CPY(a,b) memcpy((a),(b),sizeof(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)<(0)?-(a):(a))
#define HAS(x,k) ((x).find(k)!=(x).end())
#define sqr(a) ((a)*(a))
//#pragma comment(linker,"/STACK:200000000")

#define PREV(x) ((x)&((x)-1))
#define NEXT(x) (((x)<<1) - PREV(x))

char ch[1<<20];
string gs(){ scanf("%s",ch); return string(ch); }
string gl(){ gets(ch); return string(ch); }

set<PII> A;
set<PII> B;
int N;

void next()
{
	B.clear();
	for(set<PII>::iterator it=A.begin(); it!=A.end(); ++it)
	{
		PII t1=*it;
		PII t2=*it;
		t1.first--;
		t2.second--;
		if (HAS(A,t1) || HAS(A,t2)) 
			B.insert(*it);
		
		PII t=*it; t.first++;
		t1=t; t1.second--;
		if (HAS(A,t1)) 
			B.insert(t);

		t=*it; t.second++;
		t1=t; t1.first--;
		if (HAS(A,t1)) 
			B.insert(t);
	}
	A=B;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int tc=0; int t; scanf("%d",&t);
	while(t--)
	{
		++tc;
		scanf("%d",&N);
		FOR(i,0,N)
		{
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			FOR(x,x1,x2+1) FOR(y,y1,y2+1)
				A.insert(mp(x,y));
		}
		int r=0;
		while(A.sz)
			next(),++r;
		
		printf("Case #%d: %d\n",tc,r);
		fprintf(stderr,"Case #%d: %d\n",tc,r);
	}
	
	return 0;
}
