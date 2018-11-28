#include<iostream>
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
typedef long long ll;
typedef unsigned long long ull;
typedef double dd;
typedef long double ld;
typedef vector <int > VI;
typedef vector < VI > VVI;
typedef vector < ll > VLL;
typedef vector < dd > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define VAR(V,init) __typeof(init) V=(init)
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define FOREACH(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
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
#define INF 1000000000
int COND = 100;
#define DB(x) ({if(COND){COND--; cerr << __LINE__ << " : " << #x << ": " << x << endl; };})
#define deb(A ) A
/////////////////


#define MAX_N 300
#define MAX_M 10000

int test,x[MAX_N],y[MAX_N],res,num,n;
vector<int> p[MAX_N];
vector< pair<int,int> > v;
string c[MAX_N];
map<string,int> has;

int main()
{
	scanf("%d",&test);
	REP(ttt,test)
	{
		scanf("%d",&n);
		REP(i,n)
		{
			cin>>c[i];
			scanf("%d%d",&x[i],&y[i]);
			x[i]--; y[i]--;
		}
		num=0;
		has.clear();
		res=n+1;
		REP(i,n)
			p[i].clear();
		REP(i,n)
		{
			if(has.find(c[i])==has.end())
				has[c[i]]=num++;
			p[has[c[i]]].PB(i);
		}
		REP(i,1<<n)
		{
			v.clear();
			has.clear();
			int dif=0;
			REP(j,n)
				if((i&(1<<j))==(1<<j))
				{
					if(has.find(c[j])==has.end())
						dif++;
					has[c[j]]=0;
					v.PB(make_pair(x[j],y[j]));
				}
			if(v.empty() || dif>3)
				continue;
			sort(v.begin(),v.end());
			//REP(l,SZ(v)){DB(l); DB(v[l].FI); DB(v[l].SE);}
			int md=0;
			int pp=0;
			bool good=true;
			REP(l,SZ(v))
			{
				int r=l;
				if(md<v[l].FI)
				{
					good=false;
					break;
				}
				while(r+1<SZ(v) && v[l+1].FI==v[r].FI)
					l++;
				if(v[l].FI==md || v[l].SE>=md)
					pp++;
				md=MAXX(md,v[l].SE+1);
			}
			good&=(md>=MAX_M);
			//DB(good);
			if(good)
				res=MINN(res,pp);
		}
		printf("Case #%d: ",ttt+1);
		if(res==(n+1))
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",res);
	}
	return 0;
}
