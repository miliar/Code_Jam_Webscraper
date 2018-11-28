//GCC 4.4.3 C++ Compiler

#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <memory.h>

#define FI(i,a) for (int i=0; i<(a); ++i)
#define FOR(i,s,e) for (int i=(s); i<(e); ++i)
#define MEMS(a,b) memset(a,b,sizeof(a))
#define ISIN(s,a) (s.find(a)!=s.end())
#define VI vector <int>
#define VVI vector <vector <int> >
#define pb push_back
#define mp make_pair
#define pnt pair <int,int>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define ABS(a) (((a)>0)?(a):-(a))
#define LL long long
#define U unsigned
#define ALL(a) a.begin(),a.end()

using namespace std;

#define DOUT(a) cerr << a << endl;
#define SOUT(a) cerr << a << "  ";

pair <LL , LL> a[100];
int n,t,b,k;
int tt;

int main()
{
	//freopen("sample.in","rt",stdin);
	freopen("input.in","rt",stdin);
	freopen("result.txt","wt",stdout);
	cin >> tt;
	FI(it,tt)
	{
		cin >> n >> k >> b >> t;
		FI(i,n) cin >> a[i].first;
		FI(i,n) cin >> a[i].second;
		int swaps=0;
		//int lastc=n;
		int c=0;
		for (int i=n-1; i>=0; --i)
		{
			if (a[i].first+a[i].second*t>=(LL)b) {swaps+=(n-i-1-c); c++;}
			if (c==k) break;
		}
		printf("Case #%d: ",it+1);
		if (c<k) printf("IMPOSSIBLE\n");
		else printf("%d\n",swaps);
	}

	return 0;
}
