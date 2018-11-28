#include<map>
#include<set>
#include<list>
#include<cmath>
#include<ctime>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<cctype>
#include<cstdio>
#include<string>
#include<vector>
#include<cstdlib>
#include<cstring>
#include<iomanip>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<functional>

using namespace std;

// Begin Template By yaymao

#ifndef ONLINE_JUDGE
	#define READ freopen("B-large.in","r",stdin)
	#define WRITE freopen("B-large.out","w",stdout)
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

#define X first
#define Y second
#define MII map<int,int>
#define MSI map<string,int>
#define PII pair<int,int>
#define PB(x) push_back(x)
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
bool hasNext(){char c;if(scanf(" %c",&c)==EOF) return false;ungetc(c,stdin);return true;}

int dx[]={ 0, 0,-1, 1,-1, 1,-1, 1};
int dy[]={-1, 1, 0, 0,-1,-1, 1, 1};
string dir[]={"L","R","U","D","LU","LD","RU","RD"};

int twoPower[32]={0x1,0x2,0x4,0x8,0x10,0x20,0x40,0x80,0x100,0x200,0x400,0x800,0x1000,0x2000,0x4000,0x8000,0x10000,0x20000,0x40000,0x80000,0x100000,0x200000,0x400000,0x800000,0x1000000,0x2000000,0x4000000,0x8000000,0x10000000,0x20000000,0x40000000,0x80000000};
int tenPower[10]={0x1,0xA,0x64,0x3E8,0x2710,0x186A0,0xF4240,0x989680,0x5F5E100,0x3B9ACA00};

#define range(i,l,r) for(int i=(l);i<(int)(r);++i)
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define all(c) (c).begin(),(c).end()

// End Template By yaymao

const int MAX_C=26;

char combine[MAX_C][MAX_C];
bool opposed[MAX_C][MAX_C];

void output(const vector<char> &result)
{
	putchar('[');
	rep(i,SIZE(result))
	{
		putchar(result[i]);
		if(i+1<SIZE(result))
			printf(", ");
	}
	putchar(']');
	putchar('\n');
}

void deal(vector<char> &result)
{
	//output(result);

	int l=SIZE(result);
	if(l>1 && combine[result[l-2]-'A'][result[l-1]-'A']!=-1)
	{
		char c=combine[result[l-2]-'A'][result[l-1]-'A']+'A';
		result.pop_back();
		result.pop_back();
		result.PB(c);
		return;
	}
	rep(i,l-1)
		if(opposed[result[i]-'A'][result[l-1]-'A'])
		{
			result.clear();
			return;
		}
}

void run(const int &caseID)
{
	memset(combine,0xFF,sizeof(combine));
	memset(opposed,false,sizeof(opposed));

	int C;
	cin>>C;
	while(C--)
	{
		char a,b,c;
		scanf(" %c%c%c",&a,&b,&c);
		combine[a-'A'][b-'A']=c-'A';
		combine[b-'A'][a-'A']=c-'A';
	}

	int D;
	cin>>D;
	while(D--)
	{
		char a,b;
		scanf(" %c%c",&a,&b);
		opposed[a-'A'][b-'A']=true;
		opposed[b-'A'][a-'A']=true;
	}

	vector<char> result;
	result.clear();

	int n;
	cin>>n;
	rep(i,n)
	{
		char c;
		cin>>c;
		result.PB(c);
		deal(result);
	}
	
	printf("Case #%d: ",caseID);output(result);
}

int main(int argc, char *argv[])
{
	READ;
	WRITE;

	int caseT;
	scanf("%d",&caseT);
	for(int caseID=1;caseID<=caseT;++caseID)
		run(caseID);

	return (EXIT_SUCCESS);
}
