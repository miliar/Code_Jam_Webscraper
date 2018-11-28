#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <sstream>
#include <numeric>
#include <functional>
#include <set>
#include <cmath>
#include <stack>
#include <fstream>
#include <cassert>
#ifdef HOME_PC
#include <ctime>
#endif
using namespace std;

#pragma comment(linker,"/stack:16000000")
#pragma warning (disable : 4996)

#define ALL(v) v.begin(),v.end()
#define SZ(v) ((int)(v.size()))
#define mset(A,x) memset((A),(x),sizeof(A))
#define FOR(i,start,N) for(int i=(start);i<(N);++i)
#define FORSZ(i,start,v) FOR(i,start,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define FORE(i,start,N) FOR(i,start,N+1)
#define make_unique(v) v.resize(unique(ALL(v))-v.begin())
#define debug(x) cout<<#x<<" = "<<x<<endl;
#define adebug(A,N) FOR(i,0,N) cout<<#A<<"["<<i<<"] = "<<A[i]<<endl;
#define adebug2d(a,n,m) FOR(i,0,n) { FOR(j,0,m) { cout<<a[i][j]<<" ";} cout<<endl;}
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)
#define sqr(x) ((x)*(x))


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<25;
const double eps = 1e-9;

string ntos(int n)
{
	ostringstream ss;
	ss<<n;
	return ss.str();
}

int main()
{
#ifdef HOME_PC
	freopen ("C-large.in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("output.txt","w",stdout);
#else
	//freopen ("input.txt","r",stdin);
	//freopen ("output.txt","w",stdout);
#endif
	int numTests = 2;
	cin>>numTests;
	FORE(testCase,1,numTests)
	{
		int A = 1000000,B = 2000000;
		cin>>A>>B;
		bool was[2100000];
		mset(was,false);
		int ans = 0;
		FORE(n,A,B)
		{
			if(was[n])
				continue;
			set<int> st;
			string ns = ntos(n);
			REPSZ(i,ns)
			{
				ns += ns[0];
				ns.erase(0,1);
				if(ns[0] == '0') continue;
				int x = atoi(ns.c_str());
				if(x>=A && x<=B)
					st.insert(x);
			}
			for(set<int>::iterator it = st.begin();
				it != st.end();
				++it)
			{
				was[*it] = true;
			}
			ans+=st.size() * (st.size() - 1) / 2;
		}
		printf("Case #%d: %d\n",testCase,ans);
	}
	
#ifdef HOME_PC
	cerr<<endl<<"Execution time = "<<clock()<<" ms"<<endl;
#endif
	return 0;
}
