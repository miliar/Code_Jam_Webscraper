#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <deque>
#include <algorithm>
#include <memory.h>
#include <complex>
#include <ctime>
using namespace std;


typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef vector<pair<int,PII> > VIII;
typedef vector<string> VS;
typedef complex<double> base;
const double pi=3.1415926535897932384626433832795;
const double eps=1e-9;

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
string gs(){scanf("%s",ch); return string(ch);}
string gl(){gets(ch); return string(ch);}
LL gcd(LL a, LL b) {return (!a)?b:gcd(b%a,a);}

int B[128];
int dp[101000];
int N;
LL L;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);


	int t; cin >> t;
	int tn=0; 
	while(t--)
	{
		++tn;
		//printf("Case #%d: ",tn);
		cout << "Case #" << tn << ": ";
		cerr << "Case #" << tn << ": ";
		//fprintf(stderr,"Case #%d: ",tn);
		cin >> L >> N;	
		FOR(i,0,N) cin >> B[i];
		FOR(t,0,101000) dp[t]=1<<30;
		dp[0]=0;
		FOR(i,1,101000)
			FOR(j,0,N) if (i-B[j]>=0)
				dp[i]=MIN(dp[i],dp[i-B[j]]+1);
		LL best=1LL<<60;
		FOR(i,0,N)
		{
			LL X=L;
			LL S=X-100000LL;
			if (S<=0) 
				S=0;
			else
				S/=B[i];

			
			int y=X-(LL)B[i]*S;
			if (dp[y]==1<<30) continue;
			LL d=S+dp[y];
			best=MIN(best,d);
		}
		if (best==1LL<<60)
			cout << "IMPOSSIBLE\n";
		else
			cout << best << endl;
	}
	
	return 0;
}