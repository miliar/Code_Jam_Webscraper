#include<iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<sstream>
#include<map>
#include<utility>

#define S(n) scanf("%d",&n)


#define REP(i,n) for(i=0; i<n; i++)
#define REPA(i,a,n) for(i=a; i<n; i++)
#define SOR(x) sort(x.begin(), x.end())
#define REV(x) reverse(x.begin(), x.end())
#define FOREACH(iter,var) for(__typeof((var).begin()) iter=(var).begin(); iter!=(var).end(); iter++)
#define PB push_back
#define VI vector<int>
#define SZ size()
#define VS vector<string>

#define MP make_pair
#define VVI vector< vector<int> >
#define INF 2000000000

#define CLR(var,val) memset(var,val,sizeof((var)))
#define S(n) scanf("%d",&n)
#define LL unsigned long long
#define LD long double
#define triple pair<int, pair<int,int> >
#define OFF 0
#define MAX(a,b) (a>b?a:b)

using namespace std;


int main()
{
	int t; S(t);
	int c = 0;
	while(t--)
	{
		c++;
		int ans = 0;
		int n; S(n);
		VI a; VI b;
		
		int i;
		REP(i,n) { int ta, tb; S(ta); S(tb); a.PB(ta); b.PB(tb); }
		
		for(i = 0; i < n; i++)
			for(int j = i + 1; j < n; j++)
				if(a[i] > a[j]) { swap(a[i],a[j]); swap(b[i],b[j]); }
		
		for(i = 0; i < n; i++)
			for(int j = i + 1; j < n; j++)
				if(b[i] > b[j] && a[j] > a[i]) ans++;
		cout << "Case #" << c << ": " << ans << endl;
	}
	return 0;
}
