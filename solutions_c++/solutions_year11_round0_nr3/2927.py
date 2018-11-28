/*
** In the name of God **
*/
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
#include <stdio.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it))
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define EPS 1e-8
#define MOD 1000000007
#define INF 100000000
#define SQR(a) ((a)*(a))
#define pb push_back
typedef long long ll;
typedef unsigned long long ull;
typedef long double lld;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
#define ORANGE true
#define BLUE false
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tnum;
	scanf("%d",&tnum);
	int n;
	int a[1001];
	FOR(q,1,tnum+1)
	{
		scanf("%d",&n);
		int sum=0;
		ull ans=0;
		FR(i,n){ scanf("%d",&a[i]); sum^=a[i];ans+=a[i];}
		printf("Case #%d: ",q);
		if(sum!=0)printf("NO\n");
		else
		{
			int mini=a[0];
			FOR(i,1,n) if(a[i]<mini)mini=a[i];
			cout<<ans-mini<<endl;
		}
	}
}