#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <ctime>
using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it)) 
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define INF 1e8
#define EPS 1e-8
#define MOD 1000000007
#define SQR(a) ((a)*(a))
typedef long long  ll;
typedef unsigned long long  ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);	
	char a[300]={0};
	a[97]='y';
	a[98]='h';
	a[99]='e';
	a[100]='s';
	a[101]='o';
	a[102]='c';
	a[103]='v';
	a[104]='x';
	a[105]='d';
	a[106]='u';
	a[107]='i';
	a[108]='g';
	a[109]='l';
	a[110]='b';
	a[111]='k';
	a[112]='r';
	a[113]='z';
	a[114]='t';
	a[115]='n';
	a[116]='w';
	a[117]='j';
	a[118]='p';
	a[119]='f';
	a[120]='m';
	a[121]='a';
	a[122]='q';
	a[32]=' ';
	int t;cin>>t;cin.get();
	FR(cas,t)
	{
		printf("Case #%d: ",cas+1);
		char s[1000];
		cin.getline(s,1000);
		FR(i,1000) if(s[i]==0) break;
		else s[i]=a[s[i]];
		cout<<s<<endl;
	}
	return 0;
}