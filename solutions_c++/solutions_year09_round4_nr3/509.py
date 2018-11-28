#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define sz size()
#define pb push_back
#define mp make_pair
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define CLR(a,v) memset((a),(v),sizeof(a))
#define CPY(a,b) memcpy((a),(b),sizeof(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)<(0)?-(a):(a))

int C[128][128];
int N,K;
VI use;
int dp[20][1<<16];

int A[128][128];
char ch[1024];
int bc[1<<16];
int was[1<<16];
PII ms[1<<16];

int main()
{
	bc[0]=0; FOR(i,1,1<<16) bc[i]=bc[i/2]+(i&1);
	FOR(i,0,1<<16) ms[i]=mp(bc[i],i);
	sort(ms,ms+(1<<16));
	freopen("in.txt","r",stdin);
	FILE *f=fopen("out.txt","w");
	//freopen("out.txt","w",stdout);

	int TTT; scanf("%d",&TTT);
	int CASE=0;
	while(TTT--)
	{
		++CASE;
		scanf("%d%d",&N,&K);
		FOR(i,0,N)
			FOR(j,0,K) scanf("%d",&A[i][j]);
		
		CLR(C,0);
		CLR(was,0);
		FOR(i,0,N) FOR(j,i+1,N)
		{
			int ok=0;
			int d=A[i][0]-A[j][0];
			if (d==0) ok=1;
			FOR(t,1,K)
			{
				int nd=A[i][t]-A[j][t];
				if (nd>0 && d<0 || nd<0 && d>0 || nd==0) ok=1;
				d=nd;
			}
			if (ok) C[i][j]=C[j][i]=1;
		}
		use.clear();
		
		//RFOR(mi,(1<<16)-1,1) if (ms[mi].second<(1<<N)) if (!was[ms[mi].second])
		FOR(m,0,1<<N)
		{
			//int m=ms[mi].second;
			int ok=1;
			FOR(a,0,N) if (m&(1<<a)) FOR(b,a+1,N) if (m&(1<<b))
			{
				if (C[a][b]) {ok=0;break;}
			}
			if (ok || bc[m]==1) 
			{
				use.pb(m);
				for(int q=m; q>0; q=(q-1)&m)
					was[q]=1;
			}
		}
		//if (use.sz>500)
		//	cout << "tmp: " << use.sz << endl;

		int t=0;
		CLR(dp,0);
		dp[0][0]=1;
		while(!dp[t][(1<<N)-1])
		{
			FOR(m,0,1<<N) if (dp[t][m])
				FOR(mi,0,use.sz)
					dp[t+1][m|use[mi]]=1;
			++t;
		}
		int r=t;
		printf("Case #%d: %d\n",CASE,r);
		fprintf(f,"Case #%d: %d\n",CASE,r);
	}
	


	return 0;
}