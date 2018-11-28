#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
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
const double pi=3.1415926535897932384626433832795;

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
#pragma comment(linker,"/STACK:200000000");

#define PREV(x) ((x)&((x)-1))
#define NEXT(x) (((x)<<1) - PREV(x))

char ch[1<<20];
string gs(){scanf("%s",ch); return string(ch);}




int main()
{
	freopen("in.txt","r",stdin);

	//freopen("A-small.in","r",stdin);
	//freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
		
	int k;
	int n;
	int T; scanf("%d",&T);
	int tn=0;
	while(T--)
	{
		++tn;
		printf("Case #%d: ",tn);
		scanf("%d%d",&n,&k);
		k%=(1<<n);
		if (k==(1<<n)-1) printf("ON\n");
		else printf("OFF\n");
	}
	
	return 0;
}
