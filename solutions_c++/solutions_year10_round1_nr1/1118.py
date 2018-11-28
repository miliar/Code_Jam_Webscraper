#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include<climits>
using namespace std;
#define SZ(a) int((a).size())
#define PB push_back
#define MP make_pair
#define ALL(c) (c).begin(),(c).end()
#define TR(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define PRESENT(c,x) ((c).find(x) != (c).end())
#define FOR(i,a,b) for(int i=(int)a;i<(int)b;i++)
#define REV(i,a,b) for(int i=(int)a;i>(int)b;i--)
#define REP(i,n) for(int i=0;i<(int)n;i++)
#define SETBIT(a,b) a|=(1<<b)
#define UNSETBIT(a,b) a&=~(1<<b)
#define GETBIT(a,b) a&(1<<b)
#define FILL(a,b) memset(a,b,sizeof(a))
#define NBITS(a) __builtin_popcount(a)
#define INF 1000000000
#define EPS 1e-9
typedef long long LL;
typedef pair<int,int> PII;
vector<int> VI;
vector<vector<int> > VVI;
vector<string> VS;
////////// ACUTAL CODE STARTS HERE /////////
char A[55][55],B[55][55];
int N,K;
int dpr[55][55][5];
int dpb[55][55][5];
void rotate()
{
	char t[55][55];
	for(int i=1;i<=N;i++)
	{
		for(int j=1;j<=N;j++)
		{
			t[i][j]=B[N-j+1][i];
		}
	}
	REP(i,N) REP(j,N) B[i+1][j+1]=t[i+1][j+1];
}
string find()
{
	//rotating
	vector<string> col(N+1);
	for(int i=N;i>=1;i--)
	{
		for(int j=N;j>=1;j--)
		{
			if(A[i][j]!='.')
				col[i].PB(A[i][j]);
		}
	}
	//new game
	REP(i,50) REP(j,50) B[i][j]='.';
	for(int i=1;i<=N;i++)
	{
		for(int j=N,k=0;k<col[i].size();j--,k++)
			B[i][j]=col[i][k];
	}
	//REP(i,N){REP(j,N) cout<<B[i+1][j+1];cout<<endl;}
	rotate();
	//REP(i,N){REP(j,N) cout<<B[i+1][j+1];cout<<endl;}
	FILL(dpr,0);
	FILL(dpb,0);
	
	bool ok1,ok2;
	ok1=ok2=false;
	
	REP(i,N) REP(j,N) if(B[i+1][j+1]=='B') REP(k,4) dpb[i+1][j+1][k+1]=1;
	REP(i,N) REP(j,N) if(B[i+1][j+1]=='R') REP(k,4) dpr[i+1][j+1][k+1]=1;
	
	
	//BLUE
	
	//up
	for(int i=2;i<=N;i++)
	{
		for(int j=1;j<=N;j++)
		{
			if(B[i][j]==B[i-1][j] && B[i][j]=='B')
				dpb[i][j][1]=dpb[i-1][j][1]+1;
		}
	}
	
	//down
	for(int i=1;i<=N;i++)
	{
		for(int j=2;j<=N;j++)
		{
			if(B[i][j]==B[i][j-1] && B[i][j]=='B')
				dpb[i][j][2]=dpb[i][j-1][2]+1;
		}
	}
	//diagonal left up
	for(int i=2;i<=N;i++)
	{
		for(int j=2;j<=N;j++)
		{
			if(B[i][j]==B[i-1][j-1] && B[i][j]=='B')
				dpb[i][j][3]=dpb[i-1][j-1][3]+1;
		}
	}
	//diagonal right up
	for(int i=2;i<=N;i++)
	{
		for(int j=N-1;j>=1;j--)
		{
			if(B[i][j]==B[i-1][j+1] && B[i][j]=='B')
				dpb[i][j][4]=dpb[i-1][j+1][4]+1;
		}
	}
	
	
	//RED
	
	//up
	for(int i=2;i<=N;i++)
	{
		for(int j=1;j<=N;j++)
		{
			if(B[i][j]==B[i-1][j] && B[i][j]=='R')
				dpr[i][j][1]=dpr[i-1][j][1]+1;
		}
	}
	
	//down
	for(int i=1;i<=N;i++)
	{
		for(int j=2;j<=N;j++)
		{
			if(B[i][j]==B[i][j-1] && B[i][j]=='R')
				dpr[i][j][2]=dpr[i][j-1][2]+1;
		}
	}
	//diagonal left up
	for(int i=2;i<=N;i++)
	{
		for(int j=2;j<=N;j++)
		{
			if(B[i][j]==B[i-1][j-1] && B[i][j]=='R')
				dpr[i][j][3]=dpr[i-1][j-1][3]+1;
		}
	}
	//diagonal right up
	for(int i=2;i<=N;i++)
	{
		for(int j=N-1;j>=1;j--)
		{
			if(B[i][j]==B[i-1][j+1] && B[i][j]=='R')
				dpr[i][j][4]=dpr[i-1][j+1][4]+1;
		}
	}
	
	REP(i,N) REP(j,N) REP(k,4) if(dpb[i+1][j+1][k+1]>=K) ok1=true;
	REP(i,N) REP(j,N) REP(k,4) if(dpr[i+1][j+1][k+1]>=K) ok2=true;
	
	if(ok1&&ok2) return "Both";
	if(ok1) return "Blue";
	if(ok2) return "Red";
	if(!ok1&&!ok2) return "Neither";
	return "I will qualify to the next round! :)";
}


int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("Aout.txt","w",stdout);
	int T;
	string s;
	cin>>T;
	REP(tests,T)
	{
		cin>>N>>K;
		REP(i,N)
		{
			cin>>s;
			//cout<<s<<endl;
			REP(j,N) A[i+1][j+1]=s[j];
		}
		cout<<"Case #"<<tests+1<<": "<<find()<<endl;
	}
 	return 0;
}
