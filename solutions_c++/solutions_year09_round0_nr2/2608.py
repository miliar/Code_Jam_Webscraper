
/* Macros and Headers and Functions {{{ */
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<stack>
#include<queue>
#include<cstdarg>
#include<map>
#include<list>
#include<deque>
#include<cctype>
#include<iterator>
#include<numeric>
#include<complex>
#include<climits>
#include<cstdlib>
#include<cstring>


using namespace std;

#define REP(i,n) for(int i=0; i<n; ++i)
#define REPS(p,s) for(char *p=s;*p;p++)
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define RFOR(i,a,b) for(int i=a;i>=b;--i)

#define EL() cout<<endl;

#define BN begin()
#define ED end()
#define RN rbegin()
#define RD rend()
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second

#define PB push_back
#define PF push_front
#define BP pop_back
#define FP pop_front

#define IT(X) __typeof((X).BN)
#define RIT(X) __typeof((X).RN)
#define REF(X) __typeof(__typeof(X)::reference)

#define FORIT(it,X) for(IT(X) it= (X).BN; it!=(X).ED; ++it)
#define FORITR(it,X) for(RIT(X) it=(X).RN; it!=(X).RD; ++it)

#define VV(X) vector< vector< X > >
#define PIB(X) pair< IT(X), bool >

typedef long long LL;
typedef unsigned long long ULL;
//typedef stringstream ss;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< PII > VPII;

//debugging IO functions start

void IO(int l, ...)
{
	va_list val;
	va_start(val,l);
	int i;
	FOR(i,0,l)
	{
		cout<<va_arg(val,int)<<"  ";
	}
}

void SO(int l, ...)
{
	va_list val;
	va_start(val,l);
	int i;
	FOR(i,0,l)
	{
		cout<<va_arg(val,char*)<<"  ";
	}
}

void AIO(int n,int a[])
{
	REP(i,n)
		cout<<a[i]<<"  ";
	EL();
}

void ASO(int n,string a[])
{
	REP(i,n)
		cout<<a[i]<<"  ";
	EL();
}

/*void GIO(char *f, ...)
{
	va_list val;
	va_start(val,f);
	while(*f!='\0')
	{
		if(*f=='d')    //here we can add more options as we need like for double, or user defined structs
			cout<<va_arg(val,int)<<"  ";
		else if(*f=='s')
			cout<<va_arg(val,char*)<<"  ";
		f++;
	}
}*/

//debugging IO functions end
/* }}} */

bool f[105*105];
int val[105*105],n;
vector<vector<int> > g(105*105);
void dfs(int c,int v)
{
	f[c]=true;
	val[c]=v;
	int l=g[c].size();
	REP(i,l)
		if(f[g[c][i]]==0)
			dfs(g[c][i],v);
	REP(i,n)
		if(i!=c)
			if(find(g[i].BN,g[i].ED,c)!=g[i].ED)
				if(f[i]==0)
					dfs(i,v);
}

int main()
{
	int T,H,W,w,e,s,c,ma[105][105],from,to,gv;
	cin>>T;
	REP(x,T)
	{
		cin>>H>>W;
		REP(i,H)
			REP(j,W)
			{
				cin>>ma[i][j];
//				pa[i][j]=-1;
			}
		n=H*W;
		REP(i,n)
			g[i].clear();
		REP(i,H)
		{
			REP(j,W)
			{
				from=i*W+j;
				n=w=e=s=20000;
				c=ma[i][j];
				if(i!=0)
					n=ma[i-1][j];
				if(i!=H-1)
					s=ma[i+1][j];
				if(j!=0)
					w=ma[i][j-1];
				if(j!=W-1)
					e=ma[i][j+1];
				if(n<=w && n<=e && n<=s && n<c)
				{
					to=(i-1)*W+j;
					g[from].PB(to);
					g[to].PB(from);
				//	g[from][to]=1;
				//	g[to][from]=1;
				}
				else if(w<n && w<=e && w<=s && w<c)
				{
					to=i*W+j-1;
					g[from].PB(to);
					g[to].PB(from);
//					g[from][to]=1;
//					g[to][from]=1;
				}
				else if(e<n && e<w && e<=s && e<c)
				{
					to=i*W+j+1;
					g[from].PB(to);
					g[to].PB(from);
//					g[from][to]=1;
//					g[to][from]=1;
				}
				else if(s<n && s<w && s<e && s<c)
				{
					to=(i+1)*W+j;
					g[from].PB(to);
					g[to].PB(from);
//					g[from][to]=1;
//					g[to][from]=1;
				}
			}
		}
		n=H*W;
/*		REP(i,n)
		{
			REP(j,n)
				cout<<g[i][j]<<" ";
			cout<<endl;
		}
		EL();*/
		gv=0;
		memset(f,0,sizeof(f));
		memset(val,-1,sizeof(val));
		REP(i,n)
		{
			if(f[i]==0)
			{
//				IO(2,i,gv);
//				cout<<i<<" ";
				dfs(i,gv);
				gv++;
			}
		}
//		EL();
		printf("Case #%d:\n",x+1);
//		IO(2,H,W);
//		EL();
		REP(i,H)
		{
			REP(j,W)
			{
				if(j!=0)
					cout<<" ";
				cout<<(char)(val[i*W+j]+'a');
			}
			EL();
		}
//		EL();
	}
	return 0;
}
