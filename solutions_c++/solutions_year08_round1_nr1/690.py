#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <list>
#include <stack>
#include <numeric>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <cstdio>
using namespace std;
#define debug(a) cout << #a
#define FO(it,a) for(__typeof(a)::iterator it=a.begin();it!=a.end();++it)
#define FZ(i,n) for(int i=0;i<n;++i)
#define FL(i,s,e) for(int i=s;i<e;++i)
#define CL(s,t) memset(s,t,sizeof(s))
#define sz size()
#define pb push_back
#define B begin()
#define E end()
#define all(a) a.B,a.E 
#define GI ({int t;scanf("%d\n",&t);t;})
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vector<int> > vvi;

int main()
{
	int tt = GI;
	FZ(t,tt)
	{
		int n = GI,mn = INT_MAX,tot;
		vector<int> a,b;
		FZ(i,n) a.pb(GI);
		FZ(i,n) b.pb(GI);
		sort(all(a));
		sort(all(b));
		do{
			tot = 0;
			FZ(i,n) tot += a[i] * b[i];
			mn <?= tot;
	
		}while(next_permutation(all(a)));	
		cout <<"Case #"<<t+1<<": "<< mn << endl;

	}
	return 0;
}
