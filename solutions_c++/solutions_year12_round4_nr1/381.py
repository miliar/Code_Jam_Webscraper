#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define rep(i,n) for(int i=0;i<(n);++i)
#define REP(i,n) for(int i=1;i<=(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)
#define print(expr) cout<<(#expr)<<" : "<<(expr)<<endl

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long int64;
typedef pair<int,int> pii;
#define tr(it,c) for(auto it=(c).begin(); it!=(c).end(); ++it)
#define all(c) (c).begin(), (c).end()

void setIO(string s)
{
	string inF=s+".in";
	string outF=s+".out";
	freopen(inF.c_str(),"r",stdin);
	freopen(outF.c_str(),"w",stdout);
}

bool solve(void);
int main(void)
{
	setIO("A-large");
	int T; cin>>T;
	REP(Case,T)
	{
		cout<<"Case #"<<Case<<": ";
		cout<<(solve() ? "YES" : "NO")<<endl;
	}
}

const int maxn=10050;
int d[maxn], l[maxn];
int fd[maxn];
int D,n;

bool solve()
{
	cin>>n; rep(i,n) cin>>d[i]>>l[i]; cin>>D;
	memset(fd,-1,sizeof fd);
	fd[0]=2*d[0];
	d[n]=D;
	rep(i,n) if(fd[i]!=-1)
	{
		if(fd[i]>=D) return true;
		for(int j=i+1;j<n && d[j]<=fd[i]; j++)
		{
			fd[j]=max(fd[j],min(d[j]+l[j],2*d[j]-d[i]));
		}
	}
	return false;
}