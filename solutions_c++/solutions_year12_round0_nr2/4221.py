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
#include <ctime>
#include <fstream>
#include <cstring>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define FOR(i, a, b) for (int i = a; i < b; i++) 
#define REP(i, n) FOR(i,0,n)
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({ll t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define pb push_back 
#define sz size()
#define TRvi(c, it) for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 1000000007
#define flush(x) memset(x,-1,sizeof(x))
#define MAXN 100010

int main()
{
	int t=GI;
	int k=1;
	while(t--)
	{
		cout<<"Case #"<<k++<<": ";
		int n=GI, s=GI, p=GI;
		int a[110];
		REP(i,n) a[i]=GI;
		int ans=0;
		REP(i,n)
		{
			if(a[i]/3>=p) ans++;
			else if(a[i]/3==p-1&&a[i]%3>0) ans++;
			else if(a[i]/3==p-1&&s>0&&a[i]!=0){ ans++;s--;}
			else if(a[i]/3==p-2&&a[i]%3==2&&s>0){ans++;s--;}
		}
		cout<<ans<<endl;
	}
}
