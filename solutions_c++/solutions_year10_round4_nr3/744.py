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
	#define READ freopen("C-small.in","r",stdin)
	#define WRITE freopen("C-small.out","w",stdout)
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

#define MAX_C 100

int minR,maxR;
int minC,maxC;
bool isB[MAX_C+2][MAX_C+2];

bool allDied()
{
	for(int i=minR;i<=maxR;i++) for(int j=minC;j<=maxC;j++) if(isB[i][j]) return false;
	return true;
}

void output()
{
	for(int i=minR;i<=maxR;i++)
	{
		for(int j=minC;j<=maxC;j++) cout<<isB[i][j];
		cout<<endl;
	}
	cout<<endl;
}


void go()
{
	bool isBB[MAX_C+2][MAX_C+2];
	memset(isBB,0x0,sizeof(isBB));
	for(int i=minR;i<=maxR;i++) for(int j=minC;j<=maxC;j++)
	{
		if(!isB[i][j] && isB[i-1][j] && isB[i][j-1]) isBB[i][j]=true;
		else if(isB[i][j] && !isB[i-1][j] && !isB[i][j-1]) isBB[i][j]=false;
		else isBB[i][j]=isB[i][j];
	}
	memcpy(isB,isBB,sizeof(isB));
}

void solve(const int &caseID)
{
	minR=I_INF;
	maxR=-I_INF;
	minC=I_INF;
	maxC=-I_INF;

	memset(isB,0x0,sizeof(isB));
	int R;
	cin>>R;
	while(R--)
	{
		int x1,y1,x2,y2;
		cin>>y1>>x1>>y2>>x2;

		if(x1>x2) swap(x1,x2);
		if(y1>y2) swap(y1,y2);

		checkMin(minR,x1);checkMin(minR,x2);
		checkMax(maxR,x1);checkMax(maxR,x2);
		checkMin(minC,y1);checkMin(minC,y2);
		checkMax(maxC,y1);checkMax(maxC,y2);

		for(int i=x1;i<=x2;i++) for(int j=y1;j<=y2;j++) isB[i][j]=true;
	}

	//output();

	int ans=0;
	while(!allDied())
	{
		go();
		//output();
		ans++;
	}
	printf("Case #%d: %d\n",caseID,ans);
}

int main()
{
	//READ;
	//WRITE;

	freopen("C-small.in","r",stdin);freopen("C-small.out","w",stdout);
	//freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);

	int T;
	scanf("%d",&T);
	for(int caseID=1;caseID<=T;caseID++) solve(caseID);
	return 0;
}
