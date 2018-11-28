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

#define SIZE 110
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tt;cin>>tt;FR(cas,tt)
	{
		printf("Case #%d:\n",cas+1);
		char a[SIZE][SIZE]={0};
		int n;cin>>n;
		FR(i,n) cin>>a[i];
		int win[SIZE]={0};
		int num[SIZE]={0};
		FR(i,n) FR(j,n) 
			if(a[i][j]=='1')
			{
				win[i]++;
				num[i]++;
			}
			else if(a[i][j]=='0') num[i]++;
	
		double owp[SIZE]={0};
		FR(i,n)
		{
			int cnt=0;
			double sum=0;
			FR(j,n) 
				if(a[j][i]!='.')
				{
					cnt++;
					int t1=win[j];
					int t2=num[j]-1;
					if(a[j][i]=='1') t1--;
					sum+= (double)t1/t2;
				}
				owp[i]=0;
				if(cnt!=0) owp[i]=sum/cnt;
		}
		FR(i,n)
		{
			double RIP=0.25 * (double)win[i]/num[i] + 0.50 * owp[i];
			int cnt=0;
			double sum=0;
			FR(j,n) 
				if(a[i][j]!='.') {sum+=owp[j];cnt++;}
			if(cnt!=0) RIP+= .25*sum/cnt;
			cout<<fixed<<setprecision(12)<<RIP<<endl;
		}

	}

	return 0;
}