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
 
using namespace std;
 
#define RP(a,h) for(a=0; a<(h); a++)
#define FR(a,l,h) for(a=(l); a<=(h); a++)
#define GMAX(X, Y) ((X) > (Y) ? (X) : (Y))
#define GMIN(X, Y) ((X) < (Y) ? (X) : (Y))
#define SZ(a) (LL)a.size()
#define ALL(a) a.begin(), a.end()
#define pb push_back
typedef vector <int> VI;
typedef vector <string> VS;
typedef pair<int, int> PII;
#define LL long long

const int INF = 100000000;
const int MAX = 20000000;

bool dfs(int n1,int n2,int a[][MAX],int m1[],int m2[],bool v1[],bool v2[],int x){v1[x]=true;int i;RP(i,n2)if(a[x][i]&&!v2[i]){v2[i]=true;int y=m2[i];if(y==-1){m2[i]=x;m1[x]=i;return true;}else{if(!v1[y]&&dfs(n1,n2,a,m1,m2,v1,v2,y)){m2[i]=x;m1[x]=i;return true;}}}return false;}
bool pushflow(int n1,int n2,int a[][MAX],int m1[],int m2[]){bool v1[MAX];bool v2[MAX];memset(v1,false,sizeof(v1));memset(v2,false,sizeof(v2));int i;RP(i,n1)if(m1[i]==-1&&!v1[i]&&dfs(n1,n2,a,m1,m2,v1,v2,i))return true;return false;}
int bipartite(int n1,int n2,int a[][MAX],int m1[],int m2[]){int i;RP(i,n1)m1[i]=-1;RP(i,n2)m2[i]=-1;int nmatch=0;while(pushflow(n1,n2,a,m1,m2))nmatch++;return nmatch;}

vector <string> split(const string& s, const string& delim = " ") { vector<string> res; string t; for ( unsigned int i = 0 ; i != s.size() ; i++ ) { if ( delim.find( s[i] ) != string::npos ) { if ( !t.empty() ) { res.push_back( t ); t = ""; } } else { t += s[i]; } } if ( !t.empty() ) { res.push_back(t); } return res; }
vector <int> splitInt(const string& s, const string& delim = " ") { vector <string> tok = split(s, delim); vector <int> res; for (unsigned int i = 0; i != tok.size(); i++) res.push_back( atoi( tok[i].c_str() ) ); return res; }

int cache[MAX][11];
int memo[1<<11];
VI a;
int ans;

int happy(int num, int base)
{
	int &res = cache[num][base];
	if (res >= 0) return cache[num][base];
	if (num == 1) return cache[num][base]=1;

	res = 0;
	int nxt = 0;
	while (num > 0)
	{
		nxt += (num%base) * (num%base);
		num /= base;
	}
	return res = happy(nxt, base);
}

void process()
{
	ans = 2;

	while (true)
	{
		bool ok = true;
		int i;
		RP(i, SZ(a))
		if (!happy(ans, a[i])) { ok=false; break; }
		if (ok) return;
		ans ++;
	}
}

int main()
{
	//freopen("A-large.in", "r", stdin); //freopen("sample.out", "w", stdout);
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);

	int tc, testcase, i;
	string str;
	char cc[1000];

	memset(cache, -1, sizeof(cache));
	memset(memo, -1, sizeof(memo));
	
	cin >> tc; cin.getline(cc, 1000);

	RP(testcase, tc)
	{
		cin.getline(cc, 1000);
		str = string(cc);
		a = splitInt(str);
		int mask = 0;
		RP(i, SZ(a)) mask |= 1<<(a[i]-2);
		if (memo[mask] >= 0) ans = memo[mask];
		else
		{
			process();
			memo[mask] = ans;
		}
		printf("Case #%d: %d\n", (testcase+1), ans);
	}

	return 0;
}
