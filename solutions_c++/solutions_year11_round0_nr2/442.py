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
#define SZ(v) (int)v.size()
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

int main()
{
#ifdef HOME_PC
	//freopen ("input.txt","r",stdin);
	freopen ("B-large.in","r",stdin);
	freopen ("output.txt","w",stdout);
#endif

	int tt;
	scanf("%d",&tt);
	for(int cas = 1;cas<=tt;++cas)
	{
		char trans[256][256];
		mset(trans,'#');
		bool opp[256][256];
		mset(opp,false);

		int T; cin>>T;
		FOR(i,0,T)
		{
			string s;
			cin>>s;
			int a = s[0], b = s[1], c = s[2];
			trans[a][b] = trans[b][a] = c;
		}
		int Op; cin>>Op;
		FOR(i,0,Op)
		{
			string s;
			cin>>s;
			int a = s[0], b = s[1];
			opp[a][b] = opp[b][a] = true;
		}
		
		int N;
		cin>>N;

		string s;
		cin>>s;
		vector<char> st;
		REPSZ(i,s)
			if(st.empty())
				st.push_back(s[i]);
			else
			{
				int a = st.back(), b = s[i];
				if(trans[a][b] != '#')
				{
					st.pop_back();
					st.push_back(trans[a][b]);
					continue;
				}
				REPSZ(j,st)
					if(opp[st[j]][b])
					{
						st.clear();
						break;
					}
				if(!st.empty())
					st.push_back(s[i]);
			}

		
		printf("Case #%d: ",cas);
		printf("[");
		REPSZ(i,st)
		{
			if(i)
				printf(", ");
			printf("%c",st[i]);
		}
		puts("]");

	}
#ifdef HOME_PC
	cerr<<endl<<"Execution time = "<<clock()<<" ms"<<endl;
#endif
	return 0;
}

