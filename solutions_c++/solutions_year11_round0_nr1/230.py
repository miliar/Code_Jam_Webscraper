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
	#define READ freopen("A-large.in","r",stdin)
	#define WRITE freopen("A-large.out","w",stdout)
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

// End Template By yaymao

const int MAX_N=100;

int n;
char op[MAX_N+1];
int button[MAX_N+1];
vector<int> O,B;

void run(const int &caseID)
{
	cin>>n;

	O.clear();
	B.clear();

	rep(i,n)
	{
		scanf(" %c %d",&op[i],&button[i]);
		if(op[i]=='O')
			O.PB(button[i]);
		else if(op[i]=='B')
			B.PB(button[i]);
	}

	int oPos=1,bPos=1;
	int oI=0,bI=0;

	int now=0;
	rep(i,n)
	{
		if(op[i]=='O')
		{
			// move
			while(oPos!=O[oI])
			{
				if(O[oI]<oPos)
					--oPos;
				else
					++oPos;

				if(bI<SIZE(B) && bPos!=B[bI])
				{
					if(B[bI]<bPos)
						--bPos;
					else
						++bPos;
				}

				++now;
			}
			// push
			++oI;

			if(bI<SIZE(B) && bPos!=B[bI])
			{
				if(B[bI]<bPos)
					--bPos;
				else
					++bPos;
			}

			++now;
		}
		else if(op[i]=='B')
		{
			// move
			while(bPos!=B[bI])
			{
				if(B[bI]<bPos)
					--bPos;
				else
					++bPos;

				if(oI<SIZE(O) && oPos!=O[oI])
				{
					if(O[oI]<oPos)
						--oPos;
					else
						++oPos;
				}

				++now;
			}
			// push
			++bI;

			if(oI<SIZE(O) && oPos!=O[oI])
			{
				if(O[oI]<oPos)
					--oPos;
				else
					++oPos;
			}

			++now;
		}
	}

	printf("Case #%d: %d\n",caseID,now);
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
