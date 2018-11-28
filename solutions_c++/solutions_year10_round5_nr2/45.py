#include <stdio.h>
#include <time.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#pragma comment(linker, "/STACK:16777216")
using namespace std;

#define bit(n) (1<<(n))
#define inf 1000000000
#define eps 1e-9
#define PI 3.1415926535897932385
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) a.begin(),a.end()
#define fill(ar,val) memset(ar,val,sizeof ar)
#define MIN(a,b) if(a>(b)) a=(b)
#define MAX(a,b) if(a<(b)) a=(b)
#define sqr(x) ((x)*(x))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef __int64 LL;

clock_t start=clock();

#define N 101010
set<pair<LL,int> > st;
LL t[N];

void relax(int i,int tt)
{
	set<pair<LL,int> >::iterator it=st.find(mp(t[i],i));
	if(it!=st.end() && t[i]>tt)
	{
		st.erase(it);
		t[i]=tt;
		st.insert(mp(t[i],i));
	}
}

int main()
{
	freopen("B2.in","r",stdin);
	freopen("B2.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d: ",++tst);
		fprintf(stderr,"Case #%d:\n",tst);
		LL L;
		int n,i;
		scanf("%I64d%d",&L,&n);
		int b[111];
		for(i=0;i<n;i++) scanf("%d",&b[i]);
		sort(b,b+n);
		reverse(b,b+n);
		int B=b[0];
		st.cl;
		LL INF=2*LL(inf)*inf;
		for(i=0;i<B;i++)
		{
			t[i]=INF;
			st.insert(mp(t[i],i));
		}
		relax(0,0);
		int r=L%B;
		while(st.sz)
		{
			int u=st.begin()->second;
			if(u==r || t[u]==INF) break;
			st.erase(st.begin());
			int T=t[u];
			for(i=1;i<n;i++)
				relax((u+b[i])%B,T+B-b[i]);
		}
		if(t[r]==INF) puts("IMPOSSIBLE"); else printf("%I64d\n",(t[r]+L)/B);
	}
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
	return 0;
}
