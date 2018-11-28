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


int res[26];

int good(int x, int mask)
{
	if ((mask&(1<<(x-2)))==0) return 0;
	int c=0;
	int k=1;
	FOR(i,2,x)
	{
		if (mask&k) c++;
		k<<=1;
	}
	return c+1;
}

int main()
{
	//freopen("sample.in","rt",stdin);
	freopen("input.in","rt",stdin);
	freopen("result.txt","wt",stdout);
	MEMS(res,0);
	FOR(ii,2,26)
	{
		int cnt=0;
		FI(k,(1<<(ii-1)))
		{
			int x=ii;
			while (1)
			{
				if (x==0) break;
				else if (x==1) {cnt++;  break;}
				x=good(x,k);
			}
		}
		res[ii]=cnt%100003;
	}

	int tt;
	cin >> tt;
	FI(it,tt)
	{
		int n;
		cin >> n;
		printf("Case #%d: %d\n",it+1,res[n]);
	}

	return 0;
}
