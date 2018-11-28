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

string s;
bool flag=false;

void run(void)
{
	int64 res=0;
	rep(i,s.size()) res = (res<<1) + s[i] - '0';
	int64 tmp = (int64) (sqrt((double)res)+0.5);
	if(tmp*tmp == res) flag=true;
}

void dfs(int t)
{
	if(t == s.size()) { run(); return;}
	if(s[t] == '?')
	{
		s[t] = '0';
		dfs(t+1);
		if(flag) return;
		s[t] = '1';
		dfs(t+1);
		if(flag) return;
		s[t] = '?';
	}
	else dfs(t+1);
}

int main(void)
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
	int T; cin>>T;
	REP(Case,T)
	{
		flag=false;
		cin>>s;
		//reverse(s.begin(),s.end());
		dfs(0);
		//reverse(s.begin(),s.end());
		cout<<"Case #"<<Case<<": "<<s<<endl;
	}
}