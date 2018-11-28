#include<map>
#include<set>
#include<cmath>
#include<ctime>
#include<queue>
#include<cstdio>
#include<vector>
#include<cstring>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

// Begin Template By yaymao

#ifndef ONLINE_JUDGE
	#define READ freopen("B-small.in","r",stdin)
	#define WRITE freopen("B-small.out","w",stdout)
#else
	#define READ
	#define WRITE
#endif

#ifdef _MSC_VER
	#define LL __int64
	#define ULL unsigned __int64
#else
	#define LL long long
	#define ULL unsigned long long
#endif

#define EPS 1E-9
#define D_INF 1E99
#define I_INF 0x7FFFFFFF
#define L_INF 0x7FFFFFFFFFFFFFFFLL

#define SIZE(x) ((int)x.size())
#define LENGTH(x) ((int)x.length())

#define PB(x) push_back(x)

#define X first
#define Y second
#define IMAP map<int,int>
#define SIMAP map<string,int>
#define IPAIR pair<int,int>
#define SIPAIR pair<string,int>
#define MP(x,y) make_pair(x,y)

#define TWO(x)			(1<<(x))
#define TWOL(x)			(1LL<<(x))
#define LOWER_BIT(x)	((x)&(-(x)))
#define CONTAIN(s,x)	(((s)&TWO(x))!=0)
#define CONTAINL(s,x)	(((s)&TWOL(x))!=0)

template<class T>inline void checkMax(T &a,const T &b){if(a<b) a=b;}
template<class T>inline void checkMin(T &a,const T &b){if(b<a) a=b;}
template<class T>inline string toString(const T &n){ostringstream out;out<<n;out.flush();return out.str();}
template<class T>inline T toValue(const string &s){T x;istringstream in(s);in>>x;return x;}
bool havaNextTestData(){char c;if(scanf(" %c",&c)==EOF) return false;ungetc(c,stdin);return true;}

int dx[]={ 0, 0,-1, 1,-1, 1,-1, 1};
int dy[]={-1, 1, 0, 0,-1,-1, 1, 1};
string dir[]={"L","R","U","D","LU","LD","RU","RD"};

int twoPower[]={0x1,0x2,0x4,0x8,0x10,0x20,0x40,0x80,0x100,0x200,0x400,0x800,0x1000,0x2000,0x4000,0x8000,0x10000,0x20000,0x40000,0x80000,0x100000,0x200000,0x400000,0x800000,0x1000000,0x2000000,0x4000000,0x8000000,0x10000000,0x20000000,0x40000000,0x80000000};
int tenPower[10]={0x1,0xA,0x64,0x3E8,0x2710,0x186A0,0xF4240,0x989680,0x5F5E100,0x3B9ACA00};

// End Template By yaymao

#define MAX_P 10
#define MAX_N 1024

int p;
int n;

int M[MAX_N+1];

int C[MAX_P+1][MAX_N+1];


void solve(const int &caseID)
{
	cin>>p;
	n=TWO(p);
	for(int i=0;i<=n;i++) cin>>M[i];
	for(int i=p;i>=1;i--)
	{
		for(int j=0;j<TWO(i);j++) cin>>C[i][j];
	}

	int ans=0;
	for(int i=p;i>0;i--) for(int j=0;j<TWO(p-i);j++)
	{
		int k;
		for(k=j*TWO(i);k<j*TWO(i)+TWO(i);k++) if(p>M[k]) break;
		if(k<j*TWO(i)+TWO(i))
		{
			ans++;
			for(k=j*TWO(i);k<j*TWO(i)+TWO(i);k++) M[k]++;
		}
	}

	printf("Case #%d: %d\n",caseID,ans);
}

int main()
{
	//READ;
	//WRITE;

	freopen("B-small.in","r",stdin);freopen("B-small.out","w",stdout);
	//freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);

	int C;
	scanf("%d",&C);
	for(int caseID=1;caseID<=C;caseID++) solve(caseID);
	return 0;
}
